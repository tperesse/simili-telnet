#!/usr/bin/python3

"""
Ce script a pour but de simuler un serveur pour le projet simili-telnet.
Fait par :
- Théo PERESSE
- Alexandre KOSTAS
- Jean-Alexandre PIOT
- Philippe DA SILVA OLIVEIRA
"""

import os
import sys
import socket
import select
import pty
import time

def ls(path):
    """Fonction permettant de lister le contenu du dossier qui nous est donné en paramètre."""
    try:
        fd = os.open("ls.txt", os.O_WRONLY | os.O_CREAT)
        os.ftruncate(fd, 0)
        os.dup2(fd, pty.STDOUT_FILENO)
        os.execlp("/bin/ls", 'ls', path)
        sys.exit(0)
    except OSError:
        print("erreur d'ouverture du fichier ls.txt")
        sys.exit(-1)

def cd(path):
    """Fonction permettant de changer de dossier."""
    fd = os.open("cd.txt", os.O_WRONLY | os.O_CREAT)
    os.ftruncate(fd, 0)
    os.dup2(fd, pty.STDOUT_FILENO)
    os.chdir(path)
    os.execlp("/bin/pwd", 'pwd')
    sys.exit(0)

def pwd():
    """Fonction permettant de changer de dossier."""
    try:
        fd = os.open("pwd.txt", os.O_WRONLY | os.O_CREAT)
        os.ftruncate(fd, 0)
        os.dup2(fd, pty.STDOUT_FILENO)
        os.execlp("/bin/pwd", 'pwd')
        sys.exit(0)
    except OSError:
        print("erreur d'ouverture du fichier ls.txt")
        sys.exit(-1)

def read(file):
    """Fonction permettant de lire et d'envoyer"""
    resultat = []
    file = open(file, 'r')
    lines = file.readlines()
    for line in lines:
        print(line.strip("\n"))
        resultat.append(line.strip("\n"))
    return resultat

def execute_commands(comm, path):
    """Cette fonction permet d'exécuter dans un processus fils la commande passée en paramètre."""
    child = os.fork()
    if comm == "cd" and child == 0:
        cd(path)
    elif comm == "ls" and child == 0:
        ls(path)
    elif comm == "pwd" and child == 0:
        pwd()

def commands(lu):
    """Cette fonction va exécuter le scénario d'utilisation
    des commandes 'ls', 'pwd' et 'cd'."""
    try:
        if lu == "cd":
            if len(path) != 0:
                del path[0]
            chemin = input("path > ")
            path.append(chemin)
            try:
                execute_commands(lu, path[0])
                time.sleep(3)
                print("CDOK")
            except:
                print("NOCD")
        elif lu == "ls":
            if len(path) == 0:
                execute_commands("pwd", " ")
                time.sleep(3)
                pth = read("pwd.txt")
                path.append(pth[0])
                execute_commands(lu, pth[0])
                time.sleep(3)
                read("ls.txt")
            else:
                execute_commands(lu, path[0])
                time.sleep(3)
                read("ls.txt")
        elif lu == "pwd":
            if len(path) == 0:
                execute_commands("pwd", "")
                time.sleep(3)
                pth = read("pwd.txt")
                path.append(pth[0])
            else:
                print(path[0])
    except:
        return 0

def client(end_data, connectes, sockfd):
    """Fonction permettant de simuler un client."""
    msg_bonj = "BONJ"
    msg_bonj = msg_bonj.encode()
    sockfd.send(msg_bonj)
    while True:
        msg = sockfd.recv(4096).decode()
        print(msg)
        if msg == "BYE":
            print("Deconnexion du serveur")
            sys.exit(-1)
        a_lire, [], [] = select.select(connectes, [], [])
        for desc in a_lire:
            if desc == sockfd:
                if end_data == 1:
                    print("Deconnexion du serveur")
                    sys.exit(-1)

            if desc == fd:
                lu = os.read(fd, 1024).decode().strip('\n').encode()
                if len(lu) == 0:
                    sockfd.shutdown(socket.SHUT_WR)
                    end_data = 1
                    connectes = [sockfd]
                else:
                    comm = lu.decode()
                    if comm == "cd" or comm == "ls" or comm == "pwd":
                        return 0
                    else:
                        sockfd.send(lu)

if __name__ == "__main__":
    """Cette partie correspond au main du programme."""
    if sys.argv[3] != "stdin":
        fd = os.open(sys.argv[3], os.O_RDONLY)
    else:
        fd = sys.stdin.fileno()

    connectes = [fd]
    end_data = 0
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sockfd.connect((sys.argv[1], int(sys.argv[2])))
    connectes.append(sockfd)
    client(end_data, connectes, sockfd)
    path = []
    while True:
        lu = input("> ")
        commands(lu)   
