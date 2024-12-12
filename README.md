#QA Labs
Repository for QA labs. Made by Shikalovskyi IO-13

## Requirement
- Python3
- Pytest
- paramiko
- iperf2
- ssh server on Windows

## TASK 1
Main.py was created and has a client function to connect to iperf server and parser to parse iperf output data. Also it has parameter IP which must be filled correctly.

## TASK 2
Special program for testing iperf connection was created. Server is running on the other computer and starts up on PC which runs pytest via SSH connection. The main .py file is conftest, where all logic of server and client is written. There are some variables you must fill before running test: 
- IP
- username
- password. 

If you don't fill them, test will fail with appropriate server error. Also was created parser file and iperf_test file. The first one is used to parse output and errors and the second one is used to run pytest. 
It can check for: 
- server error 
- client error
- client data is good.

Also, after successfully running test, you can get output data from iperf.

