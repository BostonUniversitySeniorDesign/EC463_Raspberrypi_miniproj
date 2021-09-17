import bluetooth

# "lookup_names was added in order to return the name of the device in addition to the bluetooth address

disc_devs = bluetooth.discover_devices(duration=5, lookup_names=True) 
print(f"Found {len(disc_devs)} devices.")

for a, n in disc_devs:
    print(a, n)
