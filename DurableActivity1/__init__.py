# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import asyncio
import logging
import time

def main(sleep: float):
    logging.info(f"Started activity with input = '{sleep}'. ")
    # await asyncio.sleep(sleep)
    time.sleep(sleep)
    logging.info(f"Finished activity with input = '{sleep}'.")
    return "done"
