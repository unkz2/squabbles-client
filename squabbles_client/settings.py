from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    SQUABBLES_USERNAME: str = 'username'
    SQUABBLES_PASSWORD: str = 'password'
