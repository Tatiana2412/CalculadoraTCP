import socket                       # Librería estándar 'socket' para crear sockets TCP/IP.
import tkinter as tk                # Importa tkinter para crear la interfaz gráfica (alias 'tk' para abreviar).
from tkinter import messagebox      # Importa el submódulo messagebox para mostrar diálogos (errores, avisos).

# -------------------------
# Configuración de red
# -------------------------
SERVER_IP = "192.168.1.8"          # IP del servidor.
PORT = 5000                        # Puerto TCP donde el servidor está escuchando (debe coincidir con el servidor).

# -------------------------
# Función que envía la operación y recibe el resultado
# -------------------------
def calcular():
    """
    6. Función llamada cuando el usuario hace clic en "Calcular".
       Reúne los datos de la interfaz, valida, abre conexión TCP, envía el mensaje,
       recibe el resultado y lo muestra en la etiqueta de resultado.
    """

    num1 = entrada_num1.get()       # Lee el texto actual del campo de entrada 'entrada_num1'.
    num2 = entrada_num2.get()       # Lee el texto actual del campo de entrada 'entrada_num2'.
    operador = operacion.get()      # Obtiene el operador seleccionado en el OptionMenu ('+', '-', '*', '/').

    #Validación básica: asegurar que los campos no estén vacíos.

    if not num1 or not num2:
        messagebox.showwarning("Datos incompletos", "Debe ingresar ambos números.")
        return                      # Sale de la función si faltan datos.

    # Validación de formato: intentar convertir a float para asegurarnos que sean números.

    try:
        float(num1)                 #Intento de conversión para validar; no guardamos el valor convertido aún.
        float(num2)
    except ValueError:

        # Si la conversión falla lanzamos un aviso al usuario y no continuamos.
        messagebox.showwarning("Valor inválido", "Los valores deben ser números (ej: 3.5 o 7).")
        return

    # Construimos el mensaje con el formato que espera el servidor: "num1 operador num2"
    mensaje = f"{num1} {operador} {num2}"

    # Intento de conexión y comunicación dentro de un bloque try/except para capturar errores de red.
    try:
        cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # Crea un socket IPv4 (AF_INET) orientado a conexión/TCP (SOCK_STREAM).

        cliente.connect((SERVER_IP, PORT))
        # Inicia la conexión TCP con el servidor usando la IP y el puerto configurados.
        #     Si el servidor no responde o la IP es incorrecta, esto lanzará una excepción.

        cliente.send(mensaje.encode())
        # Envía el mensaje al servidor codificado a bytes (UTF-8 por defecto).
        #     .encode() convierte la cadena a bytes para la transmisión.

        resultado = cliente.recv(1024).decode()
        # Recibe hasta 1024 bytes de respuesta del servidor y los decodifica a string.
        #     Asumimos que el servidor envía una respuesta corta (resultado de la operación).

        etiqueta_resultado.config(text=f"Resultado: {resultado}")
        # Actualiza la etiqueta en la interfaz con el resultado recibido.

        cliente.close()
        # Cierra el socket para liberar recursos y terminar la conexión TCP.
    except Exception as e:
        # Si ocurre cualquier excepción (conexión rechazada, timeout, etc.), mostramos un error.
        messagebox.showerror("Error de conexión", f"No se pudo conectar al servidor.\n\nDetalle: {e}")

# -------------------------
# Construcción de la interfaz gráfica
# -------------------------
ventana = tk.Tk()                   # Crea la ventana principal de la aplicación.
ventana.title("Calculadora Remota TCP")  # Título de la ventana.
ventana.geometry("320x280")         # Tamaño inicial de la ventana.
ventana.resizable(False, False)     # Evita que el usuario cambie el tamaño. 
ventana.configure(bg="#F3E6F8") 

# Etiqueta y campo para el primer número
tk.Label(ventana, text="Número 1:", bg="#F3E6F8", anchor="w").pack(padx=10, pady=(12,2), fill="x")
entrada_num1 = tk.Entry(ventana)    # Campo de entrada para el primer número.
entrada_num1.pack(padx=10, pady=(0,8), fill="x")

# Etiqueta y campo para el segundo número
tk.Label(ventana, text="Número 2:", bg="#F3E6F8", anchor="w").pack(padx=10, pady=(6,2), fill="x")
entrada_num2 = tk.Entry(ventana)    # Campo de entrada para el segundo número.
entrada_num2.pack(padx=10, pady=(0,8), fill="x")

# Etiqueta y menú para seleccionar la operación
tk.Label(ventana, text="Operación:", anchor="w").pack(padx=10, pady=(6,2), fill="x")
operacion = tk.StringVar(value="+") # Variable de control que guarda la opción seleccionada; valor inicial '+'.
menu_operacion = tk.OptionMenu(ventana, operacion, "+", "-", "*", "/")

# OptionMenu crea un desplegable con las cuatro operaciones y lo enlaza a 'operacion'.
menu_operacion.pack(padx=10, pady=(0,8), fill="x")

# Botón principal que ejecuta la función 'calcular' al hacer clic
boton_calcular = tk.Button(ventana, text="Calcular", command=calcular)
boton_calcular.pack(padx=10, pady=(6,10), fill="x")

# Etiqueta del resultado 
etiqueta_resultado = tk.Label(
    ventana,
    text="Resultado:",
    bg="#F3E6F8",          
    font=("Arial", 10, "bold"),  
    fg="black"            
)
etiqueta_resultado.pack(padx=10, pady=(10,6), fill="x")

# Inicia el loop principal de la interfaz; la aplicación queda a la espera de eventos (clics, entradas).
ventana.mainloop()
