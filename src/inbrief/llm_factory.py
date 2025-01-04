from collections.abc import Iterator

from google import generativeai as genai
from google.generativeai import GenerativeModel

from inbrief.configs import Config
from inbrief.singleton import Singleton


class LlmFactory(metaclass=Singleton):
    """Factory class for Language Models.

    Note:
        This class is a Singleton class.
        It supports only gemini models.

    Usage:
        >>> llm = LlmFactory()
        >>> for model in llm.available_models():
        >>>     print(model)

    """

    def __init__(self):
        self._use_gemini = False

    def create(self, model_name: str, *args, **kwargs) -> GenerativeModel:
        self._configure_gemini()
        assert model_name in self.available_models(), f"Model '{model_name}' is not available."
        return genai.GenerativeModel(model_name, *args, **kwargs)

    def available_models(self) -> Iterator[str]:
        self._configure_gemini()

        for model in genai.list_models():
            if "generateContent" in model.supported_generation_methods:
                yield model.name

    def _configure_gemini(self) -> None:
        if not self._use_gemini:
            genai.configure(api_key=Config.gemini_api_key)
            self._use_gemini = True


if __name__ == "__main__":
    model = LlmFactory().create("models/gemini-1.5-flash")
    print(model)
