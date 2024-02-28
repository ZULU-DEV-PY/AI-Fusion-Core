Ejecución del proyecto:

Para ejecutar el proyecto, siga estos pasos:

Instale las dependencias necesarias.
Ejecute el comando python app.py.
Contribuciones:

Se aceptan contribuciones al proyecto. Para más información, consulte el archivo CONTRIBUTING.md.

Licencia:

Este proyecto está licenciado bajo la licencia Apache 2.0.

Contacto:

Si tiene alguna pregunta o necesita más ayuda, no dude en ponerse en contacto con el autor del proyecto.


No todas las clases van en la clase Interfaz.

Organización de las clases:

Entidad.py: Contiene la clase Entidad y sus clases hijas (por ejemplo, Persona, Objeto).
Relacion.py: Contiene la clase Relacion y sus clases hijas (por ejemplo, Amistad, Cercania).
Mundo.py: Contiene la clase Mundo que representa el estado del mundo.
Regla.py: Contiene la clase Regla y sus clases hijas (por ejemplo, ReglaPersonaMayorDeEdad).
Sensor.py: Contiene la clase Sensor y sus clases hijas (por ejemplo, SensorCamara).
Actuador.py: Contiene la clase Actuador y sus clases hijas (por ejemplo, ActuadorMotor).
Controlador.py: Contiene la clase Controlador que se encarga de leer los sensores, procesar la información y enviar comandos a los actuadores.
Interfaz.py: Contiene la clase Interfaz que se encarga de la visualización del estado del mundo y la interacción con el usuario.
Ejemplo de estructura de archivos:

├── entidades
│   ├── entidad.py
│   └── persona.py
│   └── objeto.py
└── relaciones
    ├── relacion.py
    └── amistad.py
    └── cercania.py
mundo.py
reglas
├── regla.py
└── regla_persona_mayor_edad.py
sensores
├── sensor.py
└── sensor_camara.py
actuadores
├── actuador.py
└── actuador_motor.py
controlador.py
interfaz.py
Importación de las clases:

En la clase Interfaz se importan las clases que se necesitan para la visualización del mundo y la interacción con el usuario.

Python
from entidades import Persona, Objeto
from relaciones import Amistad, Cercania
from mundo import Mundo
from reglas import ReglaPersonaMayorDeEdad
from sensores import SensorCamara
from actuadores import ActuadorMotor
from controlador import Controlador
Usa el código con precaución.
Nota:

Esta es una estructura de ejemplo, puedes adaptarla a las necesidades de tu proyecto.

imagen de perfil
desarrolla la Referencia API: Documentación de clases, métodos y parámetros.
Referencia API: Documentación de Clases, Métodos y Parámetros
Clase Entidad:

Descripción:

Representa una entidad del mundo.

Atributos:

nombre: El nombre de la entidad.
id: El identificador único de la entidad.
estado: Un diccionario que contiene el estado actual de la entidad.
Métodos:

__init__(self, nombre): Constructor de la clase Entidad.
obtener_id(self): Obtiene el identificador de la entidad.
obtener_estado(self): Obtiene el estado actual de la entidad.
Ejemplo:

Python
entidad = Entidad("Persona")
print(entidad.nombre)  # Salida: "Persona"
print(entidad.obtener_id())  # Salida: "Persona_1234"
print(entidad.obtener_estado())  # Salida: {"edad": 25, "posicion": (10, 20)}
Usa el código con precaución.
Clase Persona:

Descripción:

Representa una entidad del mundo de tipo persona.

Atributos:

nombre: El nombre de la persona.
id: El identificador único de la persona.
edad: La edad de la persona.
posicion: La posición actual de la persona.
Métodos:

__init__(self, nombre, edad, posicion): Constructor de la clase Persona.
obtener_id(self): Obtiene el identificador de la persona.
obtener_estado(self): Obtiene el estado actual de la persona.
Ejemplo:

Python
persona = Persona("Juan", 25, (10, 20))
print(persona.nombre)  # Salida: "Juan"
print(persona.obtener_id())  # Salida: "Persona_1234"
print(persona.obtener_estado())  # Salida: {"edad": 25, "posicion": (10, 20)}
Usa el código con precaución.
Clase Relacion:

Descripción:

Representa una relación entre dos entidades.

Atributos:

entidad1: La primera entidad de la relación.
entidad2: La segunda entidad de la relación.
id: El identificador único de la relación.
tipo: El tipo de la relación.
Métodos:

__init__(self, entidad1, entidad2): Constructor de la clase Relacion.
obtener_id(self): Obtiene el identificador de la relación.
obtener_tipo(self): Obtiene el tipo de la relación.
Ejemplo:

Python
persona1 = Persona("Juan", 25, (10, 20))
persona2 = Persona("Maria", 28, (20, 30))
relacion = Amistad(persona1, persona2)
print(relacion.obtener_id())  # Salida: "Amistad_1234"
print(relacion.obtener_tipo())  # Salida: "Amistad"
Usa el código con precaución.
Clase Amistad:

Descripción:

Representa una relación de amistad entre dos personas.

Atributos:

entidad1: La primera persona de la amistad.
entidad2: La segunda persona de la amistad.
id: El identificador único de la amistad.
tipo: El tipo de la relación (en este caso, "Amistad").
Métodos:

__init__(self, persona1, persona2): Constructor de la clase Amistad.
obtener_id(self): Obtiene el identificador de la amistad.
obtener_tipo(self): Obtiene el tipo de la relación.
Ejemplo:

Python
persona1 = Persona("Juan", 25, (10, 20))
persona2 = Persona("Maria", 28, (20, 30))
amistad = Amistad(persona1, persona2)
print(amistad.obtener_id())  # Salida: "Amistad_1234"
print(amistad.obtener_tipo())  # Salida: "Amistad"
Usa el código con precaución.
Clase Mundo:

Descripción:

Representa el estado del mundo.

Atributos:

entidades: Un diccionario que contiene todas las entidades del mundo.
relaciones: Un diccionario que contiene todas las relaciones del mundo.
Métodos:

agregar_entidad(self, entidad): Agrega una entidad
imagen de perfil
continua
Continuación de la Referencia API: Documentación de Clases, Métodos y Parámetros
Clase Mundo:

Métodos:

agregar_entidad(self, entidad): Agrega una entidad al mundo.
eliminar_entidad(self, entidad): Elimina una entidad del mundo.
obtener_entidad(self, id_entidad): Obtiene una entidad por su identificador.
agregar_relacion(self, relacion): Agrega una relación al mundo.
eliminar_relacion(self, relacion): Elimina una relación del mundo.
obtener_relacion(self, id_relacion): Obtiene una relación por su identificador.
simular(self, tiempo_simulacion): Simula la dinámica del mundo durante un tiempo determinado.
aplicar_reglas(self): Aplica las reglas del mundo al estado actual.
obtener_estado(self): Obtiene el estado actual del mundo.
generar_observacion(self): Genera una observación del mundo.
Ejemplo:

Python
mundo = Mundo()
persona1 = Persona("Juan", 25, (10, 20))
persona2 = Persona("Maria", 28, (20, 30))
amistad = Amistad(persona1, persona2)

mundo.agregar_entidad(persona1)
mundo.agregar_entidad(persona2)
mundo.agregar_relacion(amistad)

mundo.simular(10)
estado_mundo = mundo.obtener_estado()

print(estado_mundo)  # Salida: {"entidades": {"Persona_1234": {"nombre": "Juan", "edad": 25, "posicion": (10, 20)}, "Persona_4567": {"nombre": "Maria", "edad": 28, "posicion": (20, 30)}}, "relaciones": {"Amistad_1234": {"entidad1": "Persona_1234", "entidad2": "Persona_4567", "tipo": "Amistad"}}}
Usa el código con precaución.
Clase Regla:

Descripción:

Representa una regla del mundo.

Atributos:

condiciones: Una lista de condiciones que deben cumplirse para que la regla se active.
acciones: Una lista de acciones que se ejecutan cuando la regla se activa.
Métodos:

__init__(self, condiciones, acciones): Constructor de la clase Regla.
evaluar(self, mundo): Evalúa si la regla se cumple en el estado actual del mundo.
Ejemplo:

Python
class ReglaPersonaMayorDeEdad(Regla):

    def __init__(self):
        super().__init__(
            condiciones=[
                lambda mundo: mundo.obtener_entidad("Persona_1234").edad >= 18,
            ],
            acciones=[
                lambda mundo: print("La persona es mayor de edad"),
            ],
        )

    def evaluar(self, mundo):
        return super().evaluar(mundo)

regla = ReglaPersonaMayorDeEdad()
regla.evaluar(mundo)  # Salida: "La persona es mayor de edad"
Usa el código con precaución.
Clase Sensor:

Descripción:

Representa un sensor del mundo.

Atributos:

nombre: El nombre del sensor.
tipo: El tipo de sensor.
Métodos:

__init__(self, nombre, tipo): Constructor de la clase Sensor.
leer_datos(self): Lee datos del sensor.
preprocesar_datos(self, datos): Preprocesa los datos leídos por el sensor.
Ejemplo:

Python
class SensorCamara(Sensor):

    def __init__(self):
        super().__init__(
            nombre="Camara",
            tipo="Vision",
        )

    def leer_datos(self):
        # Leer imágenes de la cámara
        # ...

    def preprocesar_datos(self, datos):
        # Detectar objetos en las imágenes
        # ...

sensor_camara = SensorCamara()
datos_camara = sensor_camara.leer_datos()
datos_preprocesados = sensor_camara.preprocesar_datos(datos_camara)

print(datos_preprocesados)  # Salida: {"objetos": ["Persona", "Coche"], "posiciones": {"Persona": (10, 20), "Coche
Usa el código con precaución.
imagen de perfil
continua
Mostrar versiones

Continuación de la Referencia API: Documentación de Clases, Métodos y Parámetros
Clase Actuador:

Descripción:

Representa un actuador del mundo.

Atributos:

nombre: El nombre del actuador.
tipo: El tipo de actuador.
Métodos:

__init__(self, nombre, tipo): Constructor de la clase Actuador.
enviar_comando(self, comando): Envía un comando al actuador.
Ejemplo:

Python
class ActuadorMotor(Actuador):

    def __init__(self):
        super().__init__(
            nombre="Motor",
            tipo="Movimiento",
        )

    def enviar_comando(self, comando):
        # Enviar comandos al motor
        # ...

actuador_motor = ActuadorMotor()
comando_motor = {"velocidad": 10, "direccion": "norte"}
actuador_motor.enviar_comando(comando_motor)
Usa el código con precaución.
Clase Controlador:

Descripción:

Representa el controlador del sistema.

Atributos:

mundo: El mundo que se está controlando.
sensores: Un diccionario que contiene todos los sensores del mundo.
actuadores: Un diccionario que contiene todos los actuadores del mundo.
Métodos:

__init__(self, mundo, sensores, actuadores): Constructor de la clase Controlador.
leer_sensores(self): Lee datos de todos los sensores.
procesar_informacion(self, datos_sensores): Procesa la información de los sensores.
generar_comandos(self, decisiones): Genera comandos para los actuadores.
enviar_comandos(self, comandos): Envía comandos a los actuadores.
ejecutar_ciclo_control(self): Ejecuta un ciclo de control continuo.
Ejemplo:

Python
mundo = Mundo()
sensor_camara = SensorCamara()
actuador_motor = ActuadorMotor()

controlador = Controlador(
    mundo=mundo,
    sensores={"Camara": sensor_camara},
    actuadores={"Motor": actuador_motor},
)

while True:
    # Leer datos de los sensores
    datos_sensores = controlador.leer_sensores()

    # Procesar la información y generar decisiones
    decisiones = controlador.procesar_informacion(datos_sensores)

    # Generar comandos y enviarlos a los actuadores
    comandos = controlador.generar_comandos(decisiones)
    controlador.enviar_comandos(comandos)
Usa el código con precaución.
Clase Interfaz:

Descripción:

Representa la interfaz gráfica de usuario del sistema.

Atributos:

mundo: El mundo que se está visualizando.
controlador: El controlador del sistema.
Métodos:

__init__(self, mundo, controlador): Constructor de la clase Interfaz.
actualizar(self): Actualiza la interfaz gráfica de usuario.
Ejemplo:

Python
class Interfaz:

    def __init__(self, mundo, controlador):
        self.mundo = mundo
        self.controlador = controlador

        # Crear la ventana principal
        self.ventana = tk.Tk()
        self.ventana.title("Interfaz del Sistema")

        # ... (implementación de la interfaz gráfica de usuario)

    def actualizar(self):
        # ... (implementación de la actualización de la interfaz)

interfaz = Interfaz(mundo, controlador)

while True:
    # Actualizar la interfaz gráfica de usuario
    interfaz.actualizar()

    # ... (resto del código del bucle principal)
