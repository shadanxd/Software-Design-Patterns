# Adapter Design Pattern
# As name suggests its used as a code adapter between two seemingly incompatible interfaces


# Adaptee: Existing class representing temperature readings in Celsius in our own codebase
class CelsiusSensor:
    def __init__(self, temperature):
        self.temperature = temperature
    
    def get_temperature(self):
        return self.temperature
    
# Target: Interface for temperature readings in Fahrenheit a third party interface that needs temp in F
# Abstract method
class FahrenheitSensor:
    def get_temperature(self):
        raise NotImplementedError()

# Adapter: Adapts CelsiusSensor to work with FahrenheitSensor interface inherits constructor and methods of both the classes
class CelsiusToFahrenheitAdapter(CelsiusSensor, FahrenheitSensor):
    
    def __init__(self, celsius_sensor):
        self.celsius_sensor = celsius_sensor

    def get_temperature(self):
        # Convert Celsius to Fahrenheit
        celsius_temp = self.celsius_sensor.get_temperature()
        fahrenheit_temp = (celsius_temp * 9/5) + 32
        return fahrenheit_temp

# Client code that uses the FahrenheitSensor interface
def client_code(sensor):
    print(f"Temperature in Fahrenheit: {sensor.get_temperature()}°F")

# Usage
celsius_sensor = CelsiusSensor(20)  # Temperature in Celsius
adapter = CelsiusToFahrenheitAdapter(celsius_sensor)  # Adapter to convert Celsius to Fahrenheit
client_code(adapter)
