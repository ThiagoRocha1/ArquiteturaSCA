from sensor import TemperatureSensor
from actuator import AirConditioner
from controller import Controller
from iot_thing import IoTThing

def main():
    # Instâncias
    sensor = TemperatureSensor()
    actuator = AirConditioner()

    # Controller recebe lista de sensores e atuadores
    controller = Controller(sensors=[sensor], actuators=[actuator])

    # IoTThing encapsula o controller e executa o ciclo
    device = IoTThing(controller)
    device.run()

if __name__ == "__main__":
    main()
