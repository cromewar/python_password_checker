import requests
import hashlib


def resquest_data(query_data):
    api_url = 'https://api.pwnedpasswords.com/range/' + query_data
    res = requests.get(api_url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API')
    return res

def pass_check(password):
    '''
    Take the password given as input and convert it to an SHA1 hash code in UTF-8 formal
    Also make it compatible with the API setting it to upper case and reducing it to 5 char.
    '''
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five, remain = sha1pass[:5], sha1pass[5:]
    response = resquest_data(first_five)
    print(response)
    return response


pass_check('laconcha')