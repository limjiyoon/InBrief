from dataclasses import dataclass


@dataclass
class TranscriptChunk:
    text: str
    start: float
    duration: float


@dataclass
class Transcript:
    transcript: list[TranscriptChunk]
