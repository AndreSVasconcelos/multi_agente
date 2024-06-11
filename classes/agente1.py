# Libs
from pade.misc.utility import display_message
from pade.core.agent import Agent

class Agente(Agent):
    def __init__(self, aid):
        super(Agente, self).__init__(aid=aid)
        display_message(self.aid.localname, "Hello World!")