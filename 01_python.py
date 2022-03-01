import serial
from serial.tools import list_ports

#Lista as portas do arduino
for port in list_ports.comports():
    print('Dispositivo {} conectado na porta {}'.format(port.description, port.device))
#Conexão
conexao = serial.Serial('COM3', 115200)#Serial usada no arquivo .ino #No linux, a porta muda de COM3 para /dev/ttyUSBN onde N pode assumir qualquer número relacionado ao USB em questão 
#Menu
acao = input('''
    Menu:
    
    [L] Ligar
    [D] Desligar
''').upper()
#Verificar se o usuário digitou corretamente a ação
while acao == 'L' or acao == 'D':
    #Verificar qual a ação digitada
    if acao == 'L':
        conexao.write(b'1')
    else:
        conexao.write(b'0')
    #Menu
    acao = input('''
        Menu:
        
        [L] Ligar
        [D] Desligar
    ''').upper()
#Encerra a conexão
conexao.close()
print('Conexão encerrada')