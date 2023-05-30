from oauthlib.oauth2 import LegacyApplicationClient
from requests_oauthlib import OAuth2Session

import utils

TOKEN_URL = "https://api.xbrl.us/oauth2/token"


def fetch_token():
    secrets = utils.read_secrets()

    client = LegacyApplicationClient(client_id=secrets["CLIENT_ID"])
    oauth = OAuth2Session(client=client)

    return oauth.fetch_token(token_url=TOKEN_URL, username=secrets["USERNAME"], password=secrets["PASSWORD"],
                             client_id=secrets["CLIENT_ID"],
                             client_secret=secrets["CLIENT_SECRET"], include_client_id=True)
