from iRacingSDK.client import Client

@functions_framework.http
def el_session_data(request):
    username = "vo.dangkh@gmail.com"
    password = "22v33zZ4gduRY"

    ir = Client(username, password)
    result = ir.lap_data(subsession_id=64059658)
    print(result)
    return result
