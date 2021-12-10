import pandas as pd
import numpy as np
import nltk
from nltk import pos_tag
# nltk.download()
from nltk import RegexpParser

with open("data/A.txt", encoding="latin-1") as f:
    lines = f.readlines()

# print(lines)
# print(len(lines))
# print(lines[1])

words = []

for i in range(len(lines)-1):
    lines[i].replace("."," .")
    lines[i].replace("\n", " \n")
    lines[i].strip('\n')
    # words.append(lines[i].split(" "))
    words.append(lines[i].split(" "))
# print(tokens_tag)

#adding tokens
tokens_tag = []
for word in words:
    tokens_tag.append((pos_tag(word)))

# print(tokens_tag)
# print(len(tokens_tag))
# print(tokens_tag[0][0][1])
tok_tag = []
for p in tokens_tag:
    for o in p:
        for u in p:
            tok_tag.append(u[1])

print(tok_tag)


a= []
for wo in words:
    np.transpose(wo)
    for w in wo:
        np.transpose(w)
        a.append(w)

df = pd.DataFrame(a, columns=['Word'])
df['Sentence #'] = ""
df['POS'] = ''
df['TAG'] = 'O'
# print (df)

indexs = df.index[df['Word'] == '.']
# print(indexs)


df['Sentence #'][0] = 'Sentence' + " " + str(1)
zlicz = 2
for i in indexs:
    df['Sentence #'].iloc[i+1] = 'Sentence' + " " + str(zlicz)
    zlicz = zlicz+1

for j in range(len(df['Word'])):
    df["POS"].iloc[j] = tok_tag[j]

# print(indexs[1:3])

# print(df['Sentence #'].iloc[48])
# print(df.iloc[77])
# print(df)

#
# data_frame = pd.DataFrame(index=[],columns=["Sentence #","Word","POS","Tag"])
# # print(data_frame)
#
# data_frame["Word"] = words
# print(data_frame)
searchfor = ['polyglutamine', 'glutamine-rich', 'polyQ', 'poly-Q', 'Q-rich', 'poly-glutamine', 'serines', 'serine-rich','arginine-serine','arginine-rich', 'proline-rich', 'adenine-rich', 'cysteine-rich', 'GC-rich', 'Gly-Pro-Ala-rich', 'G-rich', 'N-rich', 'Q/N-rich', 'glycine-rich', 'Thr-rich', 'asparagine-rich', 'proline/glycine-rich', 'PGR', 'lysine-rich', 'SR', 'methionine-rich', 'KAE-rich', 'Asparagine-rich', 'tryptophane-rich', 'histidine-rich', 'AT-rich' ]
df["TrueFalse"] = df['Word'].apply(lambda x: 1 if any(i in x for i in searchfor) else 0)
print(df)

indexs_2 = df.index[df['TrueFalse'] == 1]
print(indexs_2)

for m in indexs_2:
    df['TAG'].iloc[m] = 'LCR'

# print(df.iloc[669])


# df = df[['Sentence #', 'Word','POS','TAG']]
# df['Sentence #'].fillna(method="ffill")
# df.fillna(method="ffill")

# print(df.iloc[0-50])

# df['Sentence #'].fillna(method='bfill')
# print(df.isnull().sum()) # check numbers of null value in each column
# modifiedDf=df.fillna("NaN") #
# df[['Sentence #']].fillna(0, inplace=True)
df = df.replace(r'^\s*$', np.nan, regex=True)
df.fillna(method="ffill", inplace = True)
df = df[['Sentence #', 'Word','POS','TAG']]
print(df)

print(df['POS'].iloc[0:30])

# df.to_csv('file_name.csv', encoding="latin1")