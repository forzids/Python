days = 1
km = 0
req_km = 0
km = int(input("Please insert count of kms in first day: "))
req_km = int(input("Please insert count of required kms: "))
while km < req_km:
    a1 = km + ((km * 10) / 100)
    km = a1
    days = days + 1
    continue
if km >= req_km:
    print(f"Requested kms will be reached on day {days}")
