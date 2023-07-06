'''
 * Reto #49
 * EL DETECTOR DE HANDLES
 * Fecha publicación enunciado: 05/11/22
 * Fecha publicación resolución: 12/12/22
 * Dificultad: FÁCIL
 *
 * Enunciado: Crea una función que sea capaz de detectar y retornar todos los handles de un texto usando solamente Expresiones Regulares.
 * Debes crear una expresión regular para cada caso:
 * - Handle usuario: Los que comienzan por "@"
 * - Handle hashtag: Los que comienzan por "#"
 * - Handle web: Los que comienzan por "www.", "http://", "https://" y finalizan con un dominio (.com, .es...)
'''

import re

def detect_handles (text):
    handles_user = list
    handles_hastag = list
    handles_web = list

    handles_user = re.findall("@\w+", text)
    handles_hastag = re.findall("#\w+", text)
    handles_web = re.findall("https?:\/\/[w]{3}\.[a-z]+\.[a-z]+|https?:\/\/[a-z]+\.[a-z]+|[w]{3}\.[a-z]+\.[a-z]+", text)
    
    print("Handles usuario:")
    print(handles_user)
    print("Handles hastag:")
    print(handles_hastag)
    print("Handles web:")
    print(handles_web)

text = input("Escribe el texto a analizar:\n")
detect_handles(text)