import re
from pathlib import Path

from inbrief.types import Transcript, TranscriptChunk

root_dir = Path(__file__).parents[2]


def video_id_from_youtube_url(url: str) -> str:
    """Extract video ID from YouTube video URL.

    Example:
        "https://www.youtube.com/watch?v=loaTGpqfctI" -> "loaTGpqfctI"
    """
    match = re.search(r"(?<=www\.youtube\.com/watch\?v=)[\w-]+", url)
    if match is None:
        raise ValueError("Invalid YouTube video URL.")
    return match.group(0)


def wrap_transcript(raw_transcript: list) -> Transcript:
    """Wrap raw transcript into a Transcript object."""
    return Transcript(
        transcript=[
            TranscriptChunk(text=chunk["text"], start=chunk["start"], duration=chunk["duration"])
            for chunk in raw_transcript
        ]
    )
