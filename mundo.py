from .entidad import Entidad
from .relacion import Relacion
from .regla import Regla

class Mundo:

    def __init__(self):
        self.entidades = {}
        self.relaciones = {}
        self.reglas = {}

    def agregar_entidad(self, entidad):
        self.entidades[entidad.id] = entidad

    def eliminar_entidad(self, entidad):
        del self.entidades[entidad.id]

    def obtener_entidad(self, id_entidad):
        return self.entidades[id_entidad]

    def agregar_relacion(self, relacion):
        self.relaciones[relacion.id] = relacion

    def eliminar_relacion(self, relacion):
        del self.relaciones[relacion.id]

    def obtener_relacion(self, id_relacion):
        return self.relaciones[id_relacion]

    def agregar_regla(self, regla):
        self.reglas[regla.id] = regla

    def eliminar_regla(self, regla):
        del self.reglas[regla.id]

    def obtener_regla(self, id_regla):
        return self.reglas[id_regla]

    def simular(self, tiempo_simulacion):
        # Simular la dinámica del mundo
        # ...

    def aplicar_reglas(self):
        # Aplicar las reglas del mundo
        # ...

    def obtener_estado(self):
        # Obtener el estado actual del mundo
        # ...

    def generar_observacion(self):
        # Generar una observación del mundo
        # ...
