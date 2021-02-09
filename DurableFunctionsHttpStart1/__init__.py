# This function an HTTP starter function for Durable Functions.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable activity function (default name is "Hello")
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt
 
import logging

import azure.functions as func
import azure.durable_functions as df


async def main(req: func.HttpRequest, starter: str) -> func.HttpResponse:
    client = df.DurableOrchestrationClient(starter)
    sleep_time = float(req.params.get('sleep'))
    instance_id = await client.start_new("DurableFunctionsOrchestrator1", None, sleep_time)
    logging.info(f"Started orchestration with ID = '{instance_id}', sleep_time = {sleep_time}.")
    return client.create_check_status_response(req, instance_id)