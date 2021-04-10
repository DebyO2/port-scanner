#!/usr/bin/python3

#inbuilt modules
import socket
import os
from time import sleep

#external modules
import pyperclip
import keyboard
import pyautogui


time = 0

output = "a"

otp = []

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

	os.system("cls")
	while True:
		e = input("Command> ").lower()
		if e == "run":
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			see_settings()
			s.settimeout(time)
			
			host = input("Target IP: ")
			port_type = input("Port scan type: ")
			if port_type == "base":
				port = int(input("Target Port: "))

				def scan(port):

					global output

					if s.connect_ex((host, port)):
						print("port: closed")
						output = "port: closed"
					else:
						print("port: open" )
						output = "port: open"

				scan(port)
				
				print("press ctrl to copy")

				while True:
					if keyboard.is_pressed('ctrl'):
						
						pyperclip.copy(output)

						break

			elif port_type == "range":

				port = input("Port range: ").split("-")

				def scan(p1,p2):
					global otp

					for i in range(p1, p2+1):

						if s.connect_ex((host,i)):
							print(f"port {i}: closed" )
							otp.append(f"port {i}: closed")

						else:
							print(f"port {i}: open")
							otp.append(f"port {i}: open")

				scan(int(port[0]), int(port[1]))

				print("press ctrl to copy")

				while True:
					if keyboard.is_pressed('ctrl'):
						w = str(otp).replace("'","").replace("[","").replace("]","").replace(",","\n")
						pyperclip.copy(w)
						
						break
				
			else:
				print("#unknown scan type")

		elif e == "settings":
			see_settings()
			print("current settings >")
			print(f"       timeout = {time}")

		elif e == "change":
			change_settings()

		elif e == "exit":
			exit()

		elif e == "clear":
			os.system("cls")

		elif e == "help":
			print('''
  
1.run = run the scan
  
2.settings = change settings
	 ____|___________________________________
	|1.change = to change the timeout setting|
	 ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

3.exit = exit the tool

</> Types of port scans:
	
	<+> base : scans only on port
	<+> range : scans more than one port ; e.g/ 80-85


''')

		else:
			print("#unknown Command")

