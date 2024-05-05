import mailbox
import pandas as pd
import email.header
import re

# Function to decode encoded words in headers
def decode_header(header):
    try:
        decoded_header = email.header.decode_header(header)
        decoded_text = ' '.join(text.decode(encoding or 'utf-8', errors='ignore') if isinstance(text, bytes) else text for text, encoding in decoded_header)
    except Exception as e:
        decoded_text = str(header)
    return decoded_text

def get_email_body(message):  # getting plain text 'email body'
    if message.is_multipart():
        for part in message.walk():
            if part.get_content_type() == 'text/plain':
                body = part.get_payload(decode=True).decode('utf-8')
                return body
    else:
        body = message.get_payload(decode=True).decode('utf-8')
        return body

def get_email_address(string):
    return string  # Return the string as is if it's already an email address

mb = mailbox.mbox('C:\\Users\\asus\\Masaüstü\\Takeout\\Posta\\sample.mbox')

keys = ['Subject', 'Date', 'From', 'X-Gmail-Labels']
message_list = []

for message in mb.values():
    dmessage = dict(message.items())
    message_list.append({key: decode_header(dmessage.get(key, '')) for key in keys})

messages = pd.DataFrame(message_list)

# Drop any extra columns not in the keys list
messages = messages[keys]

messages['From'] = messages['From'].apply(get_email_address)

messages['X-Gmail-Labels'] = messages['X-Gmail-Labels'].str.split(',', n=1).str[0]
messages.index = messages['Date'].apply(lambda x: pd.to_datetime(x, errors='coerce'))
messages.drop(['Date'], axis=1, inplace=True)

print(messages.shape)
print(messages.head(5))

