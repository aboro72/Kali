#!/usr/bin/python3
import locale
import sys
import hashlib
import time

ts = time.time()
if len(sys.argv) != 3:
    print("Usage: ")
    print("./" + sys.argv[0] + " [HASHFILE] [WORDLIST] \n")
    sys.exit()

hashes = set()
with open(sys.argv[1], "r") as hashfile:
    for line in hashfile:
        hashes.add(line.strip())

with open(sys.argv[2], "r") as wordlist:
    for word in wordlist:
        for line in hashes:
            tmp = line.split("$")
            word = word.strip('\n')
            to_hash = tmp[0] + word
            md5_hash = tmp[0] + "$" + hashlib.md5(to_hash.encode()).hexdigest()
            if md5_hash == line:
                print(md5_hash + " == " + word)

td = time.time() - ts
print("Done in " + str(td) + " sec. ")


