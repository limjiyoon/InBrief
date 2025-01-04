from dataclasses import dataclass


@dataclass(frozen=True)
class TranscriptChunk:
    """A transcript at specific time."""
    text: str
    start: float
    duration: float


@dataclass
class Transcript:
    """A collection of transcript chunks."""
    transcript: list[TranscriptChunk]
