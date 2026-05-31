import zmq
import time

def client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)  # Cria o socket de requisição (Request)

    # Conecta ao IP público do seu servidor na porta permitida
    server_ip = "3.227.138.6"
    socket.connect(f"tcp://{server_ip}:5678")
    print(f"Conectado ao servidor {server_ip}:5678")

    # Enviando algumas mensagens para testar a nova funcionalidade
    mensagens = ["Hello world", "Sistemas Distribuidos", "ZeroMQ na AWS"]

    for msg in mensagens:
        print(f"Enviando: {msg}")
        socket.send(msg.encode())
        
        reply = socket.recv()
        print(f"Resposta do Servidor: {reply.decode()}\n")
        time.sleep(1)

    # Envia o comando para parar o servidor
    print("Enviando comando STOP...")
    socket.send(b"STOP")
    reply = socket.recv()
    print(f"Resposta final: {reply.decode()}")

if __name__ == "__main__":
    client()
