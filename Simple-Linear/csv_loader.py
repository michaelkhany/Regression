# importing csv module
import csv


def loadCSV_text(csv_file_path, rows2show):
    # csv file name
    if (csv_file_path.strip() != ''):
        filename = csv_file_path  # "aapl.csv"

        # initializing the titles and rows list
        fields = []
        rows = []

        # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

            # extracting each data row one by one
            for row in csvreader:
                rows.append(row)

            # get total number of rows
            result = ("Total no. of rows: %d" % (csvreader.line_num))

        # printing the field names
        result += ('Field names are:' + ', '.join(field for field in fields))

        #  printing first n rows
        result += ('\nFirst n rows are:\n')
        for row in rows[:rows2show]:
            # parsing each column of a row
            for col in row:
                result += ('\t'+col)  # ("%10s" % col),
            result += ('\n')

        return result
    else:
        return ''


def loadCSV_array(csv_file_path):
    # csv file name
    if (csv_file_path.strip() != ''):
        filename = csv_file_path  # "aapl.csv"

        # initializing the titles and rows list
        rows = []

        # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)
            data = list(csvreader)

        # data into list(multi dimension array)
        return data
    else:
        return ''


def get_CSVFieldNames_array(csv_file_path):
    # csv file name
    if (csv_file_path.strip() != ''):
        filename = csv_file_path  # "aapl.csv"

        # initializing the titles and rows list
        fields = []

        # reading csv file
        with open(filename, 'r') as csvfile:
            # creating a csv reader object
            csvreader = csv.reader(csvfile)

            # extracting field names through first row
            fields = next(csvreader)

        # printing the field names
        return fields
    else:
        return ''


def get_CSVrowsCount_int(csv_file_path):
    data =loadCSV_array(csv_file_path)
    if (data != ''):
        return len(data)
    else:
        return -1
