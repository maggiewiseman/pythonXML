import csv

def invoke():
    with open('movies.csv') as csvfile:
        myreader = csv.reader(csvfile, delimiter=',')
        for row in myreader:
            print '!'.join(row)


def makeXML():
    f = open('movies.csv')
    csv_f = csv.reader(f)
    data = []

    for row in csv_f:
        data.append(row)
    f.close()

    print data[1:]
    # loop through data
    # convert_row

def convert_row(row):
    return """<movietitle="%s">
    <type>%s</type>
    <format>%s</format>
    <year>%s</year>
    <rating>%s</rating>
    <stars>%s</stars>
    <description>%s</description>
</movie>"""%(row[0], row[1], row[2], row[3], row[4], row[5], row[6])

print '\n'.join([convert_row(row) for row in data[1:]])