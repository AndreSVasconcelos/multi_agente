# Libs
from pade.core.agent import Agent
from classes.comportamentos import ComportamentoTeste

class AgenteTeste(Agent):
    def __init__(self, aid):
        super(AgenteTeste, self).__init__(aid=aid)
        #display_message(self.aid.localname, "Hello World!")
        comportamento = ComportamentoTeste(self, 2.0)
        self.behaviours.append(comportamento)