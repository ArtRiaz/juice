from dataclasses import dataclass

from environs import Env


@dataclass
class TgBot:
    """
    Creates the TgBot object from environment variables.
    """

    token: str

    @staticmethod
    def from_env(env: Env):
        """
        Creates the TgBot object from environment variables.
        """
        token = env.str("TOKEN")

        return TgBot(token=token)


@dataclass
class Config:
    tg_bot: TgBot


def load_config(path: str = None) -> Config:
    """
    This function takes an optional file path as input and returns a Config object.
    :param path: The path of env file from where to load the configuration variables.
    It reads environment variables from a .env file if provided, else from the process environment.
    :return: Config object with attributes set as per environment variables.
    """

    # Create an Env object.
    # The Env object will be used to read environment variables.
    env = Env()
    env.read_env(path)

    return Config(
        tg_bot=TgBot.from_env(env)
    )
