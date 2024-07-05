import typer
import json
from enum import Enum
from typing_extensions import Annotated
from rich.console import Console
from rich.table import Table
from .sql import run_sql, SQLResult

console = Console()

app = typer.Typer()


class Format(str, Enum):
    table = "table"
    yaml = "yaml"
    json = "json"


def render_table(resp: SQLResult):
    table = Table()
    if not resp:
        table.add_column("No results")
        console.print(table)
        return
    cols: list[str] = list(resp[0].keys())
    for col in cols:
        table.add_column(col)
    for row in resp:
        string_row = [str(row[col]) for col in cols]
        table.add_row(*string_row)
    console.print(table)


def render_json(resp: SQLResult):
    print(json.dumps(resp, indent=2, default=str))


def render_yaml(resp: SQLResult):
    raise NotImplementedError()


@app.command()
def main(
    host: Annotated[str, typer.Argument(envvar="PYMYSQL_HOST")],
    user_name: Annotated[str, typer.Argument(envvar="PYMYSQL_USER")],
    password: Annotated[str, typer.Argument(envvar="PYMYSQL_PASS")],
    sql: str,
    database: Annotated[str, typer.Option("--db", "-d")] = None,
    format: Annotated[str, typer.Option("--format", "-f")] = "table",
):
    """
    Run a SQL query.
    """
    resp = run_sql(sql, host=host, user=user_name, password=password, database=database)
    globals()[f"render_{format}"](resp)
