import utils
import auth
import renderer

if __name__ == '__main__':
    # print('Running in password mode...')
    #
    # utils.acquire_and_store_pair('client_id', 'client_secret', public_display='Client ID')
    # utils.acquire_and_store_pair('username', 'password')
    #
    # print('Acquiring access token...')
    # token = auth.fetch_token()
    # print('Access token: ')
    # print(token)

    renderer.download_and_render('https://www.sec.gov/Archives/edgar/data/320193/000032019323000064/0000320193-23-000064-xbrl.zip', 'aapl-20230401.htm')
