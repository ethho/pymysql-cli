import typer
from typing_extensions import Annotated
from rich.console import Console
from rich.table import Table
from .sql import run_sql

console = Console()

app = typer.Typer()


@app.command()
def main(
    host: Annotated[str, typer.Argument(envvar="PYMYSQL_HOST")],
    user_name: Annotated[str, typer.Argument(envvar="PYMYSQL_USER")],
    password: Annotated[str, typer.Argument(envvar="PYMYSQL_PASS")],
    sql: str,
    format: Annotated[str, typer.Option("table", "--format")],
):
    """
    Run a SQL query.
    """
    print(f"{host=}")
    print(f"{user_name=}")
    print(f"{password=}")
    print(f"{sql=}")
    resp = run_sql(sql, host=host, user=user_name, password=password)
    breakpoint()
