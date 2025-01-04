from __future__ import annotations

from youtube_transcript_api import YouTubeTranscriptApi


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
    def fetch_transcript(self, video_id: str) -> list:
        """Fetch transcript from YouTube video.

        If there is english transcript available, it will be fetched.
        If not and there is korean transcript available, it will be fetched.
        Otherwise, it will return None.
        """
        return YouTubeTranscriptApi.get_transcript(video_id=video_id, languages=["en", "ko"])

    # TODO: define more elaborate type of transcript and return type
    def summarize(self, transcript: list) -> None:
        """Summarize the transcript."""
        pass


if __name__ == '__main__':
    # Yannic Kilcher's video on "Byte Latent Transformer: Patches Scale Better Than Tokens (Paper Explained)"
    video_id = "loaTGpqfctI"
    youtube_inbrief = YoutubeInBrief()
    transcript = youtube_inbrief.fetch_transcript(video_id)
    print(transcript)