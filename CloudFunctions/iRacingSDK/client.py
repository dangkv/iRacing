import logging
import json
import requests

import endpoints
import helpers


class Client:
    def __init__(self, username: str, password: str):
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
        )
        self.username = username
        self.password = password
        self.cookies = self._login()


    def _login(self):
        password = helpers.encode_pw(self.username, self.password)
        data = {"email": self.username, "password": password}
        headers = {"Content-Type": "application/json"}
        json_data = json.dumps(data)

        login_response = requests.post(
            endpoints.URL_LOGIN, data=json_data, headers=headers
        )
        return login_response.cookies

    def _build_requests(self, url, params):
        if not self.cookies:
            logging.info("No cookies in cookie jar.")
            self.cookies = self._login()

        logging.info(f'Request being sent to: {url} with params: {params}')

        response = requests.get(
            url,
            params=params,
            cookies=self.cookies,
            allow_redirects=False,
            timeout=10.0
        )
        logging.info(f'Request sent for URL: {response.url}')
        logging.info(f'Status code of response: {response.status_code}')
        logging.debug(f'Contents of the response object: {response.__dict__}')

        response_json = json.loads(response.text)
        link = response_json.get("link")

        response_text = requests.get(link).text

        return response_text

    def _wrap_payload(self, payload, method, endpoint, parameters):
        ## {timestamp, payload, method, endpoint, parameters, username}
        record = {
            "timestamp": helpers.get_current_utc_time(),
            "payload": payload,
            "method": method,
            "endpoint": endpoint,
            "parameters": parameters,
            "username": self.username
        }
        return record

    def lap_data(self, subsession_id: int):
        full_session = []
        parameters = []

        for simsession_number in [0, -1, -2]:
            params = {"subsession_id": subsession_id, "simsession_number": simsession_number}
            results_response = self._build_requests(endpoints.URL_LAP_DATA, params)

            parameters.append(params)
            full_session.append(results_response)

        record = self._wrap_payload(full_session, "lap_data", endpoints.URL_LAP_DATA, parameters)
        return record
