import logging
import Utility
import sheets
import openpyxl
import os.path

logging.basicConfig(filename='logfile.log', filemode='a', format='%(asctime)s - %(levelname)s: %(message)s', datefmt='%d-%b-%y %H:%M:%S',
                            level=logging.DEBUG)

# Instantiate class objects
dc = Utility.date_class
s = sheets.sheets_class
logging.info(f"{'#' * 40}\nNew logging session.\n")

# Take user input and read file until file is valid (with a grabbable date)
while True:
    logging.info('Attempting to read file.')

    try:
        userfile = input("Enter a filename: ")
        if os.path.isfile(userfile):
            logging.info('File found!')
            grabbedDate = dc.findDate(userfile)
            logging.info(f"Month and year parsed from file.")
            break
    except:
        logging.info('Input invalid. Trying again.')
        print("Input is invalid. Please try again.")
    else:
        logging.info('Input file does not exist. Trying again.')
        print("File doesn't exist. Please try again.")

wb = openpyxl.load_workbook(filename=userfile) # Loads the existing file with openpyxl for reading capabilities
logging.info(f'File {userfile} correctly loaded.')

filedate = dc.setDate(grabbedDate) # Set date
logging.info('Datetime object created.')

# Summary Rolling MoM
o_sheet = wb["Summary Rolling MoM"]
monthDictSumm = s.summaryRolling(o_sheet, filedate) # Populate the dictionary, monthDictSumm, by invoking the class methods
#print(monthDictSumm)

# VOC Rolling MoM
o_sheet = wb["VOC Rolling MoM"]
monthDictVOC = s.VOCRolling(o_sheet, filedate) # Populate the dictionary, monthDictVOC
#print(monthDictVOC)

# Convert values to correct format
for key in monthDictSumm.keys():
    # The only value in monthDictSumm that isn't a percentage is the 'Calls Offered' one
    if "Calls Offered".lower() in key.lower():
        continue
    monthDictSumm[key] = monthDictSumm[key] * 100
    monthDictSumm[key] = "{0:.2f}".format(monthDictSumm[key]) + "%"

for key in monthDictVOC.keys():
    # The only values in monthDictVOC that are percentages
    if "%" in key:
        monthDictVOC[key] = monthDictVOC[key] * 100
        monthDictVOC[key] = "{0:.2f}".format(monthDictVOC[key]) + "%"

# Log and print information
f = '{0:<30}{1:<10}'
logging.info("\nSummary Rolling MoM data.")
print("\nSummary Rolling MoM data.")
for key, value in monthDictSumm.items():
    logging.info(f.format(key, value))
    print(f.format(key, value))

logging.info("\nVOC Rolling MoM data.")
print("\nVOC Rolling MoM data.")
for key, value in monthDictVOC.items():
    logging.info(f.format(key, value))
    print(f.format(key, value))

logging.info('\n\nLogging session ended.\n')