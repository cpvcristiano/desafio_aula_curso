from collections import namedtuple
from tkinter import N

n_t = namedtuple('Cliente',['Nome', 'Plano' ,'CPF','ID'])

cliente = n_t('Ronaldo','AZUL',10600985957,95)
print(f'NOME: {cliente[0]}\nPLANO : {cliente[1]}\nNÙMERO DO CPF: {cliente[2]}\nID: {cliente[3]}')
