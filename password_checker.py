import requests
import hashlib
import sys


def resquest_data(query_data):
    api_url = 'https://api.pwnedpasswords.com/range/' + query_data
    res = requests.get(api_url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API')
    return res

def get_pass_leaks(hashes, hash_to_check):
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check:
            return count   
    return 0

def pass_check(password):
    '''
    Take the password given as input and convert it to an SHA1 hash code in UTF-8 formal
    Also make it compatible with the API setting it to upper case and reducing it to 5 char.
    '''
    sha1pass = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five, remain = sha1pass[:5], sha1pass[5:]
    response = resquest_data(first_five)
    return get_pass_leaks(response, remain)


def main(args):
    for password in args:
        count = pass_check(password)
        if count:
            print(f'The password {password} was founf {count} times, it\'s highly recommended to change your password')
        else:
            print(f'the password {password} was NOT found, you have a solid one!')
        return 'done!'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

