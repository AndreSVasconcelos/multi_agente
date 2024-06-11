# Libs
from pade.core.agent import Agent
from classes.comportamentos import ComportamentoTeste, ComportamentoVendedor, ComportamentoComprador, ComportamentoTemporal
from pade.acl.messages import ACLMessage
from pade.acl.aid import AID

# Classes

# Agente Vendedor
class AgenteVendedor(Agent):
    def __init__(self, aid):
        super(AgenteVendedor, self).__init__(aid=aid)
        self.comport_request = ComportamentoVendedor(self)
        self.behaviours.append(self.comport_request)

# Agente Comprador
class AgenteComprador(Agent):
    def __init__(self, aid, recebedor):
        super(AgenteComprador, self).__init__(aid=aid)
        mensagem = ACLMessage(ACLMessage.REQUEST)
        mensagem.set_protocol(ACLMessage.FIPA_REQUEST_PROTOCOL)
        mensagem.add_receiver(AID(name=recebedor))
        mensagem.set_content('produtos')
        # Comportamentos
        self.comport_request = ComportamentoComprador(self, mensagem)
        self.comport_temp = ComportamentoTemporal(self, 8.0, mensagem)
        self.behaviours.append(self.comport_request)
        self.behaviours.append(self.comport_temp)

# Agente de testes
class AgenteTeste(Agent):
    def __init__(self, aid):
        super(AgenteTeste, self).__init__(aid=aid)
        #display_message(self.aid.localname, "Hello World!")
        comportamento = ComportamentoTeste(self, 2.0)
        self.behaviours.append(comportamento)