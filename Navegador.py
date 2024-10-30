import csv
import os
from datetime import datetime
from bs4 import BeautifulSoup

#Clase stack para implementar la estructura
class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def clear(self):
        self.items.clear()

class NodoPestania:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre de la pestaña
        self.siguiente = None  # Puntero al siguiente nodo

    def __str__(self):
        return f"NodoPestania(nombre={self.nombre})"

