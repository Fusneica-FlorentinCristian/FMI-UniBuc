import string
import secrets

if __name__ == '__main__':
    alphabet = string.ascii_letters + string.digits + '.!$@'
    while True:
        password = ''.join(secrets.choice(alphabet) for i in range(10))
        if (any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and any(c.isdigit() for c in password)
                and any((c in '.!$@') for c in password)):
            break

print(password)


print('https://mydomain.com/safeurl=' + secrets.token_urlsafe(32))
print('hex token: ' + secrets.token_hex(64))
print(secrets.compare_digest(password, password))
