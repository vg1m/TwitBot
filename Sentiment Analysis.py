import csv
from textblob import TextBlob
from textblob.sentiments import NaiveBayesAnalyzer
import sys
non_bmp_map = dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

infile = "Feedback.csv"

with open(infile, 'r', encoding='utf-8', errors='ignore') as csvfile:
    rows = csv.reader(csvfile)
    count=1
    for row in rows:
        sentence = row[10]
        blob=TextBlob(sentence)
        polarity= blob.sentiment.polarity
        subjectivity= blob.sentiment.subjectivity
        blob= TextBlob(sentence, analyzer = NaiveBayesAnalyzer())
        classification= blob.sentiment.classification
        positive= blob.sentiment.p_pos
        negative= blob.sentiment.p_neg
        
        print("\n")
        print (count, ")", sentence.translate(non_bmp_map))
        print("\n")
        print("***Mood Meter***")
        print("Positive: ", positive)
        print("Negative: ", negative)
        print("\n")
        if classification=="neg":
            print ("Bad feedback. ")
        if classification=="pos":
            print ("Good feedback. ")
        count=count+1
        noneTypeCount = 0
        try:
            f = csv.writer(open('TwitBot-Feelings.csv', 'a', encoding='utf-8', errors='ignore'))
            f.writerow(['Tweet', "Positive", "Negative"])
            Tweet=sentence
            Positive= positive
            Negative= negative
            f.writerow([Tweet, Positive, Negative])
        except Exception as e:
            print(e)
        
