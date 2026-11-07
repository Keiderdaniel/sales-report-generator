import csv

def read_csvfile(csv_file: str) -> list [dict]:
    try:
        with open(csv_file, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            data = []
            for l in reader:
                data.append(l)
        return data
    except FileNotFoundError:
        print(f'The file {csv_file} was not found')
        return []

def calculate_totals(data: list[dict]) -> dict:
    totals = {}
    for item in data:
        category = item["categoria"]
        try:
            value = float(item['valor'])
            if category in totals:
                totals[category] = totals[category] + value
            else: totals[category] = value
        except ValueError:
            print(f'Invalid error for: {item}')
            continue
    return totals

def save_report(txt_file: str, totals:dict) -> None:
    try:
        with open(txt_file, "w", encoding="utf-8") as f:
            f.write("SALES REPORT\n")            
            f.write("--------------")
            for category, value in totals.items():
                f.write(f'\n{category.title()}: R$  {value:.2f}\n')           
    except PermissionError:
        print("Permission Error")