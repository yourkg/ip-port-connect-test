import socket

ip="154.202.50.12"
ip=input("ip:")

#conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#conn.settimeout(3)
kg=[]
for port in range(65535):
  try:
    conn=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    conn.settimeout(1)
    conn.connect((ip,port))
    print('{} {}  is ok'.format(ip,port))
    conn.close()
    port=str(port)
    print(port,"okk")
    kg.append(port)
  except Exception as e:
    print('{} {} is unreachable'.format(ip,port))
print("开放的端口有：")
for i in kg:
  print(i)