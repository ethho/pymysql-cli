import pymysql.cursors
import typer
from typing import Dict, List, Any, Optional

SQLResult = List[Dict[str, Any]]


def get_connection(
    host: str, user: str, password: str, database: Optional[str] = None
) -> pymysql.connections.Connection:
    try:
        conn = pymysql.connect(
            host=host,
            user=user,
            password=password,
            database=database,
            # charset="utf8mb4",
            cursorclass=pymysql.cursors.DictCursor,
        )
    except pymysql.err.OperationalError:
        typer.Abort("Could not connect to the database with these credentials.")
        raise
    return conn


def run_sql(sql: str, **config) -> SQLResult:
    connection = get_connection(**config)
    with connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute(sql)
                result = cursor.fetchmany(size=config.get("page_size", 10_000))
                return result
            except pymysql.err.OperationalError as e:
                typer.Abort(f"Error: {e}")
                raise
