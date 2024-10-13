import csv

path = "src/vehicles_classification.csv"
DEBUG = True

def parse_vehicles():
    res_dict = {}

    with open(path, 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        for row in reader:
            row = ",".join(row)
            row = row.replace(" ", "")
            row = row.replace("\xa0", "")
            row = row.replace("\ufeff", "")
            row = row.split(";")

            res_dict[row[0]] = []
            for i in range(1,  len(row)):
                models = row[i]
                if len(models):
                    models = models.split(",")
                    for model in models:
                        res_dict[row[0]].append((i, model))
    
    if DEBUG:
        print_vehicles(res_dict)
    
    return res_dict


def print_vehicles(src):
    print("{")
    for key in src.keys():
        print(f"\t'{key}' : ")
        print("\t\t[")
        for item in src[key]:
            print(f"\t\t{item}")
        print("\t\t]")
    print("}")