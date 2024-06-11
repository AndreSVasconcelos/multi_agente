# Libs
from pade.behaviours.protocols import TimedBehaviour
from pade.misc.utility import display_message

class Comportamento(TimedBehaviour):
    def __init__(self, agent, tempo):
        super(Comportamento, self).__init__(agent, tempo)
        self.agent = agent

    def on_time(self):
        super(Comportamento, self).on_time()
        display_message(self.agent.aid.localname, "Olá do Agente " + str(self.agent.aid.localname))

    def on_end(self):
        pass