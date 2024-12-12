"""Created by Shikalovskyi Mykhailo IO-13"""

from subprocess import Popen, PIPE
import re
import copy


server_ip = '192.168.1.239'


def parser(output, error):
	KEYS = ('Interval', 'Transfer', 'Bitrate')
	data_output = re.findall(r'\b([0-9\.\-]+)\s+sec\s+([0-9\.]+\s+[A-Z]?Bytes)\s+([0-9\.]+\s+[A-Z]?bits/sec)\b', output.decode("utf-8"))
	error = error.decode("utf-8")

	formatted_data_output = []
	temp = {}
	for data in data_output:
		temp.clear()
		for idx in range(len(KEYS)):
			temp[KEYS[idx]] = data[idx]

		formatted_data_output.append(copy.deepcopy(temp))

	return formatted_data_output, error if error else None


def client(server_ip):
	command = ["iperf", "-c"] + re.findall(r"\b(?:[1-2]?\d{1,2}\.){3}[1-2]?\d{1,2}\b", server_ip) + ["-i", "1", "-t", "5"]
	proc = Popen(command, stdout=PIPE, stderr=PIPE)
	output, error = proc.communicate()
	return output, error


def main():
	output, error = client(server_ip)
	p_output, p_error = parser(output, error)
	if p_error: 
		print(p_error)
	for line in p_output:
		print(line)


if __name__ == '__main__':
	main()
