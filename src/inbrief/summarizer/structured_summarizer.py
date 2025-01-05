

from inbrief.llm_factory import LlmFactory
from inbrief.summarizer.base import Summarizer
from inbrief.utils import Prompts


class StructuredSummarizer(Summarizer):
    """Summarize contents using a language model with simple script."""

    def __init__(self, model_name: str):
        if model_name not in LlmFactory().available_models():
            raise ValueError(f"Model '{model_name}' is not available.")
        self._model_name = model_name
        self._model = LlmFactory().create(model_name)

        self._components = [
            "keypoints",
            "categories",
            "tags",
            "sections",
        ]

    def summarize(self, text: str) -> str:
        def extract() -> dict[str, str]:
            return {
                "keypoints": self._extract(Prompts.extract_keypoints, text),
                "categories": self._extract(Prompts.extract_categories, text),
                "tags": self._extract(Prompts.extract_tags, text),
                "sections": self._extract(
                    Prompts.extract_section_details, self._extract(Prompts.extract_sections, text)
                ),
            }

        structured = extract()
        return "\n\n".join([f"#{key.capitalize()}\n{content}" for key, content in structured])

    def _extract(self, prompt: str, contents: str) -> str:
        return self._model.generate_content([prompt, contents]).text
