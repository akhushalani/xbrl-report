from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

import utils


def fetch_token():
    client = LegacyApplicationClient(client_id=utils.get_from_db('client_id'))
    oauth = OAuth2Session(client=client)

    return oauth.fetch_token(**utils.create_token_request_body())
