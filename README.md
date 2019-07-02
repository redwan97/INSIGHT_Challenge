# INSIGHT_Challenge
## Summary

* The challenge forbade usages of libraries like pandas. As a result, I decided to create my own dataframe data structure so I could store and query the .csv input files. Once I finished creating the data structure, the remaining analysis became
trivial. I also wrote an analytics class to better organize the code. The class allows new analysis to be easily handled by simply adding the logic of the analysis as a function. The default analysis calculates the required percentage mentioned in challenge. This is then outputted into a .csv file.

* While I did some unit testing along the way, I have not added the incomplete unit tests to this repo as of now

* I only had access to a Windows machine throughout the duration of the challenge. While the code should be OS independent, I am not 100% sure the shell script (run.sh) works. If it does not, please navigate to the src folder and manually run the analytics_script.py script.
 