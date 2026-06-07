# Spam Detection with Transformer Models

A comparative NLP study that benchmarks 5 state-of-the-art transformer architectures for email spam classification — using real personal email data collected from Gmail.

## Overview

This project tackles email spam detection as a binary classification problem. Rather than relying on a standard benchmark dataset, the data was sourced directly from a personal Gmail account — making the challenge significantly more realistic and complex.

The core research question: **Which transformer model performs best on real-world, multilingual, imbalanced email data?**

Five transformer architectures were evaluated: BERT, DistilBERT, ALBERT, RoBERTa, and XLNet.

## Dataset

- **Source:** Personal Gmail account (real-world data)
- **Languages:** Mixed — Turkish and English
- **Challenge:** Imbalanced classes (non-spam significantly outnumbered spam)
- **Labeling:** Based on Gmail's spam/inbox classification

### Imbalance Handling
To address the class imbalance problem, depending on the transformer:
- **Undersampling** applied to the majority class
- **Oversampling** applied to the minority class (via **SMOTE**)

## Feature Engineering

One of the key contributions of this project is the use of **email header features** instead of (or alongside) raw email body text. Gmail stores rich metadata in email headers that are highly informative for spam detection:

<details>
<summary>Full list of extracted headers</summary>

- `X-GM-THRID`, `X-Gmail-Labels`
- `Delivered-To`, `Received`
- `X-Google-Smtp-Source`, `X-Received`
- `ARC-Seal`, `ARC-Message-Signature`, `ARC-Authentication-Results`
- `Return-Path`, `Received-SPF`
- `Authentication-Results`
- `DKIM-Signature`, `DomainKey-Signature`
- `MIME-Version`, `Date`, `Message-ID`
- `Content-Type`, `Content-Transfer-Encoding`
- `X-Priority`, `Subject`, `To`, `From`, `Reply-To`
- `X-EMID`, `X-EM-SYSTEM`, `X-EM-CAMP`, `X-EM-CUSTOMER`, `X-EM-MEMBER`, `X-EM-TYPE`
- `X-CSA-Complaints`
- `List-Id`, `List-Unsubscribe`, `List-Unsubscribe-Post`

</details>

## Models Compared

| Model | Description |
|---|---|
| **BERT** | Bidirectional Encoder Representations from Transformers (Google) |
| **DistilBERT** | Lightweight distilled version of BERT — faster, smaller |
| **ALBERT** | A Lite BERT — parameter-efficient architecture |
| **RoBERTa** | Robustly Optimized BERT — improved pretraining |
| **XLNet** | Autoregressive transformer — captures bidirectional context |

Each model was fine-tuned on the email dataset and evaluated with the same metrics for a fair comparison.

## Evaluation

For each model, the following were generated:

- **Confusion Matrix** — true vs. predicted spam/ham classifications
- **ROC Curve** — AUC score per model
- **Training & Validation Loss Curves** — convergence behavior across epochs

Sample outputs from the **BERT** model:

![bertConfusionMatrix](https://github.com/HilalDerya/Spam-Detection/assets/69717650/ff7fbfcd-ebd5-4139-8037-f64180a3403b)
![bertLoss](https://github.com/HilalDerya/Spam-Detection/assets/69717650/043201cb-33a0-4809-b38e-3b8e6393a711)
![bertROC](https://github.com/HilalDerya/Spam-Detection/assets/69717650/9e3d2856-5baf-40c0-84e5-3b3cc81650d1)

## Tech Stack

- **Language:** Python 3
- **NLP / ML:** `transformers` (Hugging Face), `torch`
- **Data Processing:** `pandas`, `numpy`, `nltk`
- **Imbalance Handling:** `imblearn` (SMOTE)
- **Visualization:** `matplotlib`, `seaborn`
- **Email Parsing:** `mailbox`
