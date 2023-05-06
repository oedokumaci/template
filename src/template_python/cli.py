"""Command line application module."""

import typer

from template_python.config_parser import YAML_CONFIG
from template_python.path import LOGS_DIR
from template_python.utils import check_log_file_name, init_logger

# Define command line arguments and options
log_file_name_argument = typer.Argument(
    YAML_CONFIG.log_file_name,
    help="Name of the log file. Default can be changed in config.yaml.",
)
override_option = typer.Option(False, help="Override the log file if it exists.")


def main(
    log_file_name: str = log_file_name_argument, override: bool = override_option
) -> None:
    """Main function for the command line application.

    Args:
        log_file_name (str): The name of the log file.
        override (bool): Whether to override the log file if it exists.
    """

    # Check if log file exists, if so ask to overwrite
    log_file = LOGS_DIR / log_file_name
    if not override and log_file.exists():
        check_log_file_name(log_file_name)

    # Initialize logger
    init_logger(log_file_name)

    # Print log file path
    print("")
    print(f"logs are saved to {log_file.resolve()}")

    # Exit the program
    raise typer.Exit()
