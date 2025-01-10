import re
from pathlib import Path

from pydantic import Field
from pydantic_settings import BaseSettings, PydanticBaseSettingsSource, SettingsConfigDict, TomlConfigSettingsSource

from inbrief.types import Transcript, TranscriptChunk

root_dir = Path(__file__).parents[2]


class Prompts(BaseSettings):
    """Settings for prompts used in the summarization process."""

    extract_keypoints: str = Field(...)
    extract_categories: str = Field(...)
    extract_tags: str = Field(...)
    extract_sections: str = Field(...)
    extract_section_details: str = Field(...)
    extract_core_statement: str = Field(...)
    extract_support_statements: str = Field(...)

    model_config = SettingsConfigDict(toml_file=root_dir / "prompts" / "prompts.toml")

    @classmethod
    def settings_customise_sources(
        cls,
        settings_cls: type[BaseSettings],
        init_settings: PydanticBaseSettingsSource,
        env_settings: PydanticBaseSettingsSource,
        dotenv_settings: PydanticBaseSettingsSource,
        file_secret_settings: PydanticBaseSettingsSource,
    ) -> tuple[PydanticBaseSettingsSource, ...]:
        _ = init_settings, env_settings, dotenv_settings, file_secret_settings  # required, but don't use
        return (TomlConfigSettingsSource(settings_cls),)


# Override the name for singleton settings instance
Prompts = Prompts()  # pyright: ignore[reportCallIssue, reportAssignmentType]


def video_id_from_youtube_url(url: str) -> str:
    """Extract video ID from YouTube video URL.

    Example:
        "https://www.youtube.com/watch?v=loaTGpqfctI" -> "loaTGpqfctI"
    """
    match = re.search(r"(?<=www\.youtube\.com/watch\?v=)[\w-]+", url)
    if match is None:
        raise ValueError(f"No 'www.youtube.com/watch?v=' found in the provided URL: {url}")
    return match.group(0)


def wrap_transcript(raw_transcript: list[dict[str, str | float]]) -> Transcript:
    """Wrap raw transcript into a Transcript object.

    Args:
        raw_transcript: List of dictionaries containing transcript chunks.
            Each chunk must have 'text' (str), 'start' (float), and 'duration' (float).

    Returns:
        Transcript object containing the processed chunks.

    Raises:
        ValueError: If raw_transcript is empty or chunks are missing required keys.
        TypeError: If field types are incorrect.
    """
    if not raw_transcript:
        raise ValueError("Raw transcript cannot be empty")

    if not all(
        isinstance(chunk, dict)
        and all(key in chunk and isinstance(chunk[key], str | float) for key in ("text", "start", "duration"))
        for chunk in raw_transcript
    ):
        raise ValueError("Each chunk must have 'text', 'start', and 'duration' fields")

    return Transcript(
        chunks=[
            TranscriptChunk(
                text=str(chunk["text"]).strip(),
                start=float(chunk["start"]),
                duration=float(chunk["duration"]),
            )
            for chunk in raw_transcript
        ]
    )
