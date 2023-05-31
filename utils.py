from tinydb import TinyDB, Query

db = TinyDB('data/credentials.json')


def check_credentials():
    Entry = Query()
    client_id = db.search(Entry.key == 'client_id')
    client_secret = db.search(Entry.key == 'client_secret')

    if (client_id and client_secret) and (len(client_id) == 1 and len(client_secret) == 1):
        return {'client_id': client_id[0]['value'], 'client_secret': client_secret[0]['value']}
    else:
        return None


def insert_into_db(key, value):
    db.insert({'key': key, 'value': value})
