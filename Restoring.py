import cv2
import os

# Ruta de la imagen (verifica que sea correcta)
ruta_imagen = r"C:\Users\theal\Desktop\Python_for_research\Restoring\Example.jpg"

# Verificar si la imagen existe
if not os.path.exists(ruta_imagen):
    print(f"❌ Error: No se encontró la imagen en la ruta: {ruta_imagen}")
else:
    print("✅ Imagen encontrada. Cargando...")

    # Cargar la imagen en color
    imagen = cv2.imread(ruta_imagen)

    # Verificar que la imagen se haya cargado correctamente
    if imagen is None:
        print("❌ Error: No se pudo abrir la imagen.")
    else:
        # Convertir la imagen a escala de grises
        gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

        # Mostrar la imagen original y en escala de grises
        cv2.imshow('Imagen Original', imagen)
        cv2.imshow('Escala de Grises', gris)

        # Esperar a que el usuario presione una tecla para cerrar
        cv2.waitKey(0)
        cv2.destroyAllWindows()
