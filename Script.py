import socket

hostname = input('Website address (URL): ')

try:
    print(f'IP address: {socket.gethostbyname(hostname)}')
except socket.gaierror as error:
    print(f'[!] Invalid hostname! Error: {error}')
