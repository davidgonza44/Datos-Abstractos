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

# Clase Nodo para la lista doblemente enlazada de pestañas
class NodoPestania:
    def __init__(self, pestania):
        self.pestania = pestania
        self.prev = None
        self.next = None

# Clase Cola para implementar la estructura de datos cola
class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Clase Pagina que representa una página web
class Pagina:
    def __init__(self, url, contenido, fecha, hora):
        self.url = url
        self.contenido = contenido
        self.fecha = fecha
        self.hora = hora

