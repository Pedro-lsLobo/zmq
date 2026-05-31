import zmq
import math
import pickle

def server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)
    socket.bind("tcp://*:5678")
    print("[Servidor] Pronto para receber requisições matemáticas na porta 5678...")

    while True:
        message = socket.recv()
        data = pickle.loads(message)
        
        if data == "STOP":
            socket.send(pickle.dumps("Servidor finalizado"))
            break
            
        num = data.get("numero")
        print(f"[Servidor] Processando o número: {num}")
        
        # Funcionalidade Matemática
        resposta = {
            "original": num,
            "quadrado": num ** 2,
            "cubo": num ** 3,
            "raiz_quadrada": round(math.sqrt(num), 4)
        }
        
        socket.send(pickle.dumps(resposta))

if __name__ == "__main__":
    server()
