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
import signal
import pty
import time

def rls(path):
    """Fonction permettant de lister le contenu du dossier qui nous est donné en paramètre."""
    try:
        fd = os.open("rls.txt", os.O_WRONLY | os.O_CREAT)
        os.ftruncate(fd, 0)
        os.dup2(fd, pty.STDOUT_FILENO)
        os.execlp("/bin/ls", 'ls', path)
        sys.exit(0)
    except OSError:
        print("erreur d'ouverture du fichier rls.txt")
        sys.exit(-1)

def rcd(path):
    """Fonction permettant de changer de dossier."""
    fd = os.open("rcd.txt", os.O_WRONLY | os.O_CREAT)
    os.ftruncate(fd, 0)
    os.dup2(fd, pty.STDOUT_FILENO)
    os.chdir(path)
    os.execlp("/bin/pwd", 'pwd')
    sys.exit(0)

def rpwd():
    """Fonction permettant de changer de dossier."""
    try:
        fd = os.open("rpwd.txt", os.O_WRONLY | os.O_CREAT)
        os.ftruncate(fd, 0)
        os.dup2(fd, pty.STDOUT_FILENO)
        os.execlp("/bin/pwd", 'pwd')
        sys.exit(0)
    except OSError:
        print("erreur d'ouverture du fichier rpwd.txt")
        sys.exit(-1)

def read(file, connfd):
    """Fonction permettant de lire et d'envoyer"""
    resultat = []
    file = open(file, 'r')
    lines = file.readlines()
    for line in lines:
        connfd.send(line.encode())
        resultat.append(line.strip("\n"))
    return resultat

def execute_commands(comm, path):
    """Cette fonction permet d'exécuter dans un processus fils la commande passée en paramètre."""
    child = os.fork()
    if comm == "rcd" and child == 0:
        rcd(path)
    elif comm == "rls" and child == 0:
        rls(path)
    elif comm == "rpwd" and child == 0:
        rpwd()

def commands(connfd):
    """Cette fonction va exécuter le scénario d'utilisation des commandes 'rls', 'rpwd' et 'rcd'."""
    path = []
    try:
        while True:
            comm = connfd.recv(1024).decode().strip('\n')
            if comm == "rcd":
                if len(path) != 0:
                    del path[0]
                msg_path = "PATH"
                msg_path = msg_path.encode()
                connfd.send(msg_path)
                chemin = connfd.recv(1024)
                path.append(chemin)
                try:
                    execute_commands(comm, path[0])
                    time.sleep(3)
                    reponse = "CDOK"
                    connfd.send(reponse.encode())
                except:
                    reponse = "NOCD"
                    connfd.send(reponse.encode())
            elif comm == "rls":
                if len(path) == 0:
                    execute_commands("rpwd", " ")
                    time.sleep(3)
                    pth = read("rpwd.txt", connfd)
                    path.append(pth[0])
                    execute_commands(comm, path[0])
                    time.sleep(3)
                    read("rls.txt", connfd)
                else:
                    execute_commands(comm, path[0])
                    time.sleep(3)
                    reader = read(comm + ".txt", connfd)
            elif comm == "rpwd":
                if len(path) == 0:
                    execute_commands("rpwd", "")
                    time.sleep(3)
                    pth = read("rpwd.txt", connfd)
                    path.append(pth[0])
                else:
                    pth = read("rcd.txt", connfd)
                    connfd.send(pth[0].encode())
    except:
        return 0

def get_creds(reponse):
    """Cette fonction va permettre de récupérer les credentials de l'utilisateur
    depuis le fichier de creds."""
    with open('creds.txt') as f:
        for x in f:
            credential = x.strip().split(' ', 1)
            user, passwd = credential[0], credential[1]
            if user == reponse:
                return passwd
            continue

def check_creds(password, reponse):
    """Fonction qui va retourner 'WELC' ou 'BYE' si les mots de passe sont égaux."""
    if password == "None" or reponse == "None":
        return "BYE"
    else:
        try:
            if password == reponse:
                return "WELC"
            else:
                return "BYE"
        except TypeError:
            return "BYE"

def ask_passd(connfd):
    """Fonction qui va jouer le scnério de l'authentification."""
    for _ in range(3):
        msg_who = "WHO"
        msg_who = msg_who.encode()
        connfd.send(msg_who)
        asw_who = connfd.recv(1024).decode()

        user_passwd = get_creds(asw_who)

        msg_passwd = "PASSWD"
        msg_passwd = msg_passwd.encode()
        connfd.send(msg_passwd)
        asw_passwd = connfd.recv(1024).decode()

        compare_creds = check_creds(asw_passwd, user_passwd)

        if compare_creds == "WELC":
            msg_welc = "WELC"
            msg_welc = msg_welc.encode()
            connfd.send(msg_welc)
            return 0

    msg_bye = "BYE"
    msg_bye = msg_bye.encode()
    connfd.send(msg_bye)
    return "BYE"

def serveur_fils(connfd):
    """Fonction qui est lancée comme processus fils et qui va jouer le rôle de serveur."""
    sockfd.close()
    msg_bonj = connfd.recv(1024)
    print(msg_bonj.decode())
    ask_passd(connfd)
    commands(connfd)
    while True:
        recu = connfd.recv(1024)
        if len(recu) == 0:
            print("Deconnexion de", client)
            connfd.close()
            sys.exit(0)

if __name__ == "__main__":
    """Cette partie correspond au main du programme."""
    if len(sys.argv) != 2:
        print("Usage : ", sys.argv[0], "n°_port")
        sys.exit()

    signal.signal(signal.SIGCHLD, signal.SIG_IGN)
    sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sockfd.bind(('', int(sys.argv[1])))
    except socket.error as msg:
        print("Erreur :", msg)
        sys.exit()

    sockfd.listen(10)
    print("Attente d'un client")
    while True:
        connfd, client = sockfd.accept()
        print("Connexion de", client)
        child = os.fork()
        if child == 0:
            serveur_fils(connfd)
        else:
            connfd.close()
