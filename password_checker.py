import requests
import hashlib
import sys


def resquest_data(query_data):
    '''
    Takes data from the API provided by https://haveibeenpwned.com/
        The query_data is a Hash code of 5 characters
        returns the resoponse with all the data realated to the query_data
        '''
    api_url = 'https://api.pwnedpasswords.com/range/' + query_data
    res = requests.get(api_url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API')
    return res

def get_pass_leaks(hashes, hash_to_check):
    '''
    Takes two arguments: hashes what is the main part of the entire has code and hash_to_check
    that reamins in the computer, this allows to not sent the entire password to the API and compare it's
    existance locally
    Funcionallity: Slipts each linea of the response given by request_data and returns how many times that password
    has been found on any data leak
    '''
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


def main():
    '''reads the password file and then checks if there is or not a match, if the count is more than 0
        it recommends to change the password.
    '''
    with open('password.txt', 'r') as password_file:
        password = password_file.read()
        count = pass_check(password)
        if count:
            print(f'The password {password} was found {count} times, it\'s highly recommended to change your password')
        else:
            print(f'the password {password} was NOT found, you have a solid one!')
        return 'done!'

if __name__ == '__main__':
    sys.exit(main())

