with open("text_3.txt", "r", encoding="utf-8") as file_obj:
    salary = []
    for lines in file_obj:
        lines = lines.split()
        if lines[1] <= '20000':
            print(f"Salary <= 20000 have: {lines[0]}")
        salary.append(float(lines[1]))

print(f"Average income is: {sum(map(float, salary)) / len(salary)}")
