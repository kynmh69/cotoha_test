from enum import Enum, auto
from typing import Any, Dict, List

from requests import Response
from requests import post

from src.abstract.cotoha_abs import CotohaApiAbc, CotohaResponseAbc
from src.logger.logger import LoggerUtils


class CotohaApiResponse(CotohaResponseAbc):
    def __init__(self, result: List[Dict[str, Any]], status: int, message: str):
        super().__init__(result, status, message)
        return


class RequestBody(Enum):
    """

    """
    default = auto()
    kuzure = auto()


class CotohaApi(CotohaApiAbc):
    def __init__(self, client_id: str = None, client_secret: str = None) -> None:
        """
        class cotoha api.
        :rtype: None
        :param client_id:
        :param client_secret:
        """
        super().__init__(client_id, client_secret)
        self.__logger = LoggerUtils.get_instance()
        self.get_access_token()
        return

    def get_access_token(self) -> None:
        """
        get Access token
        {
            "access_token": "アクセストークン",
            "token_type": "bearer",
            "expires_in": "残り有効期限(秒)" ,
            "scope": "" ,
            "issued_at": "トークン発行日時(エポックタイムからの経過ミリ秒数)"
        }
        """
        header = {
            "Content-Type": "application/json;charset=UTF-8"
        }
        payload = {
            "grantType": "client_credentials",
            "clientId": self.client_id,
            "clientSecret": self.client_secret
        }
        response: Response = post(self.access_token_publish_url, headers=header, json=payload)
        self.__logger.debug(f'Response: {response.json()}')
        self.access_token = response.json().get('access_token')
        return

    def architecture_analyze_api(self, sentence: str, req_body: RequestBody = RequestBody.default.name) \
            -> CotohaApiResponse:
        """
        構文解析
        :param sentence:
        :param req_body:
        :return:
        """
        self.__logger.debug(self)
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": f"Bearer {self.access_token}"
        }
        payload = {
            "sentence": sentence,
            "type": req_body
        }
        return self.post('/nlp/v1/parse', payload, header)

    def sentiment(self, sentence: str) -> CotohaApiResponse:
        """
        感情分析API
        :param sentence:
        :return:
        """
        self.__logger.debug(self)
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": f"Bearer {self.access_token}"
        }
        payload = {
            "sentence": sentence
        }
        return self.post('/nlp/v1/sentiment', payload, header)

    def named_entity_extraction(self, sentence, req_body: RequestBody = RequestBody.default.name)\
            -> CotohaApiResponse:
        """
        固有表現抽出
        :param sentence:
        :param req_body:
        :return:
        """
        self.__logger.debug(self)
        header = {
            "Content-Type": "application/json;charset=UTF-8",
            "Authorization": f"Bearer {self.access_token}"
        }
        payload = {
            "sentence": sentence,
            "type": req_body
        }
        return self.post('/nlp/v1/ne', payload, header)

    def post(self, resource: str, payload: dict, header: dict) -> CotohaApiResponse:
        """
        Request to API.
        :param resource:
        :param payload:
        :param header:
        :return:
        """
        response: Response = post(self.uri + resource, headers=header, json=payload)
        self.__logger.debug(f'Response: {response.json()}')
        return CotohaApiResponse(response.json().get('result'), response.json().get('status'),
                                 response.json().get('message'))

    def __str__(self) -> str:
        s = (f"uri: {self.uri}, "
             f"access token: {self.access_token}")
        return s
