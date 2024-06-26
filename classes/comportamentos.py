# Libs
from pade.behaviours.protocols import TimedBehaviour
from pade.misc.utility import display_message
from pade.behaviours.protocols import FipaRequestProtocol
from pade.acl.messages import ACLMessage

# Classes
# Comportamento para Agentes vendedores
class ComportamentoVendedor(FipaRequestProtocol):
    def __init__(self, agent):
        super(ComportamentoVendedor, self).__init__(agent=agent, message=None, is_initiator=False)
        self.produtos = 'TV 55, Notebook, Microondas'
    
    def handle_request(self, message):
        super(ComportamentoVendedor, self).handle_request(message)
        display_message(self.agent.aid.localname, "Agente " + str(self.agent.aid.localname) + " recebeu a requisição")
        resposta = message.create_reply()
        resposta.set_performative(ACLMessage.INFORM)
        resposta.set_content(self.produtos)
        self.agent.send(resposta)

# Comportamento do comprador
class ComportamentoComprador(FipaRequestProtocol):
    def __init__(self, agent, message):
        super(ComportamentoComprador, self).__init__(agent=agent, message=message, is_initiator=True)

    def handle_inform(self, message):
        display_message(self.agent.aid.localname, message.content)
    

# Comportamento Temporal
class ComportamentoTemporal(TimedBehaviour):
    def __init__(self, agent, time, message):
        super(ComportamentoTemporal, self).__init__(agent, time)
        self.message = message
    
    def on_time(self):
        super(ComportamentoTemporal, self).on_time()
        self.agent.send(self.message)    
    
   


# Comportamento de teste para agentes
class ComportamentoTeste(TimedBehaviour):
    def __init__(self, agent, tempo):
        super(ComportamentoTeste, self).__init__(agent, tempo)
        self.agent = agent

    def on_time(self):
        super(ComportamentoTeste, self).on_time()
        display_message(self.agent.aid.localname, "Olá do Agente " + str(self.agent.aid.localname))