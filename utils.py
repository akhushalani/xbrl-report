from tinydb import TinyDB, Query
from dotenv import dotenv_values
from getpass import getpass
db = TinyDB('data/credentials.json')


def __check_pair(public_name, private_name):
    Entry = Query()
    public = db.search(Entry.key == public_name)
    private = db.search(Entry.key == private_name)

    if (public and private) and (len(public) == 1 and len(private) == 1):
        return {public_name: public[0]['value'], private_name: private[0]['value']}
    else:
        return None


def __insert_into_db(key, value):
    db.insert({'key': key, 'value': value})


def acquire_and_store_pair(public_name, private_name, public_display=None, private_display=None):
    public_display = public_display if public_display else public_name.replace("_", " ").title()
    private_display = private_display if private_display else private_name.replace("_", " ").title()

    print(f"Checking for {public_display} and {private_display}")
    pair = __check_pair(public_name, private_name)
    if pair:
        print('Credentials found!')
        print(f"{public_display}: {pair[public_name]}\n{private_display}: {pair[private_name]}")
    else:
        print('Credentials not found, checking .env file...')
        dotenv = dotenv_values('.env')
        if all(name.upper() in dotenv for name in (public_name, private_name)):
            print('Credentials found!')
            __insert_into_db(public_name, dotenv[public_name.upper()])
            __insert_into_db(private_name, dotenv[private_name.upper()])
            print(f"{public_display}: {dotenv[public_name.upper()]}\n{private_display}: {dotenv[private_name.upper()]}")
        else:
            print('Credentials not found in .env file, enter manually or exit.')
            public = input(f"{public_display}: ")
            __insert_into_db(public_name, public)

            private = getpass(prompt=f"{private_display}: ")
            __insert_into_db(private_name, private)
    print()
