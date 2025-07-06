from actuators.base import Actuator

class WaterValve(Actuator):
    def __init__(self) -> None:
        self._state: str = "fechada"

    def act(self, command: str) -> None:
        if command == "abrir" and self._state != "aberta":
            print("💧 Abrindo válvula...")
            self._state = "aberta"
        elif command == "fechar" and self._state != "fechada":
            print("🚫 Fechando válvula...")
            self._state = "fechada"
        else:
            print("⏸️  Mantendo o estado da válvula.")
