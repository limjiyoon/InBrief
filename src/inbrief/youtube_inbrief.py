from __future__ import annotations

from youtube_transcript_api import YouTubeTranscriptApi

from inbrief.types import Transcript
from inbrief.utils import video_id_from_url, wrap_transcript


class YoutubeInBrief:
    """Download transcript from YouTube video and summarize it.

    Usage:
    >>> video_url = "[YouTube video URL]"
    >>> yt = YoutubeInBrief()
    >>> transcript = yt.fetch_transcript(video_url)
    >>> summary = yt.summarize(transcript)
    """

    def fetch_transcript(self, video_url: str) -> Transcript:
        """Fetch transcript from YouTube video.

        If an English transcript is available, it will be fetched.
        If not, a Korean transcript will be fetched if available.
        Otherwise, a ValueError will be raised.
        """
        video_id = video_id_from_url(video_url)
        raw_transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=["en", "ko"])
        if raw_transcript is None:
            raise ValueError("Transcript not found.")
        return wrap_transcript(raw_transcript)

    # TODO: define more elaborate type of transcript and return type
    # TODO: implement summarization algorithm
    @staticmethod
    def summarize(transcript: list) -> None:
        """Summarize the transcript."""
        pass


if __name__ == "__main__":
    # Yannic Kilcher's video on "Byte Latent Transformer: Patches Scale Better Than Tokens (Paper Explained)"
    video_url = "https://www.youtube.com/watch?v=loaTGpqfctI"
    youtube_inbrief = YoutubeInBrief()
    transcript = youtube_inbrief.fetch_transcript(video_url)
    print(transcript)
