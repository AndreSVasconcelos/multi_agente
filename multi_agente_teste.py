# Libs
from classes.agentes import AgenteTeste
from sys import argv
from pade.acl.aid import AID
from pade.misc.utility import start_loop

# Main
""" if __name__ == "__main__":
    qtd_agentes = 2
    c = 0
    agentes = list()

    for i in range(qtd_agentes):
        porta = int(argv[1]) + c
        nome_agente = 'agemte{}@localhost:{}'.format(porta, porta)
        agente = AgenteTeste(AID(name=nome_agente))
        agentes.append(agente)
        c += 1000

    start_loop(agentes) """