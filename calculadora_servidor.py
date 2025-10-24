import socket # Importamos la librería necesaria para manejar sockets

# CONFIGURACIÓN DEL SERVIDOR
HOST = "0.0.0.0"  # Escucha en todas las interfaces de la red disponible.
PORT = 5000       # Puerto donde escuchará el servidor

# CREACIÓN DEL SOCKET TCP

# AF_INET -> Familia de direcciones IPv4
# SOCK_STREAM -> Tipo de socket TCP (orientado a conexión)
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORT))# Asociamos el socket con la dirección IP y el puerto definidos
servidor.listen(1) # Ponemos el socket en modo escucha, máximo 1 cliente en cola
print(f"Servidor escuchando en {HOST}:{PORT}...")

# CICLO PRINCIPAL DEL SERVIDOR

# Este ciclo permite atender múltiples clientes uno tras otro
while True:
    # Esperamos a que un cliente se conecte
    conn, addr = servidor.accept()
    print(f"Conexión establecida con: {addr}")

    data = conn.recv(1024).decode() # Recibimos los datos enviados por el cliente (máximo 1024 bytes)
    # Si no se recibe nada, se sale del bucle
    if not data:
        break

     # Dividimos la cadena recibida (por ejemplo: "5 + 3")
    partes = data.split()
    num1 = float(partes[0])   # Primer número
    operador = partes[1]      # Operador (+, -, *, /)
    num2 = float(partes[2])   # Segundo número


     # PROCESAMIENTO DE LA OPERACIÓN

    if operador == '+':
        resultado = num1 + num2
    elif operador == '-':
        resultado = num1 - num2
    elif operador == '*':
        resultado = num1 * num2
    elif operador == '/':
        # Evitar división por cero
        resultado = num1 / num2 if num2 != 0 else "Error: división por cero"
    else:
        resultado = "Operador inválido"

     # ENVÍO DEL RESULTADO AL CLIENTE

    conn.send(str(resultado).encode())
    print(f"Resultado enviado al cliente: {resultado}")
    conn.close()  # Cerramos la conexión con ese cliente
