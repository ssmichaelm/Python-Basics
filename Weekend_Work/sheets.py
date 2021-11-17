import logging
import datetime
import Utility

class sheets_class(object):
    def summaryRolling(o_sheet, filedate):
        logging.info("Parsing through the file. Logging the \"Summary Rolling MoM\" sheet now.")

        dateEqualizer = Utility.date_class
        summKeys = ("Calls Offered", "Abandon after 30s", "FCR", "DSAT", "CSAT")
        monthDictSumm = {}
        
        # Locate the row that the month-year, and subsequently the values we need, are in
        monthRow = 0
        for i in range(1, o_sheet.max_row + 1):
            if isinstance(o_sheet.cell(i,1).value, datetime.datetime):
                if filedate == dateEqualizer.truncDate(o_sheet.cell(i,1).value):
                    monthRow = i
                    logging.info("Row with the correct month located.")
                    break
            if isinstance(o_sheet.cell(i,1).value, str):
                if filedate == Utility.date_class.fillDate(o_sheet.cell(i,1).value, filedate):
                    monthRow = i
                    break

        # Iterate through the columns. Store the values appropriately
        for j in range(1, o_sheet.max_column + 1):
            if o_sheet.cell(1,j).value.__str__().replace(" ", "").lower() in [key.replace(" ", "").lower() for key in summKeys]:
                monthDictSumm[o_sheet.cell(1,j).value.__str__().strip()] = o_sheet.cell(monthRow, j).value
                logging.info(f"{o_sheet.cell(1,j).value.__str__().strip()} filled.")

        logging.info("Parsing done. Logging for the sheet finished.")
        return monthDictSumm

    def VOCRolling(o_sheet, filedate):
        logging.info("Parsing through the file. Logging the \"VOC Rolling MoM\" sheet now.")

        dateEqualizer = Utility.date_class
        VOCKeys = ("Base Size", "Promoters (Recommend Score 9 to 10)", "Passives (Recommend Score 7 to 8)", "Dectractors (Recommend Score 0 to 6)", 
                   "Overall NPS %", "Sat with Agent %", "DSat with Agent %")
        monthDictVOC = {}

        # Locate the column our month-year, and subsequently the values we need
        monthColumn = 0
        for j in range(1, o_sheet.max_column + 1):
            if isinstance(o_sheet.cell(1,j).value, datetime.datetime):
                if filedate == dateEqualizer.truncDate(o_sheet.cell(1,j).value):
                    monthColumn = j
                    break
            if isinstance(o_sheet.cell(1,j).value, str):
                if filedate == Utility.date_class.fillDate(o_sheet.cell(1,j).value, filedate):
                    monthColumn = j
                    break

        logging.info("Column with the correct month located.")

        # Iterate through the rows, storing the values appropriately
        for i in range(1, o_sheet.max_row + 1):
            if o_sheet.cell(i,1).value.__str__().replace(" ", "").lower() in [key.replace(" ", "").lower() for key in VOCKeys]:
                if "%" in o_sheet.cell(i,1).value:
                    monthDictVOC[o_sheet.cell(i,1).value] = o_sheet.cell(i+1, monthColumn).value
                else:
                    if "promoters" in o_sheet.cell(i,1).value.__str__().lower():
                        monthDictVOC["Promoters"] = 'Good' if o_sheet.cell(i, monthColumn).value > 200 else 'Bad'
                    elif "passives" in o_sheet.cell(i,1).value.__str__().lower():
                        monthDictVOC["Passives"] = 'Good' if o_sheet.cell(i, monthColumn).value > 100 else 'Bad'
                    elif "dectractors" in o_sheet.cell(i,1).value.__str__().lower():
                        monthDictVOC["Detractors"] = 'Good' if o_sheet.cell(i, monthColumn).value > 100 else 'Bad'
                    else:
                        monthDictVOC[o_sheet.cell(i,1).value] = o_sheet.cell(i, monthColumn).value
                logging.info(f"{o_sheet.cell(i,1).value.__str__().strip()} filled.")

        logging.info("Parsing done. Logging for the sheet finished.")
        return monthDictVOC