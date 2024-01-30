#!/usr/bin/python3
import os
import math

AUTH_GITHUB_TOKEN_FORMAT = "AUTH_GITHUB_TOKEN_"
AUTH_GITHUB_USERNAME_FORMAT = "AUTH_GITHUB_USERNAME"
GITHUB_APIURL = "https://api.github.com/user/repos"

""" ENDPOINTS = {
    "repo":{
        "method":"post",
        "headers":{
            "Authorization":f"token"
        }
    }
}
 """

#Obtengo desde las variaboles de entorno
#las configuraciones de cuenta guardadas
def getCurrentAccountConfigurations():
    return

#Añado una nueva configuración de cuenta a las
#Variables de entorno
def addAnAccountConfiguration():
    return

print(getCurrentAccountConfigurations())