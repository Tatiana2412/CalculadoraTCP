# Calculadora Remota TCP

## Descripción
Este proyecto corresponde al trabajo práctico de la asignatura de Redes, cuyo objetivo es reforzar el entendimiento del protocolo TCP mediante la creación de una aplicación Cliente-Servidor.

La aplicación consiste en una calculadora remota, donde el cliente solicita dos operandos y una operación (+, -, *, /), y el servidor, utilizando sockets TCP, procesa la operación y devuelve el resultado.

Ambos programas están desarrollados en Python, ejecutándose en máquinas distintas dentro de la misma red local.

## Funcionamiento
1. El servidor escucha conexiones en el puerto 5000.
2. El cliente solicita al usuario dos números y una operación.
3. El cliente se conecta al servidor y le envía los datos.
4. El servidor procesa la operación y devuelve el resultado.
5. El cliente muestra el resultado y se cierra la conexión.

## Características principales:

Comunicación basada en protocolo TCP (SOCK_STREAM).
Cliente y servidor funcionales en sistemas Windows.
Intercambio confiable de mensajes (con confirmación ACK).
Compatible con capturas de análisis en Wireshark.

## Archivos incluidos:

calculadora_servidor.py: Servidor TCP que procesa operaciones matemáticas.
calculadora_cliente.py: Cliente TCP que solicita datos y muestra resultados.
README.txt: Instrucciones de ejecución y descripción del funcionamiento.
calculadora_remota.pcapng: Captura Wireshark de la comunicación TCP.
calculadora_remotaPuerto.pcapng: Captura Wireshark de la comunicación TCP con puerto.

## Ejecución
Servidor:
python calculadora_servidor.py

Cliente:
python calculadora_cliente.py

## Autores
- Yessica Tatiana Gualteros Ayala.
- Leidi Tatiana Nieto Goyeneche.

