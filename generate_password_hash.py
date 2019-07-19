import binascii
import hashlib
import os

from sys import version_info
if version_info.major == 2:
  input = raw_input

algorithm = input('Algorithm (sha512): ') or 'sha512'
salt = input('Salt: ') or ''
rounds = input('Rounds (100000): ') or 100000

os.system('stty -echo')
password = input('Password: ')
os.system('stty echo')
print("")

hash = hashlib.pbkdf2_hmac(algorithm, password.encode('utf-8'), salt.encode('ascii'), rounds)
print(binascii.hexlify(hash).decode('ascii'))
