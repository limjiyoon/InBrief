import json

from google.generativeai import GenerationConfig
from pydantic import BaseModel, Field

from inbrief.llm_factory import LlmFactory
from inbrief.summarizer.base import Summarizer
from inbrief.utils import Prompts


class Node(BaseModel):
    statement: str = Field(..., description="The statement")
    keywords: list[str] = Field(..., description="Keywords of the statement")
    description: str = Field(..., description="One paragraph description of the statement")

    def __repr__(self):
        return f"Node(statement={self.statement}, keywords={self.keywords}, description={self.description})"

    def __hash__(self):
        return hash(self.statement)


class LogicTreeSummarizer(Summarizer):
    def __init__(self, model_name: str, max_depth: int):
        self._model = LlmFactory().create(model_name)
        self._max_depth = max_depth

    def summarize(self, text: str) -> str:
        logic_tree = {}
        start_node = self._create_core_node(text=text)
        cur_layer = [start_node]

        for _ in range(self._max_depth):
            next_layer = []
            for node in cur_layer:
                next_nodes = self._create_support_nodes(text=node.statement)
                logic_tree[node] = next_nodes
                next_layer.extend([next_node for next_node in next_nodes if next_node.statement.strip()])

            cur_layer = next_layer

        summarized_text = self._summarize_tree(logic_tree, start_node)
        return summarized_text

    def _create_core_node(self, text: str) -> Node:
        node_json = self._model.generate_content(
            [Prompts.extract_core_statement, text],
            generation_config=GenerationConfig(
                response_mime_type="application/json",
                response_schema=Node,
            ),
        ).text
        print(f"Create core node: {node_json}")
        return Node(**json.loads(node_json))

    def _create_support_nodes(self, text: str) -> list[Node]:
        node_json = self._model.generate_content(
            [Prompts.extract_support_statements, text],
            generation_config=GenerationConfig(
                response_mime_type="application/json",
                response_schema=list[Node],
            ),
        ).text
        print(f"Create support nodes: {node_json}")

        return [Node(**node) for node in json.loads(node_json)]

    def _summarize_tree(self, logic_tree: dict[Node, list[Node]], start_node: Node, level: int = 0) -> str:
        prefix = "  " * level if level > 0 else ""
        results = f"{prefix}- {start_node.statement}\n"

        supportings = [
            self._summarize_tree(logic_tree, node, level + 1) for node in logic_tree[start_node] if node in logic_tree
        ]
        results = f"{results}{''.join(supportings)}"
        return results