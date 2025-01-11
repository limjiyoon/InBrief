from __future__ import annotations

from pprint import pprint

from youtube_transcript_api import YouTubeTranscriptApi

from inbrief.summarizer.base import Summarizer
from inbrief.summarizer.logic_tree_summarizer import LogicTreeSummarizer
from inbrief.types import Transcript
from inbrief.utils import video_id_from_youtube_url, wrap_transcript


class YoutubeInBrief:
    """Download transcript from YouTube video and summarize it.

    Usage:
     >>> from inbrief.summarizer.simple_summarizer import SimpleSummarizer
     >>> summarizer = SimpleSummarizer("models/gemini-1.5-flash")
     >>> video_url = "https://www.youtube.com/watch?v=example"
     >>> yt = YoutubeInBrief(summarizer=summarizer)
     >>> transcript = yt.fetch_transcript(video_url)
     # transcript example:
     # Transcript(chunks=[TranscriptChunk(text="Hello world", start=0.0, duration=1.5), ...])
     >>> summary = yt.summarize(transcript)  # Returns summarized text
    """

    def __init__(self, summarizer: Summarizer):
        self._summarizer = summarizer

    def fetch_transcript(self, video_url: str) -> Transcript:
        """Fetch transcript from YouTube video.

        If an English transcript is available, it will be fetched.
        If not, a Korean transcript will be fetched if available.
        Otherwise, a ValueError will be raised.
        """
        video_id = video_id_from_youtube_url(video_url)
        raw_transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=["en", "ko"])
        if raw_transcript is None:
            raise ValueError(f"Transcript not found in the provided URL: {video_url}.")
        return wrap_transcript(raw_transcript)

    def summarize(self, transcript: Transcript) -> str:
        """Summarize the transcript."""
        text = " ".join(chunk.text for chunk in transcript.chunks)
        return self._summarizer.summarize(text)


if __name__ == "__main__":
    # Yannic Kilcher's video on "Byte Latent Transformer: Patches Scale Better Than Tokens (Paper Explained)"
    video_url = "https://www.youtube.com/watch?v=loaTGpqfctI"
    # summarizer = StructuredSummarizer("models/gemini-1.5-flash"
    summarizer = LogicTreeSummarizer("models/gemini-1.5-flash", max_depth=3)
    youtube_inbrief = YoutubeInBrief(summarizer=summarizer)
    transcript = youtube_inbrief.fetch_transcript(video_url)
    summary = youtube_inbrief.summarize(transcript)
    pprint(summary)
