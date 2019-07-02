# INSIGHT_Challenge
<br>

## Problem
Instacart has published a [dataset](https://www.instacart.com/datasets/grocery-shopping-2017) containing 3 million Instacart orders.  
**"For this challenge, we want you to calculate, for each department, the number of times a product was requested, number of times a product was requested for the first time and a ratio of those two numbers."**
<br>

## Summary
* The challenge forbade usages of libraries like pandas.
* As a result, I decided to create my own dataframe data structure.
* The dataStructure allows easy storage and quering of the .csv input files.
* Once I finished creating the data structure, the process of obtaining the analysis became trivial.
* I also wrote an analytics class to better organize the code.
* The class allows new analysis to be easily handled by simply adding the logic of the analysis as a function.
* The default analysis calculates the required percentage mentioned in challenge. This is then outputted into a .csv file.
* While I did some unit testing along the way, I have not added the incomplete unit tests to this repo as of now.
* I only had access to a Windows machine throughout the duration of the challenge.
* While the code should be OS independent, I am not 100% sure the shell script (run.sh) works.
<br>

## Instructions to execute program
* Use the run.sh to run the python script.
* If the shell script does not work, please navigate to the src directory and manually run the analytics_script.py script.
* The program will save the output as report.csv in the output directory.
* On average the program takes 15 minutes to complete the analysis on order_products.csv and products.csv
<br>

## Classes
### dataFrame
* The class can be initilized on a .csv file or a given dictionary:
<pre>
    class DataFrame():
        ...

    >> someDict = { 'a':[1,2], 'b':[3,4] }
    >> df_from_file = dataFrame('example.csv')
    >> df_from_dict = dataFrame(someDict)
</pre>
* The class has a dictionary member variable and its structure in relation to "table" in .csv:
<pre>
    df_eq = { 'col1' : [list, of, column, data],  
              'col2' : [list, of, column, data],  
               ...,  
            'coln-1' : [list, of, column, data],  
              'coln' : [list, of, column, data] }  
</pre>
* The dataFrame object has the []-operator defined as follows: 
<pre>
    def __getitem__(self, col):
        return self.df[col]

    >> someDict = { 'a':[1,2], 'b':[3,4] }
    >> df = dataFrame(someDict)
    >> print (df['a'])
    [1,2]    
</pre>
* To get the index of element x in a column:
<pre>
    def getIndex(self, col, x):
        return self.df[col].index(x)

    >> someDict = { 'a':[1,2,4,5], 'b':[3,4,9,4] }
    >> df = dataFrame(someDict)
    >> print (df.getIndex('a',4))
    2
</pre>
* To pretty-print the dataFrame:
<pre>
    def printFrame(self, rowLimit = -1):
        ...

    >> someDict = { 'a':[1,2,4,5], 'b':[3,4,9,4] }
    >> someDict.printFrame(2)
    a       b
    1       3
    2       4
    >> someDict.printFrame
    a       b
    1       3
    2       4
    4       9
    5       4
</pre>
* To save the dataFrame into a csv:
<pre>
    def toCsv(self, colOrder, fileName, delm = ','):
        ...
   
    >> someDict = { 'a':[1,2,4,5], 'b':[3,4,9,4] }
    >> colOrder = sorted(someDict.keys())
    >> df = dataFrame(someDict)
    >> df.toCsv(colOrder, fileName)
    Successfully saved output to file: fileName

</pre>
<br>

### Analytics
* Initilize the analytics class by passing a list of input files.
* Internally the class creates a dicitonary of dataFrames on fileName as key.
* To conduct analysis, first add the analysis process as a member function.
* Then call any pre-defined analysis.
<pre>
    def __init__(self, csvList):
        self.dictOfInputDataFrames = {}
        for file in csvList:
            self.dictOfInputDataFrames[file] = dataFrame(os.path.join(base, 'input', file))

    >> csvList = ['input1.csv','input2.csv']
    >> analyticsObj = Analytics(csvList)
    >> analysisDict = analyticsObj.productOrderAnalysis(outputCols)

</pre>
