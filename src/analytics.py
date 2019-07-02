from dataframe import dataFrame
import os.path
base = os.path.dirname(os.path.dirname(__file__))


class Analytics():
    def __init__(self, csvList):
        self.dictOfInputDataFrames = {}
        for file in csvList:
            self.dictOfInputDataFrames[file] = dataFrame(os.path.join(base, 'input', file))

    def productOrderAnalysis(self, outputCols):
        try:
            df_products = self.dictOfInputDataFrames['products.csv']
            df_orders = self.dictOfInputDataFrames['order_products.csv']
            #df_products.printFrame(10)
            #df_orders.printFrame(10)
        except KeyError:
            print("Failed to conduct analysis on products and orders. File not found!")
        
        print("Processing product + order analysis ... ")
        processDict = {}
        orders = df_orders['product_id']
        for index,val in enumerate(orders):
            reordered = int(df_orders['reordered'][index])
            departmentName = df_products['department_id'][df_products.getIndex('product_id', val)]    
            if departmentName in processDict:
                processDict[departmentName][0] += 1
                if reordered == 0: processDict[departmentName][1] += 1
            else:
                processDict[departmentName] = [1]
                if reordered == 0: processDict[departmentName].append(1)
                else: processDict[departmentName].append(0)
        
        resultDict = {}
        for col in outputCols:
            resultDict[col] = []
        
        sortedLst = sorted([ int(keyStr) for keyStr in list(processDict.keys())])       # get list of dict keys, int cast, then sort
        for key in sortedLst:
            resultDict['department_id'].append(key)
            resultDict['number_of_orders'].append(processDict[str(key)][0])
            resultDict['number_of_first_orders'].append(processDict[str(key)][1])     
            #print(key, processDict[str(key)])                                   
        
        a = resultDict['number_of_first_orders']
        b = resultDict['number_of_orders']
        resultDict['percentage'] = ['%.2f' % float(x/y) for x, y in zip(a, b)]
        #print(resultDict)

        print("Finished conducting analysis on products and orders.".format())
        return resultDict
