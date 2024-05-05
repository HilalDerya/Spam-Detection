# Spam-Detection

This project is an ML classification project where I classify e-mail data from Google as spam and non-spam.

I tried to get the best classification result with 5 different transformers using BERT, DistilBert, ALBERT, RoBERTa and XLNet.

The first thing I did was to find out what information Google keeps about e-mails, and I took the headers that were important to me and used them as features:
+ X-GM-THRID
+ X-Gmail-Labels
+ Delivered-To
+ Received
+ X-Google-Smtp-Source
+ X-Received
+ ARC-Seal
+ ARC-Message-Signature
+ ARC-Authentication-Results
+ Return-Path
+ Received
+ Received-SPF
+ Authentication-Results
+ Received
+ DKIM-Signature
+ DomainKey-Signature
+ MIME-Version
+ Date
+ Message-ID
+ Content-Type
+ Content-Transfer-Encoding
+ X-Priority
+ Subject
+ To
+ From
+ Reply-To
+ X-EMID
+ X-EM-SYSTEM
+ X-EM-CAMP
+ X-EM-CUSTOMER
+ X-EM-MEMBER
+ X-EM-TYPE
+ Return-Path
+ X-CSA-Complaints
+ List-Id
+ List-Unsubscribe
+ List-Unsubscribe-Post

After the headers, I prepared the labels of the e-mails and did preprocessing.

Since my data set is unbalanced, in some transformers I did undersampling in the majority class and oversampling in the minorty class.

I extracted ROC Curve, confusion matrix, training and evaluation loss graphs of the project after training. 
Graphs of the BERT transformer:
![bertConfusionMatrix](https://github.com/HilalDerya/Spam-Detection/assets/69717650/ff7fbfcd-ebd5-4139-8037-f64180a3403b)
![bertLoss](https://github.com/HilalDerya/Spam-Detection/assets/69717650/043201cb-33a0-4809-b38e-3b8e6393a711)
![bertROC](https://github.com/HilalDerya/Spam-Detection/assets/69717650/9e3d2856-5baf-40c0-84e5-3b3cc81650d1)

# Python Libraries I Used

+ mailbox
+ pandas
+ numpy
+ nltk
+ seaborn
+ matplotlib.pyplot for graphs
+ nltk.corpus for stopwords
+ nltk.stem for lemmatizer and stemmer
+ imblearn.over_sampling for SMOTE
