import paramiko

conn_params = paramiko.SSHClient()


conn_params.connect(
    hostname="172.20.100.1",
    username="imejia",
    password="rosario270984",
    )

conn = conn_params.ivoke_shell()

conn.send("sh ip int brie/n")

#we need to wait for response

output = conn.recv(65535)


