import csv

csv_db = "db.csv"
# with open("db.csv", mode="r") as mock_db:
#     db_reader = csv.reader(mock_db, delimiter=":")
#     for row in db_reader:
#         print(row)

# database reader
# with open(csv_db, mode="r") as mock_db:
#     db_reader = csv.DictReader(mock_db, delimiter=":")
#     for row in db_reader:
#         print(row)

# database writer
with open("db.csv", mode="a") as mock_db:
    fieldnames = ["id", "name", "Profession"]
    db_writer = csv.DictWriter(mock_db, fieldnames=fieldnames, delimiter=":")
    db_writer.writerow({"id": "000", "name": "Helga", "Profession": "GoDev"})
