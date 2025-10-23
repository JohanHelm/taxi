from dataclasses import dataclass
from environs import Env


@dataclass
class DatabaseConfig:
    db_file: str


@dataclass
class TgBot:
    token: str
    bot_pic: tuple[str]


@dataclass
class TaxiDriver:
    username: str
    password: str
    country: str

@dataclass
class Config:
    tg_bot: TgBot
    db: DatabaseConfig
    taxi_driver: TaxiDriver

def load_config(path: str | None = None) -> Config:

    env: Env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot(
            token=env("BOT_TOKEN"),
            bot_pic=tuple(env("BOT_PIC").split(",")),
        ),
        db=DatabaseConfig(
            db_file=env("DB_FILE"),
        ),
        taxi_driver = TaxiDriver(
            username=env("USERNAME"),
            password=env("PASSWORD"),
            country=env("COUNTRY"),
        )
    )
