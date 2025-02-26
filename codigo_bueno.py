import network  # Módulo para gestionar la conexión Wi-Fi
import urequests  # Módulo para realizar solicitudes HTTP
import utime  # Módulo para manejar pausas y tiempos de espera
import machine  # Módulo para interactuar con el hardware del microcontrolador

# Credenciales de la red Wi-Fi
SSID = "riqiperes"
PASSWORD = "14121702RMPQ"

# Clave de API y URL de ThingSpeak (Reemplazar con los valores adecuados)
API_KEY = "KU3PUMINBP8L5PMY"
THINGSPEAK_URL = "https://api.thingspeak.com/update"

def conectar_wifi():
    """
    Función para conectar el microcontrolador a una red Wi-Fi.
    """
    wlan = network.WLAN(network.STA_IF)  # Se configura la interfaz Wi-Fi en modo cliente (STA)
    wlan.active(True)  # Se activa la interfaz Wi-Fi
    wlan.connect(SSID, PASSWORD)  # Se conecta a la red Wi-Fi usando las credenciales proporcionadas
    
    print("Conectando a Wi-Fi...")
    while not wlan.isconnected():  # Se espera hasta que la conexión sea exitosa
        utime.sleep(1)  # Pausa de 1 segundo para evitar ciclos innecesarios
    
    print("Conectado a Wi-Fi:", wlan.ifconfig())  # Se muestra la configuración de red obtenida

def leer_temperatura():
    """
    Función para leer la temperatura desde el sensor interno del microcontrolador.
    
    Retorna:
        float: Temperatura en grados Celsius redondeada a 2 decimales.
    """
    sensor_temp = machine.ADC(4)  # Se configura el ADC en el canal 4 para obtener la lectura del sensor interno
    conversion_factor = 3.3 / 65535  # Factor de conversión para transformar la lectura ADC a voltaje
    lectura = sensor_temp.read_u16() * conversion_factor  # Se obtiene el voltaje del sensor
    temperatura = 27 - (lectura - 0.706) / 0.001721  # Cálculo de temperatura basado en la fórmula del sensor
    return round(temperatura, 2)  # Se redondea la temperatura a dos decimales

def enviar_a_thingspeak(temp):
    """
    Función para enviar la temperatura a ThingSpeak mediante una solicitud HTTP GET.
    
    Parámetros:
        temp (float): Temperatura a enviar a la plataforma.
    """
    try:
        # Se construye la URL con la clave API y el valor de temperatura en el campo 1
        respuesta = urequests.get(f"{THINGSPEAK_URL}?api_key={API_KEY}&field1={temp}")
        print("Enviado a ThingSpeak:", respuesta.text)  # Se imprime la respuesta del servidor
        respuesta.close()  # Se cierra la conexión para liberar recursos
    except Exception as e:
        print("Error enviando datos:", e)  # Se muestra el error en caso de falla

# Se establece la conexión Wi-Fi antes de comenzar el proceso de envío de datos
conectar_wifi()

while True:
    """
    Bucle principal del programa:
    1. Lee la temperatura desde el sensor.
    2. Imprime la temperatura en consola.
    3. Envía la temperatura a ThingSpeak.
    4. Espera 180 segundos antes de repetir el ciclo.
    """
    temperatura = leer_temperatura()  # Se obtiene la temperatura actual
    print("Temperatura actual:", temperatura, "°C")  # Se muestra la temperatura en consola
    enviar_a_thingspeak(temperatura)  # Se envía la temperatura a ThingSpeak
    utime.sleep(180)  # Se espera 3 minutos antes de la próxima medición
