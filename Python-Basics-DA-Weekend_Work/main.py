
import os

import utility
import processor
import logging
from logging.handlers import RotatingFileHandler
import sys

# Store appropriate files in a list
fileList = []
for file in os.listdir(os.getcwd()):
    if "NYL" in file and file.endswith('.csv'):
        fileList.append(file)
fileList.sort(reverse=True) # Set the files in descending order, by date

u = utility.utility

# Open and retrieve names from 'NYL.lst' to see if file was already processed
with open("NYL.lst") as NYL:
    lines = [line.rstrip() for line in NYL]

try:
    # If the line count variance is over 500 or the file is already in 'NYL.lst', throw an error
    if u.getVariance(fileList) > 500:
        raise ValueError('Variance over 500 lines.')
    elif fileList[0] in lines:
        raise NameError('File already processed.')

except Exception as error:
    print('Caught this error: ' + repr(error))
    print('Exiting program.')

else:
    logging.basicConfig(handlers=[RotatingFileHandler(u.getLogName(fileList[0]), maxBytes=300000, backupCount=10)],
                        format='%(asctime)s - %(levelname)s: %(message)s',
                        level=logging.DEBUG)

    x = processor.processor(fileList[0])
    x.processFile()
    x.printDF()
    x.printN()
    x.printContract(fileList[0])
    x.plotDF()
    del x

    # Write the file name to NYL.lst
    with open("NYL.lst", "w") as NYL:
        NYL.write(fileList[0])

finally:
    sys.exit()