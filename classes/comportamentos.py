# Libs
from pade.behaviours.protocols import TimedBehaviour
from pade.misc.utility import display_message
from pade.behaviours.protocols import FipaRequestProtocol

# Classes
# Comportamento para Agentes vendedores
class ComportamentoVendedor(FipaRequestProtocol):
    def __init__(self, agent):
        super(ComportamentoVendedor, self).__init__(agent=agent,
                                                    message=None,
                                                    is_initiator=False)
        self.produtos = 'TV 55, Notebook, Microondas'
    
    def handle_request(self, message):
        super(ComportamentoVendedor, self).handle_request(message)
        display_message(self.agent.aid.localname, "Agente " + str(self.agent.aid.localname) + " recebeu a requisição")

# Comportamento de teste para agentes
class ComportamentoTeste(TimedBehaviour):
    def __init__(self, agent, tempo):
        super(ComportamentoTeste, self).__init__(agent, tempo)
        self.agent = agent

    def on_time(self):
        super(ComportamentoTeste, self).on_time()
        display_message(self.agent.aid.localname, "Olá do Agente " + str(self.agent.aid.localname))