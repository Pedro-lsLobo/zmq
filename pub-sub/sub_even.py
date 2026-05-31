import zmq
import pickle

def sub_even():
    context = zmq.Context()
    socket = context.socket(zmq.SUB)
    socket.connect("tcp://3.227.138.6:5678")
    socket.setsockopt_string(zmq.SUBSCRIBE, "PAR")

    print("[Peer 1] Inscrito no tópico PAR. Calculando somatório acumulado...")
    soma_total = 0

    while True:
        topico = socket.recv_string()
        num = pickle.loads(socket.recv())
        soma_total += num
        print(f"[{topico}] Recebido: {num} | Soma total dos pares ate agora = {soma_total}")

if __name__ == "__main__":
    sub_even()
