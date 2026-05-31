import zmq
import pickle
import time

def client():
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    server_ip = "3.227.138.6"
    socket.connect(f"tcp://{server_ip}:5678")

    numeros_teste = [4, 9, 16, 25]

    for n in numeros_teste:
        print(f"[Cliente] Enviando número {n} para cálculo...")
        socket.send(pickle.dumps({"numero": n}))
        
        resultado = pickle.loads(socket.recv())
        print(f"[Resposta do Servidor]: {resultado}\n")
        time.sleep(1)

    socket.send(pickle.dumps("STOP"))
    socket.recv()

if __name__ == "__main__":
    client()
