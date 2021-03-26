import socket



if __name__ == '__main__':

	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	s.settimeout(5)
	host = input("Target IP: ")

	port = int(input("Target Port: "))

	def scan(port):

		if s.connect_ex((host, port)):
			print("port: closed")

		else:
			print("port: open" )

	scan(port)

