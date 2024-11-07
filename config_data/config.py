from dataclasses import dataclass
from environs import Env

@dataclass
class TgBot:
    """Bot token"""
    token: str

@dataclass
class Config:
    """Bot configuration"""
    tg_bot: TgBot

def load_config(path: str | None = None) -> Config:
    """Load config from .env file or return default config"""
    env = Env()
    env.read_env(path)
    return Config(tg_bot=TgBot(token=env('BOT_TOKEN')))
