# Python program to generate WordCloud 
  
# importing all necessery modules 
from wordcloud import WordCloud, STOPWORDS 
import matplotlib.pyplot as plt 
import pandas as pd
from PIL import Image
import numpy as np
from os import path
  
# Reads 'Youtube04-Eminem.csv' file  
df = pd.read_csv(r"TelcosDominance.csv", encoding ="utf-8")

# read the mask image
# taken from
# http://publicdomainpictures.net
image=r"TwitBot.png"
scammer_mask = np.array(Image.open(image))
  
comment_words = ' '
stopwords = set(STOPWORDS)
stopwords.add("and")
  
# iterate through the csv file 
for val in df.Tweet: 
      
    # typecaste each val to string 
    val = str(val) 
  
    # split the value 
    tokens = val.split() 
      
    # Converts each token into lowercase 
    for i in range(len(tokens)): 
        tokens[i] = tokens[i].lower() 
          
    for words in tokens:
        comment_words = comment_words + words + ' '
  
  
wordcloud = WordCloud(width = 900, height = 800, 
                background_color ='white', 
                stopwords = stopwords,
                mask=scammer_mask,
                min_font_size = 10).generate(comment_words)

# generate word cloud
#wordcloud.generate(text)

# store to file
#wordcloud.to_file(path.join(d, "scammer.png"))
  
# plot the WordCloud image
plt.imshow(wordcloud, interpolation='bilinear')
plt.figure(figsize = (4, 4), facecolor = None) 
plt.imshow(scammer_mask, cmap=plt.cm.gray, interpolation='bilinear')#wordcloud) 
plt.axis("off") 
plt.tight_layout(pad = 0)   
plt.show()
