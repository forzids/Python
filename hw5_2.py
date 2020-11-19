with open("test_hw5_2.txt", "r", encoding="utf-8") as file_obj:
    i = 1
    for line in file_obj:
        print(f"Length of {i} line is: {len(line)}")
        i += 1
with open("test_hw5_2.txt", "r", encoding="utf-8") as file_obj:
    line_count = sum(1 for line in file_obj)
    print(f"Count of lines is: {line_count}")
