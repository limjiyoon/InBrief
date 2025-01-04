from abc import ABC, abstractmethod


class Summarizer(ABC):
    """Abstract class for summarizing text."""

    @abstractmethod
    def summarize(self, text: str) -> str:
        pass
