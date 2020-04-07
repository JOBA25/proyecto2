import threading
import random

#####################Variables globales########################

#meseros, chefs, mesas, clientes
num_meseros
num_mesas
num_chefs
num_clientes

## Mutex para los meseros disponibles y fila de clientes en espera
mutex_fila_espera = threading.Semaphore(1)
mutex_meseros_disp = threading.Semaphore(1)

## Multiplex para chefs, mesa, meseros disponibles
chefs = threading.Semaphore(num_chefs)
meseros = threading.Semaphore(num_meseros)
mesas = threading.Semaphore(num_mesas)





#####################Clases######################################
class Cliente:
    def __init__(self, id_cliente, num_invitados):
        self.id_cliente = id_cliente
        self.num_invitados = num_invitados
        self.lista_invitados = []
        #usaremos una barrera para que todos elijan su platillo
        self.cuenta_orden = 0
        self.mutex_orden = threading.Semaphore(1)
        self.barrera_orden = threading.Semaphore(0)
        #usaremos una barrera para que todos terminen de comer
        self.cuenta_comer = 0
        self.mutex_comer = threading.Semaphore(1)
        self.barrera_comer = threading.Semaphore(0)

    



class invitado:


class Mesero:



class Chef:


class Restaurante: