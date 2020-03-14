import requests

class CotohaApi:
    """
    class cotoha api.
    """
    def __init__(self, client_id, client_secret):
        self.__url = "https://api.ce-cotoha.com/api/dev/"
        self.__client_id = client_id
        self.__client_secret = client_secret
    def get_access_token(self):
        response = requests.get()