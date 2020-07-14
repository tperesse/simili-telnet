#!/usr/bin/python3
# coding: utf8

# import os

# counter = [1, 2]
# # while True:



# def get_creds(useranme):
#     with open('creds.txt') as f:
#         for x in f:
#             credential = x.strip().split(' ', 1)
#             user, passwd = credential[0], credential[1]
#             if user == msg:
#                 return user, passwd
#             continue

# username, password = get_creds(msg)
# print(username, password)

    # def check_username(username, counter):
    #     if username == "none" or len(counter) > 3:
    #         if len(counter) != 0:
    #             del counter[0]
    #         else:
    #             os._exit(1)
    #         print("BYE")
    #     else:
    #         if msg == username:
    #             print("WELC")

# def check_username(username, counter):
#     # Si le mdp est égale à rien.
#     if len(counter) > 0:
#         if username == "none":
#             # Si la liste n'est pas vide on retire un. 
#             del counter[0]
#             return "BYE"
#         else:
#             if msg == username:
#                 return "WELC"
#             else:
#                 del counter[0]
#                 return "BYE"
#     else:
#         return "BYE"

# def check_password(password, counter):
#     # Si le mdp est égale à rien.
#     if len(counter) > 0:
#         if password == "none":
#             # Si la liste n'est pas vide on retire un. 
#             del counter[0]
#             return "BYE"
#         else:
#             if msg_2 == password:
#                 return "WELC"
#                 os._exit(1)
#             else:
#                 del counter[0]
#                 return "BYE"
#     else:
#         return "BYE"

# def get_creds(useranme):
#     with open('creds.txt') as f:
#         for x in f:
#             credential = x.strip().split(' ', 1)
#             user, passwd = credential[0], credential[1]
#             if user == useranme:
#                 return user, passwd
#             continue

# username, password = get_creds(msg)

# def check_creds(username, password, reponse):
#     if password == "none" or username == "none":
#         return "BYE"
#     else:
#         if username in reponse:
#             if password in reponse:
#                 return "WELC"
#             else:
#                 return "BYE"
#         else:
#             return "BYE" 

# for _ in range(3):
#     username = input("user: ")
#     password = input("password: ")
#     compare = ['theo', '123']
#     lol = check_creds(username, password, compare)
#     if lol == "WELC":
#         print("WELC")
#         break
#     print("BYE")


# def socket_serveur(sock):
#     try:
#         sock.bind(('127.0.0.1', 15000))
#         sock.listen(1)
#         print("En attente de client")
#     except socket.error as msg:
#             print("Erreur :",msg)
#             sys.exit()

# def connexion_client():
#     connexion, adresse = sock.accept()
#     print("Le client avec le socket "+str(adresse[1])+" est connecté")
#     msg_bonj = connexion.recv(1024)
#     print(msg_bonj.decode())
#     ask_passd(connexion)
#     # while True:
#     #     message = connexion.recv(1024).decode()
#     #     print('\n'+ message)


# def get_creds(username):
#     with open('creds.txt') as f:
#         for x in f:
#             credential = x.strip().split(' ', 1)
#             user, passwd = credential[0], credential[1]
#             if user == username:
#                 return user, passwd
#             continue

# def check_creds(username, password, reponse):
#     if password == "None" or username == "None" or reponse == "None":
#         return "BYE"
#     else:
#         try:
#             if username in reponse:
#                 if password in reponse:
#                     return "WELC"
#                 else:
#                     return "BYE"
#             else:
#                 return "BYE" 
#         except TypeError:
#             return "BYE"

# def ask_passd(connfd):
# # On demande son username et on cherche ses infos d'authent dans le fichier.
#     msg_who = "WHO"
#     msg_who = msg_who.encode()
#     connfd.send(msg_who)
#     for _ in range(3):
#         asw_who = connfd.recv(1024).decode()
#         user_passwd = get_creds(asw_who)
#         # On demande son password.
#         msg_passwd = "PASSWD"
#         msg_passwd = msg_passwd.encode()
#         connfd.send(msg_passwd)
#         asw_passwd = connfd.recv(1024).decode()
#         # On compare ce que le client a envoyé avec les creds du fichier.
#         compare_creds = check_creds(asw_who, asw_passwd, user_passwd)
#         if compare_creds == "WELC":
#             msg_welc = "WELC"
#             msg_welc = msg_welc.encode()
#             connfd.send(msg_welc)
#             break
#         # Envoie du message "BYE".
#         msg_bye = "BYE"
#         msg_bye = msg_bye.encode()
#         connfd.send(msg_bye)

# if __name__ == "__main__": 
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     socket_serveur(sock)
#     connexion_client()

# def msg_who(connfd):
#     msg_who = "WHO"
#     msg_who = msg_who.encode()
#     connfd.send(msg_who)

# def msg_passwd(connfd):
#     msg_passwd = "PASSWD"
#     msg_passwd = msg_passwd.encode()
#     connfd.send(msg_passwd)

# rls = os.popen("/bin/ls").read().strip("\n")
# fd = os.open("test.txt", os.O_RDWR)
# line = str.encode(rls)
# os.write(fd, line)

# file1 = open('test.txt', 'r') 
# Lines = file1.readlines()
# for line in Lines:
#     print(line.strip("\n"))

# # Open a file
# fd = os.open( "test.txt", os.O_RDWR|os.O_CREAT )

# Write one string using duplicate fd
# while True:
#     os.execlp("/bin/ls", 'ls')



# def lol():
#     try:
#         fd=os.open("test.txt",os.O_WRONLY | os.O_CREAT)
#         os.dup2(fd, pty.STDOUT_FILENO)
#         os.execlp("/bin/ls", 'ls')
#         lol()
#     except OSError:
#         print("erreur d'ouverture de test_dup2")
#         sys.exit(-1)

# def lol2():
#     while True:
#         print('olo')
#         lol()
#         print('lol')

# lol2()


# =============SERVEUR======================
# def comm_to_server(sock):
#     msg_bonj = "BONJ"
#     msg_bonj = msg_bonj.encode()
#     sock.send(msg_bonj)
#     while True:
#         recu = sock.recv(1024).decode()
#         print(recu, end='\n')
#         msg = input('')
#         msg = msg.encode()
#         sock.send(msg)

# if __name__ == "__main__":
#     # Création du socket.
#     sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#     sock.connect(('127.0.0.1', 15000))
#     # La source de données est un fichier.
#     comm_to_server(sock)
# =========================================

#===============CLIENT==================
# def client(end_data, connectes, sockfd):
#     """Fonction permettant de simuler un client."""
#     # Envoie "BONJ" au serveur.
#     msg_bonj = "BONJ"
#     msg_bonj = msg_bonj.encode()
#     sockfd.send(msg_bonj)
#     compteur = []
#     while True:
#         # On récupère ce que le serveur envoie et on l'affiche.
#         msg = sockfd.recv(4096).decode()
#         print(msg)
#         # Si le message est un "BYE" et qu'il est envoyé 3 fois, on ferme la connexion au serveur.
#         if msg == "BYE":
#             compteur.append(msg)
#             if len(compteur) == 3:
#                 print("Deconnexion du serveur")
#                 sys.exit(-1)
#         # On se met en attente d'un evenement en lecture sur la socket ou l'entrée de données 
#         # on recupere dans a_lire le(s) descripteur(s) prêts à lire.
#         a_lire, [], [] = select.select(connectes,[],[])
#         for desc in a_lire:
#             # On surveille que le serveur est toujours dispo.
#             if desc == sockfd:
#                 # recu = sockfd.recv(1024).decode()
#                 # print(recu)
#                 # if len(recu) != 0:
#                 #     print("3")
#                 #     print(recu)
#                 # else:
#                 if end_data == 1:
#                     print("Deconnexion du serveur")
#                     sys.exit(-1)
#                     # else:
#                     #     sys.exit(0)

#             # On lit le "stdin" et on envoie au serveur
#             if desc == fd:
#                 lu = os.read(fd, 1024).decode().strip('\n').encode()
#                 if len(lu) == 0:
#                     sockfd.shutdown(socket.SHUT_WR)
#                     end_data = 1
#                     connectes = [sockfd]
#                 else:
#                     sockfd.send(lu)
# =========================================

# def rls():
#     rls = os.popen("/bin/ls").read().strip("\n")
#     fd = os.open("test.txt", os.O_RDWR)
#     line = str.encode(rls)
#     os.write(fd, line)

#     file1 = open('test.txt', 'r') 
#     Lines = file1.readlines()
#     for line in Lines:
#         connfd.send(line.encode())

# def commands(command):
#     com = []
#     com.append(command)
#     while command != None:
#         if command == "rls":
#             rls()

import os
import sys
import socket
import signal
import pty
import time

def rls(path):
    try:
        fd = os.open("rls.txt", os.O_WRONLY)
        os.ftruncate(fd, 0)
        os.dup2(fd, pty.STDOUT_FILENO)
        os.execlp("/bin/ls", 'ls', path)
        sys.exit(0)
    except OSError:
        print("erreur d'ouverture de test_dup2")
        sys.exit(-1)

def rpwd():
    try:
        fd = os.open("rpwd.txt", os.O_WRONLY)
        os.ftruncate(fd, 0)
        os.dup2(fd, pty.STDOUT_FILENO)
        os.execlp("/bin/pwd", 'pwd')
        sys.exit(0)
    except OSError:
        print("erreur d'ouverture de test_dup2")
        sys.exit(-1)

def rcd(path):
    try:
        fd = os.open("rcd.txt", os.O_WRONLY)
        os.ftruncate(fd, 0)
        os.dup2(fd, pty.STDOUT_FILENO)
        os.chdir(path)
        os.execlp("/bin/pwd", 'pwd')
        sys.exit(0)
    except:
        print("Chemin non valide")
        sys.exit(-1)

def read(file):
    file = open(file, 'r') 
    lines = file.readlines()
    for line in lines:
        print(line.strip("\n"))
    # content = []
    # f = open(file, "r")
    # for x in f:
    #     content.append(x.strip("\n"))
    # return content

def commands(command, path):
    child = os.fork()
    if command == "rcd" and child == 0:
        rcd(path)
    elif command == "rls" and child == 0:
        rls(path)
    elif command == "rpwd" and child == 0:
        rpwd()

path = input("> ")
commands("rpwd", path)
time.sleep(3)
# commands("rls", path)
# time.sleep(3)
read("rpwd.txt")
# result = []
# for l in lol:
#     result.append(l)
# print(result)

comm = input("command > ")
if comm == "rls" or comm == "rcd":
    path = input("path > ")
    if comm == "rls":
        execute_commands("rcd", path)
        time.sleep(3)
execute_commands(comm, path)
time.sleep(3)
reader = read(comm + ".txt")
