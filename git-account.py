#!/usr/bin/python3
import argparse
from itertools import count 

AUTH_GITHUB_TOKEN_FORMAT = "AUTH_GITHUB_TOKEN"
AUTH_GITHUB_USERNAME_FORMAT = "AUTH_GITHUB_USERNAME"
GITHUB_APIURL = "https://api.github.com/user/repos"
ACCOUNT_IDENTIFIER_NAME = "Account-"

def getEnvsByFormat(eviromentVarsDict:dict,format:str):
    return {"".join([ACCOUNT_IDENTIFIER_NAME,str(index)]):{
            format:value
            } for (key,value),index in zip(eviromentVarsDict.items(),count(1)) if key.startswith(format)}

#Obtengo desde las variaboles de entorno
#las configuraciones de cuenta guardadas
def getCurrentAccountConfigurations():
    return

#Añado una nueva configuración de cuenta a las
#Variables de entorno
def addAnAccountConfiguration():
    return

def defShowCommand(subParser):
    showReposCommands = subParser.add_parser("show",help="Mostrar información de los tokens de cuentas registrados.")
    showReposCommands.add_argument("-t",help="Muestra las cuentas con sus respectivos tokens.")

def commandHandler():
    parser = argparse.ArgumentParser(description="Interfaz de comandos...")
    subParser = parser.add_subparsers(title="Commandos",dest="command")

    defShowCommand(subParser)

    args = parser.parse_args()

    if hasattr(args,"command"):
        if args.command == "show":
            print(args.t)
    else:
        print("Sin comandos")


def app():
    commandHandler()

if __name__  == "__name__":
    app()