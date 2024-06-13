import hashlib
import itertools
import string
import os

os.system('@echo off')
os.system('cls' if os.name=='nt' else 'clear')

def crack_sha1_hash(target_hash, charset=string.ascii_lowercase + string.digits, max_length=12):
    for length in range(1, max_length + 1):
        for attempt in itertools.product(charset, repeat=length):
            attempt_string = ''.join(attempt)
            attempt_hash = hashlib.sha1(attempt_string.encode('utf-8')).hexdigest()
            print(f"Trying: {attempt_string} -> {attempt_hash} | MADE BY @hush1337")
            if attempt_hash == target_hash:
                return attempt_string
    return None

target_hash = input("Enter the SHA1 HASH you want to Bruteforce : ")

result = crack_sha1_hash(target_hash)

if result:
    print(f"The original string is: {result}")
else:
    print("The original string was not found within the given parameters.")
