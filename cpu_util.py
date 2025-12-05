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


cpu_values = []
memory_values = []
while any(p.poll() is None for p in deerflow):
    cpu_usage = sum(proc.cpu_percent(interval=None) for proc in ps_proc)
    print(f"CPU Usage: {cpu_usage}%", file = cpu_util_file)
    cpu_values.append(cpu_usage)
    memory_usage = sum(proc.memory_info().rss for proc in ps_proc) / (1024 * 1024)  # in MB
    print(f"Memory Usage: {memory_usage} MB", file = cpu_util_file)
    memory_values.append(memory_usage)
    time.sleep(1)
    

print(f"Average CPU Usage: {sum(cpu_values) / len(cpu_values)}%", file = cpu_util_file)
print(f"Maximum Memory Usage: {max(memory_values)} MB", file = cpu_util_file)