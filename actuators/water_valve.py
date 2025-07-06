from actuators.base import Actuator

class WaterValve(Actuator):
    def __init__(self):
        self.state = "fechada"

    def act(self, command):
        if command == "abrir" and self.state != "aberta":
            print("💧 Abrindo válvula...")
            self.state = "aberta"
        elif command == "fechar" and self.state != "fechada":
            print("🚫 Fechando válvula...")
            self.state = "fechada"
        else:
            print("⏸️  Mantendo o estado da válvula.")
