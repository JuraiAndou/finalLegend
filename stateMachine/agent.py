from stateMachine.state import State
class Agent:
    _state = None
    
    def __init__(self, state : State) -> None:
        self.chageState(state)

    def chageState(self, Agent: State):
        print(f"Agent: Transitioning to {type(Agent).__name__}")
        self._state = Agent
        self._state.agent = self
    
    def execute(self):
        self._state.execute()