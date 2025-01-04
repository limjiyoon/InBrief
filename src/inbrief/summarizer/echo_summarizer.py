from inbrief.summarizer.base import Summarizer


class EchoSummarizer(Summarizer):
    """Summarize text by echoing the input text."""

    def summarize(self, text: str) -> str:
        return text
