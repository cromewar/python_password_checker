# Password vulnerability checker using python

## Description
This script uses the APi from have I been pwned website by Troy Hunt, using it's passwords list to check if the password given on **password.txt** has been hacked or not.

### The official site:


https://haveibeenpwned.com/ - Official Site!
[Passwords](https://haveibeenpwned.com/Passwords)

## Functionallity 
The script transforms the password on **password.txt** to SHA1 encription format, but it does not send it entirely to the API server, instead this is how it works:

  1) Separates the SHA1 code in to parts, one of 5 character and the second one with the rest of the code.
  2) Sends just the first 5 characters part to the server, so no one interfering with your network traffic will be able to see the complete password (SHA1 code).
  3) uses the response of the API server and adds the remainig part of the code that exists just locally on your system.
  4) if it founds any match, it means that your password has been hacked, if not, you are safe to continue using it.

## Usage
Just open the **password.txt** file and put there the password you want to verify, then run the script using your command prompt like this.

```python
python password_checker.py
```

## Final Note:

This script was possible thanks to ZTM academy and it's Python course by **Andrei Neagoie**
