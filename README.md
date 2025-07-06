# 🌿 Projeto IoT: Irrigação Automática

Este projeto simula um sistema de irrigação automática baseado na arquitetura **Sensor–Controller–Actuator (SCA)**, usando **Python orientado a objetos**. A estrutura é modular e escalável, permitindo a adição de múltiplos sensores, atuadores e controladores especializados.

---

## 🔧 Funcionamento

1. Um **Sensor de Umidade do Solo** simula leituras de umidade (valores aleatórios entre 10% e 80%).
2. Um **Controlador de Irrigação** verifica se a umidade está abaixo do limite.
3. Um **Atuador (Válvula de Água)** abre ou fecha conforme o comando.

---

## 🧱 Estrutura do Projeto

```
irrigacao_automatica/
├── main.py                      # Ponto de entrada do sistema
├── iot_thing.py                 # Orquestrador do ciclo Sensor–Controller–Actuator

├── sensors/                     # Sensores disponíveis
│   ├── __init__.py
│   ├── base.py                  # Classe abstrata Sensor
│   └── soil_moisture.py         # Sensor de umidade do solo

├── actuators/                   # Atuadores disponíveis
│   ├── __init__.py
│   ├── base.py                  # Classe abstrata Actuator
│   └── water_valve.py           # Atuador (válvula de irrigação)

├── controllers/                 # Controladores de lógica de decisão
│   ├── __init__.py
│   ├── base.py                  # Classe abstrata Controller
│   └── irrigacao_controller.py # Controlador da lógica de irrigação
```

## 🔄 Arquitetura UML (SCA)

- `IoTThing` contém um `Controller`.
- `Controller` possui uma lista de `Sensor`(es) e `Actuator`(es).
- `Sensor` e `Actuator` são classes base abstratas herdadas por sensores/atuadores concretos.

Diagrama simplificado:
![SCA_UML_DIAGRAM](https://github.com/user-attachments/assets/a59d25f9-2927-480e-8e02-a121bc0e7a69)
