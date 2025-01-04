from inbrief.llm_factory import LlmFactory
from inbrief.summarizer.base import Summarizer


class SimpleSummarizer(Summarizer):
    """Summarize text using a language model with simple script."""

    def __init__(self, model_name: str):
        assert model_name in LlmFactory().available_models(), f"Model '{model_name}' is not available."
        self._model = LlmFactory().create(model_name)

    def summarize(self, text: str) -> str:
        return self._model.generate_content(["Summarize following contents", text]).text