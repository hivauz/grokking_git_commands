import csv
with open("data.csv", "w+") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow( ["title", "description", 'col3'])
    writer.writerow(["row 1", "some desc", 'another'])
    writer.writerow( ["title", "description", 'col3'])
    writer.writerow( ["title", "description", 'col3'])

with open('data.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["data 3", "data 4"])

with open('data.csv', 'w') as csvfile:
    fieldnames = ['id', 'title']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)
    writer.writeheader()
    writer.writerow({"id": 2342, "title":"sldjkflsdjf"})
    writer.writerow({"id": 21162, "title":"s7777777777777"})
    
