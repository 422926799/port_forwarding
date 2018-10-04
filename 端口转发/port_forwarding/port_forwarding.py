import socket
import threading

server_host='192.168.3.39'
server_port=4443

client_host='192.168.3.39'
client_port=3306
def log(logs):
    print('[+] log:',logs)


log('{}:{} -> {}:{}'.format(client_host,client_port,server_host,server_port))
def jianting(host,port,client_host,client_port):
    try:
        server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        server.bind((host,port))
        server.listen(5)

        ss,addr=server.accept()
        client.connect((client_host,client_port))
        while True:
            mg=ss.recv(5096)
            client.send(mg)
            log(mg)

            buf=client.recv(5096)
            ss.send(buf)
            log(buf)

    except Exception as error:
        print('[-]Error {}'.format(error))
        log('[-]Error {}'.format(error))
        exit()



def run():
    s=threading.Thread(target=jianting,args=(server_host,server_port,client_host,client_port))
    s.start()
if __name__ == '__main__':
    run()
