import zmq
import pickle

def sub_odd():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://3.227.138.6:5678")
    socket.setsockopt_string(zmq.SUBSCRIBE, "IMPAR")

    print("[Peer 2] Inscrito no tópico IMPAR. Contando ocorrências...")
    qtd_impares = 0

    while True:
        topico = socket.recv_string()
        num = pickle.loads(socket.recv())
        qtd_impares += 1
        print(f"[{topico}] Recebido: {num} | Total de impares identificados = {qtd_impares}")

if __name__ == "__main__":
    sub_odd()
