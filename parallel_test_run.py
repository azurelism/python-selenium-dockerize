from subprocess import Popen


processes = []

for counter in range(1):
    chrome_cmd = 'python -m pytest --browser chrome'
    firefox_cmd = 'python -m pytest --browser firefox'
    processes.append(Popen(chrome_cmd, shell=True))
    processes.append(Popen(firefox_cmd, shell=True))

for counter in range(1):
    processes[counter].wait()