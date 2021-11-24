import pandas as pd
from pathlib import Path
import numpy as np
import validator
import logging
import matplotlib.pyplot as plt

class processor(object):
    def __init__(self, filecsv):
        self.df = pd.read_csv(filecsv,
                              usecols=['Agent Writing Contract Start Date',
                                       'Agent Writing Contract Status',
                                       'Agent Phone Number',
                                       'Agent State',
                                       'Agent Email Address'],
                              low_memory=True)

    def processColumn(self, key):
        v = validator.validator()
        for value in self.df[key]:
            # If the number, state, or email is not valid, log to file
            if v.options[key](value) == False:
                logging.info(f'{value} is not a valid {key}')
                index = self.df[self.df[key] == value].index[0]
                self.df[key][index] = np.nan


    def processFile(self):
        for key in self.df.keys():
            self.processColumn(key)

    def printDF(self):
        print(self.df.to_string())

    def printN(self):
        n = self.df.groupby('Agent State')['Agent Writing Contract Status'].count()
        print(n)

    def printContract(self, filecsv):
        contractDf = pd.read_csv(filecsv, usecols=['Agent First Name',
                                           'Agent Middle Name',
                                           'Agent Last Name',
                                           'Date when an agent became A2O',
                                           'Agent Writing Contract Start Date'])

        contractDf["Agent Full Name"] = contractDf["Agent First Name"].str.rstrip() + " " + contractDf["Agent Middle Name"].str.rstrip() + " " + contractDf["Agent Last Name"]
        contractDf.drop(['Agent First Name', 'Agent Middle Name', 'Agent Last Name'], axis=1, inplace=True)
        contractDf.set_index('Date when an agent became A2O', inplace=True, drop=True)
        print(contractDf.to_string())

    def plotDF(self):
        self.df['Agent State'].value_counts().plot(kind="bar", title="Number of agents per states")
        plt.xlabel('States')
        #self.df.groupby('Agent State')['Agent Writing Contract Status'].count().hist(by="Agent State")
        plt.show()

    def __del__(self):
        pass