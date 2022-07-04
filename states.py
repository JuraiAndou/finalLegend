from stateMachine import State
class grdState:
    pass

class AtkState(State):
    def execute(self) -> None:
        print(f"Agent: {type(self.agent).__name__} is attacking!")
        print(f"Agent: {type(self.agent).__name__} is changing state...")
        self.agent.chageState(GrdState())

class GrdState(State):
    def execute(self) -> None:
        print(f"Agent: {type(self.agent).__name__} is guarding!")
        print(f"Agent: {type(self.agent).__name__} is changing state...")
        self.agent.chageState(AtkState())