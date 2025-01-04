"""Configuration settings for the application."""

from pydantic import Field
from pydantic_settings import (
    BaseSettings,
    PydanticBaseSettingsSource,
    SettingsConfigDict,
    TomlConfigSettingsSource,
)

from src.inbrief.utils import root_dir


class Config(BaseSettings):
    """"""

    youtube_api_key: str = Field(...)
    gemini_api_key: str = Field(...)
    model_config = SettingsConfigDict(toml_file=root_dir / "configs.toml")

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
Config = Config()  # pyright: ignore[reportCallIssue, reportAssignmentType]
