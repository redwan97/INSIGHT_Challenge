# INSIGHT_Challenge

## Problem
Instacart has published a [dataset](https://www.instacart.com/datasets/grocery-shopping-2017) containing 3 million Instacart orders.  
**"For this challenge, we want you to calculate, for each department, the number of times a product was requested, number of times a product was requested for the first time and a ratio of those two numbers."**


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

## Instructions to execute program
* Use the run.sh to run the python script.
* If the shell script does not work, please navigate to the src directory and manually run the analytics_script.py script.
* The program will save the output as report.csv in the output directory.
* On average the program takes 15 minutes to complete the analysis on order_products.csv and products.csv

## Classes
### dataFrame
* The class can be initilized on a .csv file or a given dictionary
* The structure of the dictionary 
    df_eq = {'col1' : [list, of, column, data],
             'col2' : [list, of, column, data],
              ...,
           'coln-1' : [list, of, column, data],
             'coln' : [list, of, column, data]}
* 