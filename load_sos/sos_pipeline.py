import dagster as dagster
import dlt
from dlt.common import pendulum
from dlt.sources.credentials import ConnectionStringCredentials

from dlt.sources.sql_database import sql_database, sql_table, Table
import sqlalchemy as sa
import pyodbc
import urllib.parse


def get_credentials():
    driver   = dlt.secrets["sources.sql_database.credentials.driver"]
    database = dlt.secrets["sources.sql_database.credentials.database"]
    pwd      = dlt.secrets["sources.sql_database.credentials.pwd"]
    uid      = dlt.secrets["sources.sql_database.credentials.uid"]
    server   = dlt.secrets["sources.sql_database.credentials.server"]
    port     = dlt.secrets["sources.sql_database.credentials.port"]

    conn_str = (
        f"DRIVER={driver};"
        f"SERVER={server};"
        f"DATABASE={database};"
        f"UID={uid};"
        f"PWD={pwd};"
        "Encrypt=yes;"
        "TrustServerCertificate=yes;"
    )
    conn_str_encoded = urllib.parse.quote_plus(conn_str)

    engine_url = f"mssql+pyodbc:///?odbc_connect={conn_str}"
    #print("ENGINE URL:", engine_url)
    return engine_url


##### EXTRACT SOS COMPARTMENT #############

@dlt.resource(#table_name = "sa_cm_soscompartment",
              write_disposition = "replace",
              primary_key = "id_soscompartment"
)
##def get_soscompartment():
##    
##    source_sta = sql_database(
##        get_credentials(),
##        backend="pyarrow"
##    ).with_resources("sa_cm_soscompartment")
##
##    return source_sta

@dlt.source
def soscompartment_source():
    source_sta = sql_database(
        get_credentials(),
        backend="pyarrow"
    ).with_resources("sa_cm_soscompartment")

    return source_sta