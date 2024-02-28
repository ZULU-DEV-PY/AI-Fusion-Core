from tkinter import *

class Interfaz:

    def __init__(self):
        self.ventana = Tk()
        self.ventana.title("IA Completa")

        # Área de texto para la entrada de datos
        self.entrada_datos = Text(self.ventana, width=50, height=10)
        self.entrada_datos.pack()

        # Botón para procesar los datos
        self.boton_procesar = Button(self.ventana, text="Procesar", command=self.procesar_datos)
        self.boton_procesar.pack()

        # Área de texto para la salida de resultados
        self.salida_resultados = Text(self.ventana, width=50, height=10)
        self.salida_resultados.pack()

    def procesar_datos(self):
        # Obtener el texto de la entrada de datos
        datos_entrada = self.entrada_datos.get("1.0", "end-1c")

        # Procesar los datos
        procesamiento = Procesamiento()
        representacion_mundo = procesamiento.procesar_datos(datos_entrada)

        # Razonar sobre la representación del mundo
        razonamiento = Razonamiento()
        decisiones = razonamiento.razonar(representacion_mundo)

        # Actuar en el mundo real
        actuacion = Actuacion()
        actuacion.actuar(decisiones)

        # Mostrar los resultados en la salida
        self.salida_resultados.delete("1.0", "end-1c")
        self.salida_resultados.insert("1.0", str(representacion_mundo) + "\n" + str(decisiones))

if __name__ == "__main__":
    interfaz = Interfaz()
    interfaz.ventana.mainloop()
