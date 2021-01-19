import csv

def getCSVdata(filename):

    rows = []
    datFile = open(filename, "r")
    reader = csv.reader(datFile)

    next(reader)
    for row in reader:
        rows.append(row)
    return rows
