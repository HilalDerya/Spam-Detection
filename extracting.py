import mailbox
import pandas as pd
import email.header
import re
import csv
from bs4 import BeautifulSoup
import email

mb = mailbox.mbox('C:\\Users\\asus\\Masaüstü\\Takeout\\Posta\\new_sample.mbox')

#Keys that Google keeps track of ---> go to headers_of_emails.py
#for key in mbox[0].keys():
#    print(key)

# Function to decode encoded words in headers
def decode_header(header):
    try:
        decoded_header = email.header.decode_header(header)
        decoded_text = ' '.join(text.decode(encoding or 'utf-8', errors='ignore') if isinstance (text, bytes) else text for text, encoding in decoded_header)
    except Exception as e:
        decoded_text = str(header)
    return decoded_text

def get_email_body(message): #getting plain text 'email body'
    # Extract the HTML body (if it exists)
    html_body = None
    for part in message.walk():
        content_type = part.get_content_type()
        if content_type == "text/html":
            try:
                payload = part.get_payload(decode=True)
                charset = part.get_content_charset() or 'utf-8'
                decoded_payload = payload.decode(charset)
                html_body = decoded_payload
            except Exception as e:
                # Handle any exceptions, e.g., print an error message
                print("Error while decoding email:", e)

    if html_body:
        # Parse the HTML content
        soup = BeautifulSoup(html_body, 'html.parser')

        # Remove HTML tags
        plain_text = soup.get_text()

        # Remove URLs (links)
        plain_text = re.sub(r'http\S+', '', plain_text)

        # Replace consecutive newline characters with a single newline
        plain_text = re.sub(r'\n+', '\n', plain_text)

        return plain_text

def get_email_address(string):
    email = re.findall(r'<(.+?)>', string)
    if not email:
        email = list(filter(lambda y: '@' in y, string.split()))
    return email[0] if email else None

# Open CSV file for writing
with open("mbox.csv", "w", encoding="utf-8", newline='') as outfile:
    writer = csv.writer(outfile)

    # Writing header
    writer.writerow(['subject', 'from', 'date', 'X-Gmail-Labels', 'body'])

    # Iterating through mbox and writing rows to CSV
    for message in mb.itervalues():
        dmessage = dict(message.items())
        message_data = [decode_header(dmessage.get(key, '')) for key in ['Subject', 'From', 'Date', 'X-Gmail-Labels']]
        message_data.append(get_email_body(message))
        writer.writerow(message_data)

messages = pd.read_csv("mbox.csv", encoding="utf-8")

# Extract only the email addresses from the "From" column
messages['from'] = messages['from'].apply(get_email_address)

# Extract the part before the second comma in 'X-Gmail-Labels'
messages['X-Gmail-Labels'] = messages['X-Gmail-Labels'].str.split(',', n=2).str[:2].str.join(',')

# Convert the 'Date' column to datetime
messages['date'] = pd.to_datetime(messages['date'], errors='coerce', utc=True)

# Add a new column "is_spam" based on the condition you specified
messages['is_spam'] = messages['X-Gmail-Labels'].str.contains('Spam', case=False, na=False).astype(int)

# Save the modified DataFrame back to CSV
messages.to_csv("mbox_modified.csv", encoding="utf-8", index=False)






