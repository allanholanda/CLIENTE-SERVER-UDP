import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Cria o bojeto de conexão

print("Cliente socket criado com sucesso!")

host = 'localhost'
port = 5433
mensagem = "HELLO SERVER!!"

try:
    print("Cliente: " + mensagem)
    s.sendto(mensagem.encode(), (host, 5432)) #Empacota mensagem e envia pro host na porta 5432 (porta que o servidor vai estar ouvindo)

    dados, servidor = s.recvfrom(4096) #Recebem do servidor uma resposta de 4096 bytes
    dados = dados.decode() #Desempacota os dados
    print("Cliente: " + dados) #Mostra os dados

finally:
    print('Cliente: Fechando a conexão') #Fecha a conexão para o programa não ficar em looping
    s.close()
