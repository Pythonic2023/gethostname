import socket

"""Use socket module to retrieve host name of specified IP address"""

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Creates IPv4 TCP socket.

result = socket.gethostbyaddr('IP_ADDR') # Returns 3-tuple list into result
print(result[0])