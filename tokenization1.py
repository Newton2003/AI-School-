import re
import matplotlib.pyplot as plt
from collections import Counter as co

"""
class Exercise : starting off with the basics of LLM 

- convert to lower case
- remove all puntuations
- split into individual work tokens
- find the most frequent token using the counter funtion from collection
- filter out some of the individual word token from the a list called stopword ("which are words you dont want in your final list tokens")
- find the most common words
- plot using the bar chart from matplotlib

"""


text = """Aritificial Intelligence (AI) is changing the way we live and work.
AI helps in language teanslation, chatbot and data anlysis."""

conv_lower = text.lower()
print(conv_lower)
pun_re= re.sub(r'[^\w\s]',"", conv_lower)
print(pun_re)
spilt = pun_re.split()
print(spilt)

freq= co(spilt)
print(freq)

stopword = ['and', 'is', 'the', 'in', 'we', 'of', 'chatbot','helps']
final = [i for i in text if i not in stopword]

    
most_com = freq.most_common(5)
words = [w for w,c in most_com]
counts = [c for w, c in most_com]
 
#plt.bar(freq.keys(), freq.values(), color = "blue")
plt.bar(words, counts)
plt.title("top 5 words in text")

print(final)
plt.show()