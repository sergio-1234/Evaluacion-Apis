# Importar las librerías necesarias
import requests
from dearpygui import dearpygui as dpg
import threading

# Función para obtener el precio de una criptomoneda desde la API de Binance
def obtener_precio(par):
   
    url = f"https://api.binance.com/api/v3/ticker/price?symbol={par}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        return float(datos['price'])
    else:
        raise Exception("Error al obtener datos de la API")

# Función para actualizar los precios de las criptomonedas en la interfaz gráfica
def actualizar_precios():
    
    try:
        btc = obtener_precio("BTCUSDT")
        eth = obtener_precio("ETHUSDT")
        bnb = obtener_precio("BNBUSDT")

        # Actualiza los valores mostrados en la interfaz
        dpg.set_value("BTC", f"Bitcoin: {btc:.2f} USD")
        dpg.set_value("ETH", f"Ethereum: {eth:.2f} USD")
        dpg.set_value("BNB", f"Binance Coin: {bnb:.2f} USD")
    except Exception as e:
        print(f"Error al actualizar precios: {e}")

# Función para crear un temporizador que actualice los precios cada 5 segundos
def iniciar_actualizacion_automatica():
   
    actualizar_precios()  # Llama a actualizar precios
    threading.Timer(5, iniciar_actualizacion_automatica).start()  # Repite cada 5 segundos

# Configuración de la interfaz gráfica
dpg.create_context()
dpg.create_viewport(title="MONITOR DE CRIPTOMONEDAS", width=400, height=300)

with dpg.window(label="PRECIOS EN TIEMPO REAL", width=400, height=300):
    dpg.add_text("NOMBRE DE LA CRIPTOMONEDA", color=(255, 255, 255))
    # Etiquetas con el nombre completo de cada criptomoneda
    dpg.add_text("Bitcoin: ", tag="BTC", color=(0, 255, 0))
    dpg.add_text("Ethereum: ", tag="ETH", color=(0, 255, 0))
    dpg.add_text("Binance Coin: ", tag="BNB", color=(0, 255, 0))
    dpg.add_button(label="Actualizar Manualmente", callback=actualizar_precios)

# Iniciar la actualización automática
iniciar_actualizacion_automatica()

# Configura la interfaz y la muestra
dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()

