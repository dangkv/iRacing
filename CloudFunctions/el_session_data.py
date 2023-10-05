from iRacingSDK.client import Client

if __name__ == "__main__":
    username = ""
    password = ""

    ir = Client(username, password)
    result = ir.lap_data(subsession_id=64059658)
    print(result)
    return result
