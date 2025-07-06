# Projeto: Ar-Condicionado Inteligente (Arquitetura Sensor–Controller–Actuator)

Este projeto simula, em Python orientado a objetos, o funcionamento de um sistema de **ar-condicionado inteligente** baseado na arquitetura **Sensor–Controller–Actuator (SCA)**, utilizando um modelo inspirado no **diagrama UML** enviado.

## Funcionamento

- Um **Sensor de Temperatura** simula a leitura do ambiente.
- Um **Controlador** toma decisões com base na temperatura lida.
- Um **Atuador (Ar-Condicionado)** executa as ações: ligar, desligar ou manter.

## Relacionamentos UML

O projeto segue a estrutura:

- `IoTThing` contém um `Controller`.
- `Controller` possui referências a múltiplos `Sensor`(es) e `Actuator`(es).
- `Sensor` é uma classe base abstrata, estendida por `TemperatureSensor`.
- `Actuator` é uma classe base abstrata, estendida por `AirConditioner`.

Diagrama UML:

![SCA_UML_DIAGRAM](https://github.com/user-attachments/assets/a59d25f9-2927-480e-8e02-a121bc0e7a69)
