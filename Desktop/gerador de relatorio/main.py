from functions import read_csvfile , calculate_totals , save_report

data = read_csvfile("sales_report.csv")
if not data:
    print("The file is empty")
    exit()

totals = calculate_totals(data)

save_report("sales_report.txt", totals)

print("Sales_report.txt generated succesfully")