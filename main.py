import requests
import os

str1 = """\033[91m
 _   _           _      ____ _               _
| | | | ___  ___| |_  \033[93m / ___| |__   ___  ___| | _____ _ __
| |_| |/ _ \/ __| __| | |   | '_ \ / _ \/ __| |/ / _ \ '__|
|  _  | (_) \__ \ |_  | |___| | | |  __/ (__|   <  __/ |
|_| |_|\___/|___/\__|  \____|_| |_|\___|\___|_|\_\___|_|
By : Mohamed Suleiman, MSA

\033[92mGithub : github.com/hamadax2
Facebook : facebook.com/king.hamada.sd

[+] Enrer CTRL+Z to exit
"""
os.system('clear')
print(str1)
while True:
	try:
		u = input('\033[91mEnter The host :: ')
		print('\033[94mWorking........')
		r = requests.get(f"https://{u}")
		date = r.headers.get('Date')
		content = r.headers.get('Content-Type')
		keep = r.headers.get('Keep-Alive')
		server = r.headers.get('Server')
		con = r.headers.get('Connection')
		Content_len = r.headers.get('Content-Length')
		Mime_ver = r.headers.get('Mime-Version')
		s = r.status_code
		print('Date : '+str(date)+'\n'+'Host : '+u+'\n'+'Status : '+str(s)+'\n'+'Server : '+str(server) +'\n'+'Mime-Version : '+str(Mime_ver)+'\n' +'Connection : '+str(con)+'\n'+'Keep-Alive : '+str(keep)+'\n'+'Content-Type : '+str(content)+'\n'+'Content-Length : '+str(Content_len)+'\n')
	except requests.exceptions.RequestException as e:
		print(e)

