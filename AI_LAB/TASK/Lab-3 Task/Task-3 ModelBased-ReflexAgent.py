class ModelBasedreflexAgent:
    def __init__(self, threshold=25):
        self.threshold = threshold
        self.previous_action = None

    def perceive_temperature(self, temperature):
        if temperature < self.threshold and self.previous_action != "ON":
            self.previous_action = "ON"
            return "Turning Heater ON"
        elif temperature >= self.threshold and self.previous_action != "OFF":
            self.previous_action = "OFF"
            return "Turning Heater OFF"
        else:
            return f"Heater remains {self.previous_action}"

agent = ModelBasedreflexAgent(threshold=22)
temperatures = [20,21,11,18,19,23]

for temp in temperatures:
    print(f"Temperature: {temp} C {agent.perceive_temperature(temp)}")