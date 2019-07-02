
from dataframe import dataFrame
from analytics import Analytics
import os.path

base = os.path.dirname(os.path.dirname(__file__))
print(base)

def main():
    outputCol = ['department_id', 'number_of_orders', 'number_of_first_orders', 'percentage']
    csvList = ['products.csv', 'order_products.csv']
    analysis1 = Analytics(csvList)
    resultDict = analysis1.productOrderAnalysis(outputCol)
      
    df_result = dataFrame(None, resultDict)
    #df_result.printFrame()

    keys = resultDict.keys()
    outputFileName = 'report.csv'
    df_result.frameToCsv(outputCol, keys, outputFileName)
   
main()