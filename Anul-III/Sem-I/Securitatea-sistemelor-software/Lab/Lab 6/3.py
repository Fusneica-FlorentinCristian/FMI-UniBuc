import string
import secrets
from random import randint, shuffle, getrandbits
import os
import base64

def createPassword():
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    specials = '.!$@'
    alphabet = lowercase + uppercase + digits + specials

    passSize = randint(10, 15)

    # minimal requirements
    password = [secrets.choice(uppercase), secrets.choice(digits), secrets.choice(specials), secrets.choice(lowercase)]

    password.extend([secrets.choice(alphabet) for i in range(passSize - 4)])
    shuffle(password)
    password = ''.join(password)

    return password

def getRandomBites():
    bytes = str(bytearray(getrandbits(8) for _ in range(8)))
    bytes_as_bits = ''.join(format(ord(byte), 'b') for byte in bytes)
    # this would be my salt, one time only
    return bytes_as_bits

def xorProcess(s1, s2):
    return ''.join(['0' if int(a) ^ int(b) == 0 else '1' for a,b in zip(s1, s2)])

def addPadding(stringToPad, sizeString):
    return stringToPad + ''.join(['0' for _ in range(sizeString - len(stringToPad))])

if __name__ == '__main__':


    # one time only
    masterKey = createPassword()
    print(masterKey)

    # one time only
    salt = getRandomBites()

    print('https://mydomain.com/safeurl=' + secrets.token_urlsafe(32))
    print('hex token: ' + secrets.token_hex(64))

    print(secrets.compare_digest(masterKey, masterKey))

    userPassword = createPassword()
    userPassword = ''.join(format(ord(x), 'b') for x in userPassword)
    masterKey = ''.join(format(ord(x), 'b') for x in masterKey)[0:len(userPassword)]
    masterKey = addPadding(masterKey, len(userPassword))

    #one time only
    salt = salt[0:len(userPassword)]
    salt = addPadding(salt, len(userPassword))

    print('Master key: ', masterKey)
    print('User key:   ', userPassword)
    print('Salt:       ',salt)

    result = xorProcess(userPassword, salt)
    result = xorProcess(result, masterKey)

    print('Result:     ', result)
