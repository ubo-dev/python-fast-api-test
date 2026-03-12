from pydantic_settings import BaseSettings
from pydantic import computed_field

class Settings(BaseSettings):
    postgres_user: str
    postgres_password: str
    postgres_db: str
    postgres_host: str = "localhost"  # override to "db" in Docker
    postgres_port: int = 5432

    @computed_field
    @property
    def database_url(self) -> str:
        return (
            f"postgresql+asyncpg://{self.postgres_user}:"
            f"{self.postgres_password}@{self.postgres_host}:"
            f"{self.postgres_port}/{self.postgres_db}"
        )

    model_config = {"env_file": ".env"}  # pydantic v2 style

settings = Settings()