print("The greatest Converter greets you!")
print("Just input time in seconds and you will see the magic!")
time_in_sec = int(input("Do it here:"))
hours = time_in_sec / 3600
minutes = time_in_sec % 3600 / 60
seconds = time_in_sec % 3600 % 60
print(f"{hours:.0f}:{minutes:.0f}:{seconds:.0f}")
