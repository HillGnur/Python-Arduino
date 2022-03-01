import serial
from serial.tools import list_ports
import serial
from serial.tools import list_ports

#Conexão
conexao = ''
#Lista as portas do arduino
for port in list_ports.comports():
    print('Dispositivo {} conectado na porta {}'.format(port.description, port.device))
    #Verificar se há algum arduino nas portas
    if('ARDUINO' in port.description.upper()):
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
        #Leitura da resposta
        resposta = conexao.readline()
        print(float(resposta.decode()))
    #Encerramento da conexão
    conexao.close()