# Name: Fatima                BSAI(3A)
# Roll no: SU92-BSAIM-S25-025
# Task 3:



class ModelBasedReflexAgent:
    def __init__(self):
        self.previous_action = "OFF"   

    def perceive_and_act(self, temperature):
        print(f"\nCurrent Temperature: {temperature}°C")
        print(f"Previous Action: Heater {self.previous_action}")

        
        if temperature < 20:
            if self.previous_action != "ON":
                self.previous_action = "ON"
                print("Action: Turning Heater ON")
            else:
                print("Action: Heater already ON (No change)")

        elif temperature > 25:
            if self.previous_action != "OFF":
                self.previous_action = "OFF"
                print("Action: Turning Heater OFF")
            else:
                print("Action: Heater already OFF (No change)")

        else:
            print("Action: Temperature normal (No change)")

        return self.previous_action


# Testing the Agent
agent = ModelBasedReflexAgent()

temperatures = [18, 17, 22, 27, 26, 23, 19]

for temp in temperatures:
    agent.perceive_and_act(temp)