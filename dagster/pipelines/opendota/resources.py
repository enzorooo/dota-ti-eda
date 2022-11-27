import httpx

from dagster import resource


@resource
def client_opendotaapi(init_context):
    return httpx.Client(
        base_url="https://api.opendota.com/api/",
    )
