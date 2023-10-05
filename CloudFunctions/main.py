from iRacingSDK.client import Client

@functions_framework.http
def main(request):
    username = "vo.dangkh@gmail.com"
    password = "22v33zZ4gduRY"

    ir = Client(username, password)
    result = ir.lap_data(subsession_id=64059658)
    print(result)
    return result
