import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Criamos o objeto de condxão

print("Socket criado com sucesso!")

host = 'localhost'
port = 5432

s.bind((host, port))  #Fazer uma ligação apartir do host e da porta
mensagem = '\nServidor: HELLO CLIENT!'

while 1: #Enquanto o bindo for true:
    dados, end = s.recvfrom(4096) #Vai receber 4096 bytes

    if dados: #Se em dados tiver alguma coisa o servidor vai printar
        print('Servidor enviando mensagem... ')
        s.sendto(dados + (mensagem.encode()), end)