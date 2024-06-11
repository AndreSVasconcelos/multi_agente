# Libs
from pade.misc.utility import display_message
from pade.core.agent import Agent
from classes.comportamentos import Comportamento

class Agente(Agent):
    def __init__(self, aid):
        super(Agente, self).__init__(aid=aid)
        #display_message(self.aid.localname, "Hello World!")
        comportamento = Comportamento(self, 2.0)
        self.behaviours.append(comportamento)