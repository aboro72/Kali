#!/usr/bin/python3

import sys, hashlib, time

ts = time.time()
if len(sys.argv) != 3:
    print("USAGE: ")
    print("./" + sys.argv[0], " [HASHFILE] [WORDLIST] \n")
    sys.exit()

hashes = set()
with open(sys.argv[1], "r") as hashfile:
    for line in hashfile:
        hashes.add(line.strip())

print("Start cracking .......")
with open(sys.argv[2], "r") as wordlist:
    for line in wordlist:
        line = line.strip('\n')
        md5_hash = hashlib.md5(line.encode()).hexdigest()
        if md5_hash in hashes:
            print(md5_hash + " == " + line)

td = time.time() - ts
print("Erledigt in " + str(td) + " Sekunden")
