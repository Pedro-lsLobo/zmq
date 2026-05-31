import zmq
import pickle

def final_consumer():
    context = zmq.Context()
    socket = context.socket(zmq.PULL)
    socket.connect("tcp://3.227.138.6:5679") # Conecta no estágio 2

    print("[Consumidor Final] Aguardando dados para somar 7...")

    while True:
        data = pickle.loads(socket.recv())
        x = data["x"]
        y = data["y"]
        z = y + 7
        print(f"[Resultado Final] Equação concluída: f({x}) = ({x} * 3) + 7 = {z}")

if __name__ == "__main__":
    final_consumer()
