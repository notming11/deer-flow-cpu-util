import psutil
import subprocess
import time

cpu_util_file = open("cpu_util.txt", "w")

deerflow = list()
for i in range(2):
    deerflow.append(subprocess.Popen(["uv", "run", "main.py", "Give a rigiorous mathematical proof of Ehrenfest Theorem."]))
    
for i in range(8):
    deerflow.append(subprocess.Popen(["uv", "run", "main.py", "search up the height of the effiel tower"]))


ps_proc = list()
for i in range(len(deerflow)):
    ps_proc.append(psutil.Process(deerflow[i].pid))


average_cpu_usage = 0
count = 0
while any(p.poll() is None for p in deerflow):
    cpu_usage = sum(proc.cpu_percent(interval=None) for proc in ps_proc)
    print(f"CPU Usage: {cpu_usage}%", file = cpu_util_file)
    average_cpu_usage += cpu_usage
    count += 1
    time.sleep(1)
    
average_cpu_usage /= count
print(f"Average CPU Usage: {average_cpu_usage}%", file = cpu_util_file)