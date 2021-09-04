#!/usr/bin/env python
# -*- coding: utf-8 -*-
from os import system
from os.path import dirname, realpath, join
from utils.lib_test import JsonManager
from getpass import getpass
import stdiomask, time
from passlib.hash import pbkdf2_sha256


class LoginJson(JsonManager):
    def __init__(self):
        self.path = dirname(realpath(__file__)) + '/'
        self.dataPath = join(self.path, 'data/data.json')
    
    def cadastro(self):
        print('\x1b[1;32;40m/// * Cadastre-se * \\\\\ \x1b[1;0;40m \n')
        username = input("\x1b[1;96;40mDigite o nome de usuário abaixo:\n")
        password = stdiomask.getpass("Digite sua senha abaixo:\n")
        verify = stdiomask.getpass("Digite novamente sua senha abaixo para confirma-la:\n")
        print("\x1b[1;0;40m")
        while password != verify:
            print("Senhas não correspondem")
            password = stdiomask.getpass("\x1b[1;96;40mDigite sua senha abaixo:\n")
            verify = stdiomask.getpass("Digite novamente sua senha abaixo para confirma-la:\n")
            print("\x1b[1;0;40m")
        passwithhash = pbkdf2_sha256.hash(verify)
        JsonManager().create_json(self.dataPath, username, passwithhash)
        print("Registro finalizado")
        time.sleep(3)
        system('cls')

    def login(self):
        pass
    
    def main(self):
        self.Cadastro()


if __name__ == '__main__':
    login = LoginJson()
    login.main()