rev = 0
exp = 0
rent_prof = 0
prof = 0
staff_prof = 0
staff = 0
rev = int(input("Please insert revenue: "))
exp = int(input("Please insert expenses: "))
if rev > exp:
    print("Good job! We have a profit this year!")
    prof = rev - exp
    rent_prof = (prof / rev) * 100
    staff = int(input("Please insert number of staff: "))
    staff_prof = prof // staff
    print("Profit of this year is", prof)
    print(f"Profitability is {rent_prof}%")
    print("Profit on staff is", staff_prof)
elif rev == exp:
    print("We have a zero")
else:
    print("Bad news, we have a loss")
