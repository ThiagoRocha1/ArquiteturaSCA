class Controller:
    def __init__(self, sensors, actuators, target_temp=25.0, margin=1.0):
        self.sensors = sensors
        self.actuators = actuators
        self.target_temp = target_temp
        self.margin = margin

    def process(self):
        for sensor in self.sensors:
            temperature = sensor.read()
            print(f"\n🌡️  Temperatura atual: {temperature}°C")

            if temperature > self.target_temp + self.margin:
                action = 'ligar'
            elif temperature < self.target_temp - self.margin:
                action = 'desligar'
            else:
                action = 'manter'

            for actuator in self.actuators:
                actuator.act(action)
