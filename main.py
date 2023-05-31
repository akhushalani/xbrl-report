from getpass import getpass
import utils

if __name__ == '__main__':
    credentials = utils.check_credentials()
    if credentials:
        print('Credentials found!')
        print(f"Client ID: {credentials['client_id']}\nClient secret: {credentials['client_secret']}")
    else:
        print('Credentials not found.')

        client_id = input("Client ID: ")
        utils.insert_into_db('client_id', client_id)

        client_secret = getpass(prompt='Client secret: ')
        utils.insert_into_db('client_secret', client_secret)
