import platform

print("=== System Information Report ===")
print(f"Operating System: {platform.system()} {platform.release()}")
print(f"OS Version: {platform.version()}")
print(f"Platform: {platform.platform()}")
print(f"Machine Architecture: {platform.machine()}")
print(f"Processor: {platform.processor()}")
print("---")
print(f"Hostname: {platform.node()}")
print("---")
print(f"Python Implementation: {platform.python_implementation()}")
print(f"Python Version: {platform.python_version()}")