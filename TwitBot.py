from win10toast import ToastNotifier
import time
from time import sleep
from datetime import datetime, date

import csv
# import SentimentIntensityAnalyzer class 
import twint
import textwrap3
# from vaderSentiment.vaderSentiment module. 
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

now = datetime.now()
toaster = ToastNotifier()

#POWERING TWINT
print("TwitBot [Version 3.1.1] | (c) 2019 QuickBot Enterprises | All rights reserved. ")
print("\n")

#Greet the user
User_Name=input("Name: ")
print("\n")
if now.hour == 1 or now.hour == 2 or now.hour == 3 or now.hour == 4 or now.hour == 5 or now.hour == 6 or now.hour == 7 or now.hour == 8 or now.hour == 9:
    print("Good morning", User_Name, "...")
elif now.hour==10 or now.hour == 11:
    print("Good morning", User_Name, "...")
elif now.hour==13 or now.hour == 12 or now.hour == 14 or now.hour == 15 or now.hour == 16:
    print("Good afternoon", User_Name, "...")
elif now.hour==17 or now.hour == 18 or now.hour == 19 or now.hour == 20 or now.hour == 21 or now.hour == 22 or now.hour == 23:
    print("Hey", User_Name, "going on overtime, eh?")

print("\n")
c = twint.Config()
c.Search = input(">> Give me a topic, a hashtag or a person, and i'll get the tweets for you: ")
print("\n")


# Custom output format
c.Format = "\n Date: {date} |  Username: {username} | Tweet: {tweet} | Replies: {replies} | Retweets: {retweets} | Likes: {likes}  "
Format= "Date | Username | Tweet | Replies | Retweets | Likes "

list=textwrap3.wrap(Format, width=95)
for element in list:
    print(element)
c.Store_csv = True
c.Limit = 5
c.Output = "Tweets.csv"
twint.run.Search(c)

toaster.show_toast("Tweet Fetch Complete",
                            "Starting Sentiment Analysis",
                            icon_path="Twit.ico",
                            duration=5)

# function to print sentiments 
# of the sentence. 
def sentiment_scores(sentence): 
  
    # Create a SentimentIntensityAnalyzer object. 
    sid_obj = SentimentIntensityAnalyzer() 
  
    # polarity_scores method of SentimentIntensityAnalyzer 
    # oject gives a sentiment dictionary. 
    # which contains pos, neg, neu, and compound scores. 
    sentiment_dict = sid_obj.polarity_scores(sentence) 
      
    print("Overall sentiment dictionary is : ", sentiment_dict) 
    print("sentence was rated as ", sentiment_dict['neg']*100, "% Negative") 
    print("sentence was rated as ", sentiment_dict['neu']*100, "% Neutral") 
    print("sentence was rated as ", sentiment_dict['pos']*100, "% Positive") 
  
    print("Sentence Overall Rated As", end = " ") 
  
    # decide sentiment as positive, negative and neutral 
    if sentiment_dict['compound'] >= 0.05 : 
        print("Positive") 
  
    elif sentiment_dict['compound'] <= - 0.05 : 
        print("Negative") 
  
    else : 
        print("Neutral")
    try:
        f = csv.writer(open('Tweet-Sentiment.csv', 'a', encoding='utf-8', errors='ignore'))
        f.writerow(['Tweet', "Compound", "Positive", "Negative", "Neutral"])
        Tweet=sentence
        Compound=sentiment_dict['compound']*100
        Positive= sentiment_dict['pos']*100
        Negative= sentiment_dict['neg']*100
        Neutral=sentiment_dict['neu']*100
        f.writerow([Tweet, Compound, Positive, Negative, Neutral])
    except Exception as e:
        print(e)
  
  
    
# Driver code 
if __name__ == "__main__" :
    infile = c.Output
    with open(infile, 'r', encoding='utf-8', errors='ignore') as csvfile:
        rows = csv.reader(csvfile)
        count=1
        for row in rows:
            sentence = row[10]
            print("\n", count, ")", sentence.translate(non_bmp_map))
            print(sentiment_scores(sentence) )
            count=count+1
            noneTypeCount = 0
  
            
