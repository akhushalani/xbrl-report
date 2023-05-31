import utils

if __name__ == '__main__':
    print('Running in password mode...')

    utils.acquire_and_store_pair('client_id', 'client_secret', public_display='Client ID')
    utils.acquire_and_store_pair('username', 'password')