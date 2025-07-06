class Actuator:
    def act(self, command):
        raise NotImplementedError

class AirConditioner(Actuator):
    def __init__(self):
        self.state = 'desligado'

    def act(self, command):
        if command == 'ligar' and self.state != 'ligado':
            print("❄️  Ligando o ar-condicionado...")
            self.state = 'ligado'
        elif command == 'desligar' and self.state != 'desligado':
            print("🔕  Desligando o ar-condicionado...")
            self.state = 'desligado'
        else:
            print("👌  Mantendo o estado atual.")
