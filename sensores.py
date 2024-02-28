from abc import ABC, abstractmethod

class Sensor(ABC):

    @abstractmethod
    def leer_datos(self):
        """
        Lee datos del sensor.

        Retorno:
            Los datos del sensor en un formato específico.
        """

    @abstractmethod
    def preprocesar_datos(self, datos):
        """
        Preprocesa y limpia los datos del sensor.

        Argumentos:
            datos: Los datos del sensor en bruto.

        Retorno:
            Los datos del sensor preprocesados.
        """

class SensorDistancia(Sensor):

    def leer_datos(self):
        # Leer la distancia del sensor
        # ...
        return distancia

    def preprocesar_datos(self, datos):
        # Filtrar valores atípicos
        # ...
        return datos

class SensorTemperatura(Sensor):

    def leer_datos(self):
        # Leer la temperatura del sensor
        # ...
        return temperatura

    def preprocesar_datos(self, datos):
        # Convertir a grados Celsius
        # ...
        return datos

class SincronizadorSensores:

    def __init__(self, sensores):
        self.sensores = sensores

    def sincronizar(self):
        # Leer datos de todos los sensores
        datos_sensores = {}
        for sensor in self.sensores:
            datos_sensores[sensor] = sensor.leer_datos()

        # Preprocesar los datos
        for sensor, datos in datos_sensores.items():
            datos_sensores[sensor] = sensor.preprocesar_datos(datos)

        # Sincronizar los datos con el resto del sistema
        # ...

if __name__ == "__main__":
    # Ejemplo de uso
    sensor_distancia = SensorDistancia()
    sensor_temperatura = SensorTemperatura()

    sincronizador = SincronizadorSensores([sensor_distancia, sensor_temperatura])

    while True:
        # Sincronizar los datos de los sensores
        sincronizador.sincronizar()

        # Procesar los datos sincronizados
        # ...

