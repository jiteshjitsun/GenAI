device_status = input("Input device status ").lower()

if device_status == "active":
    temperature = input("Input temp ")
    if temperature > 35:
        print("High Temp")
    else:
        print("Normal Temp")
else:
    print("Device is offline")