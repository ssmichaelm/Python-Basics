import pandas as pd

class utility(object):

    def getVariance(fileList):
        lineCountList = []
        i = 0
        while i < 2:
            df = pd.read_csv(fileList[i])
            dimensions = df.shape
            lineCountList.append(dimensions[0])
            i += 1

        n = len(lineCountList)
        mean = sum(lineCountList) / n
        deviations = [(x - mean) ** 2 for x in lineCountList]
        variance = sum(deviations) / n
        return variance

    def getLogName(csvFile):
        index = csvFile.index('.')
        logName = csvFile[:index] + '_log.log'
        return logName

