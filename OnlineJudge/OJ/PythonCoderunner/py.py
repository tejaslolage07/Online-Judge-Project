import subprocess
subprocess.run(["docker", "stop", "cpp-container"], shell=True)
print("Hello world",end='')