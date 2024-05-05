import pandas as pd
import numpy as np
import nltk
import re
import seaborn as sns
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer 
from nltk.stem.porter import PorterStemmer
from collections import Counter

email_d = pd.read_csv("C:\\Users\\asus\\Masaüstü\\VeriMadenciliği\\mbox_modified.csv")

#Text Word startistics: min.mean, max and interquartile range
txt_length = email_d.body.str.split().str.len()
stats= txt_length.describe()

column_n=['subject','date','from','X-Gmail-Labels','body','is_spam']
text_f=['subject','body']
remove_c=['date','from','X-Gmail-Labels']

ps = PorterStemmer()
wnl = nltk.stem.WordNetLemmatizer()

stop_words = set(nltk.corpus.stopwords.words('english')) | set(nltk.corpus.stopwords.words('turkish'))

stopwords_dict = Counter(stop_words)

def remove_unused_c(df, column_n=remove_c):
    df = df.drop(column_n, axis=1)
    return df

def null_process(feature_df):
    for col in text_f:
        feature_df.loc[feature_df[col].isnull(), col] = "None"
    return feature_df

def clean_dataset(df):
    df=remove_unused_c(df)

    df = null_process(df)
    return df

def clean_text(text):
    #text = str(text).replace(r'http[\w:/\.]+', ' ')  # removing urls
    #text = str(text).replace(r'[^\.\w\s]', ' ')  # remove everything but characters and punctuation
    #text = str(text).replace('[^a-zA-Z]', ' ')
    #text = str(text).replace(r'\s\s+', ' ')
    #text = text.lower().strip() 
    text = re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' ', text)
    text = re.sub(r'[^\w\s]', ' ', text)
    text = re.sub(r'\s\s+', ' ', text)
    text = text.lower().strip() 
    return text

def nltk_preprocess(text):
    text = clean_text(text)
    wordlist = re.sub(r'[^\w\s]', '', text).split()
    #text = ' '.join([wnl.lemmatize(word) for word in wordlist if word not in stop_words])
    text = ' '.join([WordNetLemmatizer().lemmatize(word) for word in wordlist if word not in stop_words])
    return  text

# Combine cleaning functions
df = clean_dataset(email_d).apply(lambda x: x.apply(nltk_preprocess) if x.name in text_f else x)

# Remove duplicates
df = df.drop_duplicates()

df.to_csv('latest.csv', index=False, encoding='utf-8')

#Display the first 5 rows of the body column
for index, row in df.head().iterrows():
    print(f"Email Body {index + 1}:\n{row['body']}\n{'='*50}\n")

# Display "is_spam" column if it's 1
#spam_rows = df[df['is_spam'] == 1]
#print(spam_rows)

ax=sns.countplot(x="is_spam", data=email_d)
plt.title("Distribution of 'is_spam' labels")
plt.xlabel("is_spam")
plt.ylabel("Percentage")

# Calculate percentages and annotate the plot
total = len(email_d)
for p in ax.patches:
    height = p.get_height()
    ax.text(p.get_x() + p.get_width() / 2., height + 3, f"{height/total:.2%}", ha="center")

# Show the plot
plt.show()





