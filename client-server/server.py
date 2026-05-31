import zmq

def server():
    context = zmq.Context()
    socket = context.socket(zmq.REP)  # Cria o socket de resposta (Reply)
    
    # Usando a porta 5678 que está liberada no seu intervalo da AWS
    socket.bind("tcp://*:5678")
    print("Servidor rodando e aguardando conexões na porta 5678...")

    while True:
        message = socket.recv()  # Aguarda a mensagem do cliente
        message_str = message.decode()
        
        if "STOP" in message_str:
            print("Comando STOP recebido. Encerrando servidor.")
            socket.send(b"Servidor finalizado")
            break
            
        # Nova funcionalidade: Retorna a string modificada + o tamanho dela
        print(f"Recebido: {message_str}")
        reply = f"{message_str}* (Tamanho: {len(message_str)})"
        
        socket.send(reply.encode())

if __name__ == "__main__":
    server()
