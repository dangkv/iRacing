import functions_framework
import os
from client import Client


def get_subsession_ids():
    # Get list of subsession_ids from Sheets
    # Example:
    subsession_ids = [64059658]
    return subsession_ids


def stage_subsession_ids(subsession_ids, full_refresh=False):
    # Compare old and new list of subssession_id and return unprocessed subsession_ids
    # full_refresh option is available to process all subsession_id
    pass


def extract(username, password):
    # Extract data from iRacing API
    data = []
    subsession_ids = get_subsession_ids()
    iRacing = Client(username, password)

    for subsession_id in subsession_ids:
        result = iRacing.lap_data(subsession_id=subsession_id)
        data.append(result)

    return data

def load(data):
    # Load data to BigQuery
    pass



def main():
    username = ""
    password = ""

    data = extract(username, password)
    print(data)
    return data

main()