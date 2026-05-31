import zmq
import random
import time
import pickle

def publisher():
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.bind("tcp://*:5678")
    print("[Publicador] Gerando números na porta 5678...")

    while True:
        num = random.randint(1, 50)
        topico = "PAR" if num % 2 == 0 else "IMPAR"
        
        print(f"[Publicador] Enviando para o tópico {topico}: {num}")
        # Enviamos o tópico como string e o número no payload
        socket.send_string(topico, zmq.SNDMORE)
        socket.send(pickle.dumps(num))
        
        time.sleep(1.5)

if __name__ == "__main__":
    publisher()
