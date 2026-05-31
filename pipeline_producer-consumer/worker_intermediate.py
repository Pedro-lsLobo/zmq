import zmq
import pickle

def intermediate():
    context = zmq.Context()
    receiver = context.socket(zmq.PULL)
    receiver.bind("tcp://*:5678") # Recebe do Produtor

    sender = context.socket(zmq.PUSH)
    sender.bind("tcp://*:5679") # Envia para o Consumidor Final

    print("[Intermediário] Aguardando dados para multiplicar por 3...")

    while True:
        data = pickle.loads(receiver.recv())
        x = data["x"]
        y = x * 3
        print(f"[Intermediário] Recebeu X={x} | Calculou Y = {x} * 3 = {y}")
        
        sender.send(pickle.dumps({"x": x, "y": y}))

if __name__ == "__main__":
    intermediate()
