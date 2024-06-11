# Libs
from sys import argv
from classes.agentes import AgenteVendedor, AgenteComprador
from pade.misc.utility import start_loop
from pade.acl.aid import AID

# Main
if __name__ == "__main__":
    qtd_agentes = 1 # 1 Comprador e 1 vendedor
    c = 0
    agentes = list()

    for i in range(qtd_agentes):
        porta = int(argv[1]) + c
        nome_agente_vendedor = 'agente_vendedor{}@localhost:{}'.format(porta, porta)
        agente_vendedor = AgenteVendedor(AID(name=nome_agente_vendedor))
        nome_agente_comprador = 'agente_comprador{}@localhost:{}'.format(porta - 10000, porta - 10000)
        agente_comprador = AgenteComprador(AID(name=nome_agente_comprador), nome_agente_vendedor)
        agentes.append(agente_vendedor)
        agentes.append(agente_comprador)
        c += 500

    start_loop(agentes)