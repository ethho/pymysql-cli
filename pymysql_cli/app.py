import typer
from typing_extensions import Annotated

app = typer.Typer()

#


@app.command()
def main(
    host: Annotated[str, typer.Argument(envvar="PYMYSQL_HOST")],
    user_name: Annotated[str, typer.Argument(envvar="PYMYSQL_USER")],
    password: Annotated[str, typer.Argument(envvar="PYMYSQL_PASS")],
    sql: str,
):
    """
    Run a SQL query.
    """
    print(f"{host=}")
    print(f"{user_name=}")
    print(f"{password=}")
    print(f"{sql=}")
