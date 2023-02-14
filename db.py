from pathlib import Path
import pandas as pd
import sqlite3


Con = sqlite3.Connection


def create_temp_tables(con: Con):
    con.executescript(Path("queries/_prelude.sql").read_text())


def fetch_children(con: Con, ref_name: str, target_id: int) -> pd.DataFrame:
    sql = Path("queries/fetch_children.sql").read_text()
    params = { "ref_name": ref_name, "target_id": target_id }
    return pd.read_sql(sql, con, index_col="id", params=params)


def fetch_internal_deps(con: Con, target_id: str) -> pd.DataFrame:
    sql = Path("queries/fetch_internal_deps.sql").read_text()
    params = { "target_id": target_id }
    return pd.read_sql(sql, con, params=params)


def fetch_clients(con: Con, target_file: str) -> pd.DataFrame:
    sql = Path("queries/fetch_clients.sql").read_text()
    params = { "target_file": target_file }
    return pd.read_sql(sql, con, index_col="id", params=params)


def fetch_client_deps(con: Con, target_id: int, target_file: str) -> pd.DataFrame:
    sql = Path("queries/fetch_client_deps.sql").read_text()
    params = { "target_id": target_id, "target_file": target_file }
    return pd.read_sql(sql, con, params=params)