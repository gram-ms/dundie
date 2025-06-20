import rich_click as click
import json

from importlib.metadata import version
from rich.console import Console
from rich.table import Table
from dundie import core

click.rich_click.USE_RICH_MARKUP = True
click.rich_click.USE_MARKDOWN = True
click.rich_click.SHOW_ARGUMENTS = True
click.rich_click.GROUP_ARGUMENTS_OPTIONS = True
click.rich_click.SHOW_METAVARS_COLUMN = False
click.rich_click.APPEND_METAVARS_HELP = True


# Defining a main command group
@click.group()
@click.version_option(version("dundie"))
def main():
    """Dunder Mifflin Rewards System.
    This cli aplication controls DM rewards.
    """


# Defining a subcommand to main group
@main.command()
@click.argument("filepath", type=click.Path())
def load(filepath):
    """Loads the file to the database

    # Features

    - Validates data
    - Parses the file
    - Loads to database
    """
    table = Table(title="Dunder mifflin Associates")
    headers = ["name", "dept", "role", "created", "e-mail"]
    for header in headers:
        table.add_column(header, style="blue")

    result = core.load(filepath)
    for person in result:
        table.add_row(*[str(value) for value in person.values()])

    console = Console()
    console.print(table)


@main.command()
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.option("--output", default=None)
def show(output, **query):
    """Show information about users"""
    result = core.read(**query)
    if output:
        with open(output, "w") as output_file:
            output_file.write(json.dumps(result))

    if not result:
        print("Nothing to show")

    table = Table(title="Dunder Mifflin Report")
    for key in result[0]:
        table.add_column(key.title(), style="blue")

    for person in result:
        table.add_row(*[str(value) for value in person.values()])

    console = Console()
    console.print(table)


@main.command()
@click.argument("value", type=click.INT, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def add(ctx, value, **query):
    """Add points to the user or dept"""
    core.add(value, **query)
    ctx.invoke(show, **query)


@main.command()
@click.argument("value", type=click.INT, required=True)
@click.option("--dept", required=False)
@click.option("--email", required=False)
@click.pass_context
def remove(ctx, value, **query):
    """remove points to the user or dept"""
    core.add(-value, **query)
    ctx.invoke(show, **query)
