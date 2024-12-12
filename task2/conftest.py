"""Created by Shikalovskyi Mykhailo IO-13"""
import paramiko
from subprocess import Popen, PIPE
import pytest
import socket


# Config
server_ip = '192.168.1.239'
username = ''
password = ''


@pytest.fixture(scope='function')
def server():
	client = paramiko.client.SSHClient()
	client.load_system_host_keys()
	try:
		client.connect(hostname=server_ip, username=username, password=password)
		assert client, "Client is empty"
		stdin, stdout, stderr = client.exec_command('iperf -s -t 10')
		error = stderr.read().decode('utf-8', errors='replace')
		
	except socket.gaierror:
		assert False, "SSH IP not found"
		exit(1)
	finally:
		client.close()

	return error if error else None


@pytest.fixture(scope='function')
def client(server):
	server_error = server
	command = ["iperf", "-c", server_ip, "-i", "1", "-t", "5"]
	proc = Popen(command, stdout=PIPE, stderr=PIPE)
	output, error = proc.communicate()
	return output, error, server_error

