import tensorflow as tf
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.models import Sequential

class RazonamientoCNN:

    def __init__(self):
        self.modelo = self._crear_modelo()

    def _crear_modelo(self):
        # Definir la arquitectura de la CNN
        modelo = Sequential()
        modelo.add(Conv2D(32, (3, 3), activation='relu', input_shape=(28, 28, 1)))
        modelo.add(MaxPooling2D((2, 2)))
        modelo.add(Conv2D(64, (3, 3), activation='relu'))
        modelo.add(MaxPooling2D((2, 2)))
        modelo.add(Flatten())
        modelo.add(Dense(128, activation='relu'))
        modelo.add(Dense(10, activation='softmax'))

        # Compilar el modelo
        modelo.compile(loss='categorical_crossentropy', optimizer='adam', metrics=['accuracy'])

        return modelo

    def cargar_pesos(self, ruta_pesos):
        # Cargar los pesos del modelo
        self.modelo.load_weights(ruta_pesos)

    def entrenar(self, imagenes, etiquetas, epocas=10):
        # Entrenar la CNN
        self.modelo.fit(imagenes, etiquetas, epochs=epocas)

    def evaluar(self, imagenes, etiquetas):
        # Evaluar la CNN
        score = self.modelo.evaluate(imagenes, etiquetas)
        return score

    def razonar(self, imagen):
        # Predecir la clase de la imagen
        prediccion = self.modelo.predict(imagen)
        return prediccion

