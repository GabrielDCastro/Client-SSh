import paramiko

host = '127.0.0.1'
user = 'gabriel'
password = 'gabriel'

client = paramiko.SSHClient() #Criando cliente SSH
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())  #Uma política de conexão
client.connect(host, username=user, password=password)


while True:
    comando = input("Digite um comando do shell")
    stdin, stdout, stderr = client.exec_command(comando)
    print(stdout.readlines())
