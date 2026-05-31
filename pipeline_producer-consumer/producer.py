import zmq
import random
import pickle
import time

def producer():
    context = zmq.Context()
    socket = context.socket(zmq.PUSH)
    socket.connect("tcp://3.227.138.6:5678") # Aponta para o Servidor

    for _ in range(10):
        x = random.randint(1, 100)
        print(f"[Produtor] Gerou valor base X = {x}")
        socket.send(pickle.dumps({"x": x}))
        time.sleep(1)

if __name__ == "__main__":
    producer()
