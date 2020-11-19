import json
with open("text_7.txt", "r", encoding="utf-8") as file_obj:
    firms = {}
    lines = file_obj.readlines()
    average = {}
    total = []
    for line in lines:
        data = line.split()
        proceed = [int(i) for i in data if i.isdigit()]
        expen = [int(j) for j in data if j.isdigit()]
        firms[data[0]] = proceed[0] - expen[1]
        firm_sum = [sum(list(values for values in map(int, firms.values()) if values >= 0))]
        firm_count = [len(list(values for values in map(int, firms.values()) if values >= 0))]
        average["Average is"] = firm_sum[0] / firm_count[0]
    total.append(firms)
    total.append(average)
with open("text_77.json", "w", encoding="utf-8") as write_f:
    json.dump(total, write_f, ensure_ascii=False, sort_keys=True, indent=4)
