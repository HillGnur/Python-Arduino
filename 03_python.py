#-*- encoding : utf-8 -*-
import serial
from serial import list_ports

#Lista as portas do arduino
for port in list_ports.comports():
    print('Dispositivo {} conectado na porta {}'.format(port.description, port.device))
    #Verificar se há algum arduino nas portas
    if 'ARDUINO' in port.description.upper():
        #Tentar realizar a conexão
        try:
            conexao = serial.Serial(port.device, 115200)
            print('Conexão realizada com {}'.format(conexao.portstr))
        #Caso não consiga se conectar, ignorar
        except:
            pass
#Caso a conexão tenha sido realizada, a mesma será diferente de vazio ('')
if conexao != '':
    while True:
        print('Recebendo dados...')
        resposta = conexao.readline()
        valor = float(resposta.decode())
        print(valor)
        if valor < 700:
            conexao.write(b'1')
        else:
            conexao.write(b'0')

        conexao.close()
        print('Conexão encerrada')
else:
    print('Sem portas disponíveis')