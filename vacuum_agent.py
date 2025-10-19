class Environment:
    def __init__(self):
        self.location = {"A": "dirty",
                         "B": "dirty"}
        self.vacuum_position = "A"

    def is_dirty(self):
        return self.location[self.vacuum_position] == "dirty"

    def clean(self):
        self.location[self.vacuum_position] = "clean"

    def move(self):
        if self.vacuum_position == "A":
            self.vacuum_position = "B"
        else:
            self.vacuum_position = "A"
  
class SimpleReflexAgent:
    def choose_action(self, env):
        if env.is_dirty():
            return "suck"
        else:
            return "move"
        
env = Environment()
agent = SimpleReflexAgent()

for i in range(6):
    action = agent.choose_action( env)
    
    if action == "suck":
        env.clean()
        print(f"step{i+1}: Sucked dirt at {env.vacuum_position}")
    else:
        env.move()
        print(f"step {i+1}: moved to {env.vacuum_position}")
        
    print("current Evniroment: ", env.location)
    print()                           