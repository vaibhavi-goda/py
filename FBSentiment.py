import pandas as pd
import nltk
import xlrd
from nltk.sentiment.vader import SentimentIntensityAnalyzer
#nltk.downloader.download('vader_lexicon')
file='fbpostdata.xlsx'
xl=pd.ExcelFile(file) #Read from excel file
dfs=xl.parse(xl.sheet_names[0]) #parsing data
#dfs=list(dfs['Your Posts'])
print(dfs)
sid=SentimentIntensityAnalyzer()
str1="UTC+5:30"
for data in dfs:
    a=data.find(str1)
    if(a==-1):
          ss=sid.polarity_scores(data)
          print(data)
          for k in ss:
              print(k,ss[k])

                         
