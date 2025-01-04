from __future__ import annotations


class YoutubeInBrief:
    """Download transcript from YouTube video and summarize it.

    Usage:
    >>> yt = YoutubeInBrief()
    >>> transcript = yt.fetch_transcript(video_url)
    >>> summary = yt.summarize(transcript)
    """

    def __init__(self):
        pass

    # TODO: define more elaborate type of transcript
    def fetch_transcript(self, video_id: str) -> None:
        """Fetch transcript from YouTube video."""
        pass

    # TODO: define more elaborate type of transcript and return type
    def summarize(self, transcript: list) -> None:
        """Summarize the transcript."""
        pass
