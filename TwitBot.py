import twint
import textwrap3

print("TwitBot Social Scrapper [Version 3.1.1] | (c) 2019 QuickBot Enterprises | All rights reserved. ")
print("\n")
c = twint.Config()
c.Search = input("Give me a topic, a hashtag or a person, and i'll get the tweets for you: ")
print("\n")

# Custom output format
c.Format = "\n Date: {date} |  Username: {username} | Tweet: {tweet} | Replies: {replies} | Retweets: {retweets} | Likes: {likes}  "
Format= "Date | Username | Tweet | Replies | Retweets | Likes "
list=textwrap3.wrap(Format, width=95)
for element in list:
    print(element)
#c.Custom["Date", "Username", "tweet"] = ["date", "username", "tweet"]
c.Store_csv = True
#c.Custom["Date", "Username", "tweet"] = ["date", "username", "tweet"]
c.Limit = 200
c.Output = "Feedback.csv"

twint.run.Search(c)





