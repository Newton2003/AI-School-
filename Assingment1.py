import re
from collections import Counter as count
import matplotlib.pyplot as plt

text = """
Artificial Intelligence (AI) is no longer a futuristic concept—it's here, and it’s changing the world faster than we expected!
From voice assistants like Alexa and Siri, to recommendation systems on Netflix and YouTube, AI quietly powers much of our daily digital experience.
   However, as AI continues to grow, questions about ethics, fairness, and privacy are becoming louder. For instance, how do we ensure that AI systems make decisions that are transparent and unbiased?
   
Many organizations have started to use machine learning (ML) to predict customer behavior, detect fraud, and even diagnose diseases.
But not all AI systems are perfect—some models may make mistakes, especially when trained on poor-quality data. 
That’s why data preprocessing, cleaning, and normalization are essential steps before any AI model is built. 

  In addition, researchers now talk about “Explainable AI” (XAI), which focuses on making AI decisions understandable to humans. 
This is particularly important in sensitive areas such as healthcare, education, and criminal justice, where wrong decisions can have serious consequences. 

Interestingly, AI is not just about coding or mathematics—it’s also about human values, social responsibility, and understanding language. 
Natural Language Processing (NLP), for example, helps computers understand human text and speech, enabling chatbots, language translation, and sentiment analysis. 

Overall, the success of AI depends on how responsibly we collect, process, and interpret data. 
As future data scientists and software engineers, your role is to build AI systems that are accurate, ethical, and human-centered. 
"""

text_lowerCase = text.lower()

rem_puntations = re.sub(r'[^\d\s+\w\s]', "",text_lowerCase).strip()

word = rem_puntations.split()
sentence = text.lower().split('.')

print(f"number of word tokens:{len(word)}")
print(f"number of sentence tokens:{len(sentence)}")

before_tokens = len(text.split())
after_tokens = len(word)

print("\ntokens before the cleaning:", before_tokens)
print("tokens of sentence after the cleaning: ", after_tokens)

stopwords = ['and', 'is', 'the', 'to', 'of', 'a', 'in', 'on', 'for', 'as', 'are', 'that', 'be', 'it', 'this'] 

filtered_tokens = [i for i in word if i not in stopwords]

print("\n\nThese are the filtered tokens: \n\n", filtered_tokens)

normalization = [i.rstrip('s') for i in filtered_tokens]
print("\n\nremoved all words ending with 's' : \n\n", normalization)

freq = count(normalization)
top_ten = freq.most_common(10)

print("\n\nThese are the most frequent words:\n\n")
for i, count in top_ten:
 print(i, ":", count)
#the frequency centers around ai etchics

words,num = zip(*top_ten)
plt.bar(words,num, color = "blue")
plt.title("Top 10 most frequent words")
plt.xlabel("words")
plt.ylabel("frequency")
plt.xticks(rotation = 49)
plt.show()



# Task 7 — Reflection Questions

# a. Which preprocessing steps changed your token list the most?
# ➡ Removing stopwords and punctuation had the biggest impact — it reduced filler words and cleaned the text.

# b. Why is cleaning and normalization important before training an AI model?
# ➡ It removes noise, standardizes inputs, and ensures consistent patterns for better model performance and accuracy.

# c. What insights do the most frequent words reveal about the theme of the text?
# ➡ The frequent terms (like ai, data, system, decision, human, ethics) highlight the text’s focus on responsible AI and data-driven decision-making.

# d. How could you further improve this text preprocessing pipeline?
# ➡ Add:

# Lemmatization (e.g., using spaCy)

# More comprehensive stopword list

# POS tagging to filter by nouns/adjectives

# Named entity recognition (NER)

# TF-IDF weighting for more meaningful importance