import pandas as pd
import requests
from config import API_SERVER
from app.logger import logger
from app.utils.appUtils import handle_api_connection


@handle_api_connection
def fetchDataFromDbWithRelations(tableName):
    """
    Fetch table data with server-side relation processing.
    """

    response = requests.get(
        f"{API_SERVER}/parameters/get_table_with_relations/{tableName}",
        timeout=10
    )

    response.raise_for_status()
    result = response.json()

    if result.get("status") != "success":
        logger.error(f"Failed to fetch table with relations: {tableName}")
        return pd.DataFrame()
    logger.info(f"Fetched table with relations: {tableName}")
    return pd.DataFrame(
        result["data"],
        columns=result["columns"]
    )
