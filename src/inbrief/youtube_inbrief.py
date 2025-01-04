from __future__ import annotations

from youtube_transcript_api import YouTubeTranscriptApi

from inbrief.types import Transcript, TranscriptChunk


class YoutubeInBrief:
    """Download transcript from YouTube video and summarize it.

    Usage:
    >>> yt = YoutubeInBrief()
    >>> transcript = yt.fetch_transcript(video_id)
    >>> summary = yt.summarize(transcript)
    """

    def __init__(self):
        pass

    # TODO: define more elaborate type of transcript
    def fetch_transcript(self, video_id: str) -> Transcript:
        """Fetch transcript from YouTube video.

        If there is english transcript available, it will be fetched.
        If not and there is korean transcript available, it will be fetched.
        Otherwise, it will return None.
        """
        raw_transcript = YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=["en", "ko"])
        if raw_transcript is None:
            raise ValueError("Transcript not found.")
        return self._wrap_transcript(raw_transcript)

    def _wrap_transcript(self, raw_transcript: list) -> Transcript:
        """Wrap raw transcript into a Transcript object."""
        return Transcript(
            transcript=[
                TranscriptChunk(text=chunk["text"], start=chunk["start"], duration=chunk["duration"])
                for chunk in raw_transcript
            ]
        )

    # TODO: define more elaborate type of transcript and return type
    def summarize(self, transcript: list) -> None:
        """Summarize the transcript."""
        pass


if __name__ == "__main__":
    # Yannic Kilcher's video on "Byte Latent Transformer: Patches Scale Better Than Tokens (Paper Explained)"
    video_id = "loaTGpqfctI"
    youtube_inbrief = YoutubeInBrief()
    transcript = youtube_inbrief.fetch_transcript(video_id)
    print(transcript)
