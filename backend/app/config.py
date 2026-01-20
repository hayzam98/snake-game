"""
Configuration settings for the Snake Game application.
Uses pydantic-settings for environment variable management.
"""
from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache


class Settings(BaseSettings):
    """Application settings loaded from environment variables."""
    
    # Database settings
    DB_HOST: str
    DB_PORT: int
    DB_USER: str
    DB_PASSWORD: str
    DB_NAME: str
    
    # Application settings
    APP_NAME: str
    APP_VERSION: str
    DEBUG: bool = False
    
    # Security
    SECRET_KEY: str
    
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True
    )
    
    @property
    def database_url(self) -> str:
        """Build MySQL database URL."""
        return (
            f"mysql+pymysql://{self.DB_USER}:{self.DB_PASSWORD}"
            f"@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        )


@lru_cache
def get_settings() -> Settings:
    """
    Get cached settings instance.
    lru_cache ensures we only load settings once.
    """
    return Settings()
