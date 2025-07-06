from sensors.soil_moisture import SoilMoistureSensor
from actuators.water_valve import WaterValve
from controllers.irrigacao_controller import IrrigationController
from iot_thing import IoTThing

def main():
    sensor = SoilMoistureSensor()
    actuator = WaterValve()
    controller = IrrigationController([sensor], [actuator])
    system = IoTThing(controller)
    system.run()

if __name__ == "__main__":
    main()
