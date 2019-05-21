import nidaqmx

system = nidaqmx.system.System.local()
system.driver_version

for device in system.devices:
    print(device)
