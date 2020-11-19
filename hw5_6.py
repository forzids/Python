with open("text_6.txt", "r", encoding="utf-8") as file_obj:
    lesson = {}
    lines = file_obj.readlines()
    for line in lines:
        data = line.replace('(', ' ').split()
        lesson[data[0][:-1]] = sum(int(i) for i in data if i.isdigit())
    print(lesson)
