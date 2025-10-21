import os
import argparse  # handle command-line arguments
from dotenv import load_dotenv
from settings import Settings
import yaml
import subprocess


def export_envs(environment: str = "dev") -> None:
    env_file_path = f"config/.env.{environment}"
    load_dotenv(env_file_path)

    command = ["sops", "--decrypt", "secrets.yaml"]  # decrypt secrets.yaml in memory
    decrypted_secrets_raw = subprocess.run(
        command, capture_output=True, text=True, check=True
    ).stdout  # read contents in yaml format

    decrypted_secrets = yaml.safe_load(
        decrypted_secrets_raw
    )  # parse yaml into a Python dict

    for key, value in decrypted_secrets.items():  # load values as environment variables
        os.environ[key.upper()] = str(value)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Load environment variables from specified.env file."
    )
    parser.add_argument(
        "--environment",
        type=str,
        default="dev",
        help="The environment to load (dev, test, prod)",
    )
    args = parser.parse_args()

    export_envs(args.environment)  # this gets a string passed after --environment

    with open("secrets.yaml", "r") as file:
        secrets = yaml.safe_load(file)

    settings = Settings()  # calls the Settings class from settings.py

    print("APP_NAME: ", settings.APP_NAME)
    print("ENVIRONMENT: ", settings.ENVIRONMENT)
    print("API Key:", settings.API_KEY)
