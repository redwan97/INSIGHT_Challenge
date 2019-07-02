import math
import csv
import os.path
base = os.path.dirname(os.path.dirname(__file__))

class dataFrame():
    def __init__(self, fileName = None, orginDict = None):
        if orginDict == None:
            self.df = {}
            with open(fileName, 'r', encoding = 'utf8') as readFile:
                firstLine = True
                for line in readFile:
                    if firstLine:
                        columns = line.strip('\n').split(',')
                        for col in columns:
                            self.df[col] = []
                        firstLine = False
                    else:
                        # Seperating columns on commas, need to be careful when commas are in strings (dont want to split string)
                        foundStart = False
                        start = 0
                        end = 0
                        
                        for index,char in enumerate(line):
                            if char == '"' and foundStart == False:
                                start = index
                                foundStart = True
                            if char == '"' and foundStart == True:
                                end = index

                        save = line[start:end+1]     
                        line = line[0:start] + save.replace(',','') + line[end +1:]
                        vals = line.strip('\n').split(',')

                        i = 0
                        for value in vals:
                            if '"' in value: value = save
                            self.df[columns[i]].append(value)
                            i+=1
            print("Finished creating dataFrame from: {}".format(fileName))
        else:
            self.df = orginDict
            print("Finished creating dataFrame from provided dictionary.")

    def __getitem__(self, col):
        return self.df[col]

    def getIndex(self, col, x):
        return self.df[col].index(x)

    def printFrame(self):
        print('\n\t\t\t*** Printing DataFrame ****')
        for col in self.df:
            print(col + '\t', end = '')
        print('')
        rows = len(next(iter(self.df.values())))  
        print(rows)    
        for row in range(rows):
            for col in self.df:
                val = self.df[col][row]
                col = str(col)
                val = str(val)
                if(len(val) < len(col)):
                    numTabs = math.ceil((len(col) - len(val)) / 4) 
                else:
                    sub = len(col) - 2
                    val = val[0:sub] + '...'
                    numTabs = 1
                print(val + numTabs*'\t', end = '')
            print('')
        print('')

    def frameToCsv(self, colOrder, keys , fileName, delm = ','):
        resultDict = self.df
        fileName = os.path.join(base, 'output', fileName)
        with open(fileName, 'w', newline='') as outfile:
            writer = csv.writer(outfile, delimiter = delm)
            writer.writerow(keys)
            
            rows = len(next(iter(resultDict.values())))  
            for listIndex in range(rows): 
                row = []
                for colIndex in range(len(colOrder)):
                    row.append(resultDict[colOrder[colIndex]][listIndex])
                writer.writerow(row)
        print('Successfully saved output to file: {}'.format(fileName))
