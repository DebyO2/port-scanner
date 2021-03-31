import socket
import os

time = 0

def change_settings():
		global time
		f =  open("Timesettings.txt","r+")

		time = int(input("Set timeout: "))
		f.write(f"TimeOut:{time}")

def see_settings():
	global time
	f = open("Timesettings.txt","r") 

	time = f.read().split(":")
	time = int(time[1])

if __name__ == '__main__':

	
	while True:
		e = input("Command> ")
		if e == "run":
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			see_settings()
			s.settimeout(time)
			
			host = input("Target IP: ")
			port_type = input("Port scan type: ")
			if port_type == "base":
				port = int(input("Target Port: "))

				def scan(port):

					if s.connect_ex((host, port)):
						print("port: closed")

					else:
						print("port: open" )

				scan(port)
				a = input()
				os.system("cls")

			elif port_type == "range":

				port = input("Port range: ").split("-")

				def scan(p1,p2):
					
					for i in range(p1, p2+1):

						if s.connect_ex((host,i)):
							print(f"port {i}: closed" )

						else:
							print(f"port {i}: open")

				scan(int(port[0]), int(port[1]))
				a = input()
				os.system("cls")

		elif e == "settings":
			see_settings()
			print("current settings >")
			print(f"       timeout = {time}")

			mr = input("Command> ")

			if mr == "change":
				change_settings()

			else:
				print("#unknown Command")
				print(mr)

