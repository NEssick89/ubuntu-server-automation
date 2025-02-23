import subprocess

def get_uptime():
    uptime_result = subprocess.run(["uptime"], capture_output=True, text=True)
    return uptime_result.stdout.strip() 

def get_cpu_usage():
    cpu_result = subprocess.run(["mpstat"], capture_output=True, text=True)
    return cpu_result.stdout.strip()

def get_memory_usage():
    memory_usage = subprocess.run(["free",  "-h"], capture_output=True, text=True)
    return memory_usage.stdout.strip()

def get_disk_usage():
    disk_usage = subprocess.run(["df", "-h"], capture_output=True, text=True)
    return disk_usage.stdout.strip()

def get_top_process():
    top_process = subprocess.run("ps aux --sort=-%cpu | head -6", shell=True, capture_output=True, text=True)
    return top_process.stdout.strip()

if __name__ == "__main__":
    print("Uptime is:\n", get_uptime())
    print("CPU usage is:\n", get_cpu_usage())
    print("Memory usage is:\n", get_memory_usage())
    print("Disk usage is at:\n", get_disk_usage())
    print("Notable Process:\n", get_top_process())