from dagster import AssetExecutionContext
from dagster_embedded_elt.dlt import DagsterDltResource, dlt_assets
from dlt import pipeline
import dlt
from .sos_pipeline import soscompartment_source

@dlt_assets(
    dlt_source = soscompartment_source(),
    dlt_pipeline = dlt.pipeline(
        pipeline_name = "sa_cm_sos",
        destination = "snowflake",
        dataset_name = "sos_data",
        #progess = "log",
    ),
    name = "soscompartment",
    group_name = "sos"
)

def dagster_sos_assets(context: AssetExecutionContext, dlt: DagsterDltResource):
    yield from dlt.run(context = context)

