# Monitoreo de Temperatura con Raspberry Pi Pico W y ThingSpeak

Este proyecto permite leer la temperatura del sensor interno de la Raspberry Pi Pico W y enviar los datos a la plataforma ThingSpeak cada 180 segundos. Está desarrollado en MicroPython y se ejecuta en la Pico W utilizando el IDE Thonny.

## Requisitos

### Hardware
- Raspberry Pi Pico W
- Cable micro USB
- Conexión a Internet vía Wi-Fi

### Software
- [Thonny IDE](https://thonny.org/) (versión recomendada 4.0 o superior)
- MicroPython instalado en la Raspberry Pi Pico W

## Instalación

### 1. Configurar Thonny IDE
1. Descarga e instala [Thonny IDE](https://thonny.org/).
2. Conecta la Raspberry Pi Pico W a tu computadora mediante el cable USB.
3. En Thonny, selecciona `Herramientas > Opciones`.
4. Ve a la pestaña `Interprete` y selecciona `MicroPython (Raspberry Pi Pico)`.
5. Si es la primera vez que usas la Pico W, haz clic en `Instalar firmware` y sigue las instrucciones.
6. Confirma que la conexión está activa revisando la consola de Thonny.

### 2. Subir el Código al Microcontrolador
1. Descarga o copia el código del archivo `main.py` en Thonny.
2. Reemplaza las credenciales Wi-Fi y la clave de API de ThingSpeak en el código:
   ```python
   SSID = "TU_SSID"
   PASSWORD = "TU_PASSWORD"
   API_KEY = "TU_API_KEY"
   THINGSPEAK_URL = "https://api.thingspeak.com/update"
   ```
3. Guarda el archivo como `main.py` en la Raspberry Pi Pico W (`Archivo > Guardar como > Raspberry Pi Pico`).
4. Reinicia la Pico W o ejecuta el código desde Thonny.

## Uso
1. Una vez que el código se está ejecutando, la Pico W se conectará a la red Wi-Fi.
2. Leerá la temperatura interna y la enviará a ThingSpeak cada 180 segundos.
3. Puedes visualizar los datos en tu canal de ThingSpeak en la pestaña de gráficos.

## Solución de Problemas
- **Error de conexión a Wi-Fi**: Verifica que el SSID y la contraseña sean correctos.
- **No se envían datos a ThingSpeak**: Confirma que la API Key es válida y que el canal en ThingSpeak está configurado correctamente.
- **Thonny no detecta la Pico W**: Prueba cambiar el cable USB o reinstalar el firmware de MicroPython.

## Créditos
Este proyecto fue desarrollado como una implementación de monitoreo remoto de temperatura utilizando IoT con Raspberry Pi Pico W y MicroPython.

