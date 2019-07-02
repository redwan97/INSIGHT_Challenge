
from dataframe import dataFrame
from analytics import Analytics
import os.path

base = os.path.dirname(os.path.dirname(__file__))
print(base)

if __name__ == '__main__':
    outputFileName = 'report.csv'  
    outputCols = ['department_id', 'number_of_orders', 'number_of_first_orders', 'percentage']
    csvList = ['products.csv', 'order_products.csv']
    
    analyticsObj = Analytics(csvList)
    analysisDict = analyticsObj.productOrderAnalysis(outputCols)

    df_result = dataFrame(None, analysisDict)
    df_result.printFrame()
    df_result.toCsv(outputCols, outputFileName)
    
   
