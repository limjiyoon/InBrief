from __future__ import annotations

from youtube_transcript_api import YouTubeTranscriptApi

from inbrief.types import Transcript, TranscriptChunk


class YoutubeInBrief:
    """Download transcript from YouTube video and summarize it.

    Usage:
    >>> video_url = "[YouTube video URL]"
    >>> yt = YoutubeInBrief()
    >>> transcript = yt.fetch_transcript(video_url)
    >>> summary = yt.summarize(transcript)
    """

    # TODO: define more elaborate type of transcript
    def fetch_transcript(self, video_url: str) -> Transcript:
        """Fetch transcript from YouTube video.

        If an English transcript is available, it will be fetched.
        If not, a Korean transcript will be fetched if available.
        Otherwise, a ValueError will be raised.
        """
        video_id = self._video_id_from_url(video_url)
        raw_transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=["en", "ko"])
        if raw_transcript is None:
            raise ValueError("Transcript not found.")
        return self._wrap_transcript(raw_transcript)

    def _video_id_from_url(self, url: str) -> str:
        """Extract video ID from YouTube video URL.

        Example:
            "https://www.youtube.com/watch?v=loaTGpqfctI" -> "loaTGpqfctI"
        """
        return url.split("v=")[1]

    def _wrap_transcript(self, raw_transcript: list) -> Transcript:
        """Wrap raw transcript into a Transcript object."""
        return Transcript(
            transcript=[
                TranscriptChunk(text=chunk["text"], start=chunk["start"], duration=chunk["duration"])
                for chunk in raw_transcript
            ]
        )

    # TODO: define more elaborate type of transcript and return type
    # TODO: implement summarization algorithm
    def summarize(self, transcript: list) -> None:
        """Summarize the transcript."""
        pass


if __name__ == "__main__":
    # Yannic Kilcher's video on "Byte Latent Transformer: Patches Scale Better Than Tokens (Paper Explained)"
    video_url = "https://www.youtube.com/watch?v=loaTGpqfctI"
    youtube_inbrief = YoutubeInBrief()
    transcript = youtube_inbrief.fetch_transcript(video_url)
    print(transcript)
