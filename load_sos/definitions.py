from . import assets
from dagster import Definitions, load_assets_from_modules, EnvVar
from dagster_embedded_elt.dlt import DagsterDltResource
from dagster_snowflake_pandas import SnowflakePandasIOManager

dlt_resource = DagsterDltResource()
all_assets = load_assets_from_modules([assets])

defs = Definitions(
    assets = all_assets,
    resources = {
        "dlt": dlt_resource,
        "io_manager": SnowflakePandasIOManager(
            account = EnvVar("SNOWFLAKE_ACCOUNT"),
            user = EnvVar("SNOWFLAKE_USER"),
            password = EnvVar("SNOWFLAKE_PASSWORD"),
            database = "raw",
            schema = "sos_data",
            warehouse = "compute_wh",
            role = "sysadmin",
        )
    }
)
