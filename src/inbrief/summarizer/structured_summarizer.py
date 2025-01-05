import asyncio

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
            # "In breif summary",
            # "Key point",
            # "Three Key takeaways",
            # "Why does it matter",
            # "Insights",
            # "In-depth insights",
            # "Possible Quesition and Answers",
            "keypoints",
            "categories",
            "tags",
            "sections",
        ]

    def summarize(self, text: str) -> str:
        # cached_model = self._concontents_cache(contents)
        async def extract() -> dict[str, str]:
            return {
                "keypoints": await self._extract(Prompts.extract_keypoints, text),
                "categories": await self._extract(Prompts.extract_categories, text),
                "tags": await self._extract(Prompts.extract_tags, text),
                "sections": await self._extract(
                    Prompts.extract_section_details, await self._extract(Prompts.extract_sections, text)
                ),
            }

        structured = asyncio.run(extract())
        return "\n\n".join([f"#{key.capitalize()}\n{structured[key]}" for key in self._components])

    async def _extract(self, prompt: str, contents: str) -> str:
        return self._model.generate_content([prompt, contents]).text
