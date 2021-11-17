import string
import datetime
import logging

months = ("jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec")

class date_class(object):

    ' This method parses through the provided user file string for a month and year '
    ' Returns a dictionary of a month and a year                                    '
    def findDate(userfile):
        monthYear = {}

        for month in months:
            if month in userfile.lower():
                monthYear["Month"] = month
                break

        # Strip the string of punctuation and letters, leaving only the digits; then typecast to int
        year = userfile.replace('_', '').replace('.', '').strip(string.ascii_letters)
        monthYear["Year"] = int(year)

        return monthYear

    ' This method receives a provided dictionary, monthYear                        '
    ' Returns a corresponding datetime object, with the day set to 1               '
    def setDate(monthYear):
        filedate = datetime.datetime(monthYear["Year"], months.index(monthYear["Month"])+1, 1)
        return filedate

    ' This method receives a datetimeobject, cellDate, and replaces the day attribute with 1 '
    ' and 0 for hour, minute, and second.                                                    '
    ' This is so we can compare only the month and years                                     '
    def truncDate(cellDate):
        logging.info("Datetime object truncated for comparison.")
        return cellDate.replace(day=1, hour=0, minute=0, second=0)

    ' This method receives a string of a month and the program filedate '
    ' Returns a datetime object of that month and the filedate year     '
    def fillDate(monthYear_string, filedate):
        for i, month in enumerate(months):
            if month in monthYear_string.lower():
                newdate = datetime.datetime(filedate.year, i+1, 1)
                break

        logging.info("Datetime object created from string value in cell.")
        return newdate