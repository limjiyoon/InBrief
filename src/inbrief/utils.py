from pathlib import Path

from inbrief.types import Transcript, TranscriptChunk

root_dir = Path(__file__).parents[2]


def video_id_from_url(url: str) -> str:
    """Extract video ID from YouTube video URL.

    Example:
        "https://www.youtube.com/watch?v=loaTGpqfctI" -> "loaTGpqfctI"
    """
    return url.split("v=")[1]


def wrap_transcript(raw_transcript: list) -> Transcript:
    """Wrap raw transcript into a Transcript object."""
    return Transcript(
        transcript=[
            TranscriptChunk(text=chunk["text"], start=chunk["start"], duration=chunk["duration"])
            for chunk in raw_transcript
        ]
    )
