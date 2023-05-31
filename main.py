import utils
import auth

if __name__ == '__main__':
    print('Running in password mode...')

    utils.acquire_and_store_pair('client_id', 'client_secret', public_display='Client ID')
    utils.acquire_and_store_pair('username', 'password')

    print('Acquiring access token...')
    token = auth.fetch_token()
    print('Access token: ')
    print(token)

