import re
from collections import Counter as count
import matplotlib.pyplot as plt

sentence = """ Aritificial Intelligence (AI) is changing the way we live and work.
AI helps in language teanslation, chatbot and data anlysis.
"""

to_lower_case = sentence.lower()
print(f"\nConverted to lower case:\n\n{to_lower_case}")

remove_pun= re.sub(r'[^\w\s+]', "", to_lower_case)
print(f"\nRemoved all puntations:\n\n{remove_pun}")

split_tokens = remove_pun.split()
print(f"\nSplitted into tokens:\n\n{split_tokens}")

frequency = count(split_tokens)
print(f"\nFrequency of words:\n\n{frequency}")

stop_word = ['and', 'is', 'the', 'in', 'we', 'of', 'chatbot','helps']
final = [i for i in split_tokens if i not in stop_word]
print(f"\nFiltered out some words:\n\n{final}")

final = count(final)
plt.bar(final.keys(), final.values(), color = "brown")

most_common = final.most_common(5)
print(f"\nMost commonc words: \n\n{most_common}")

word_list = [word for word, c in most_common]
cont_list = [c for word, c in most_common]



plt.show()