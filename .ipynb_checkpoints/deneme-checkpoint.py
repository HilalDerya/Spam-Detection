import mailbox
import pandas as pd

# Specify the path to your .mbox file
mbox_file_path = 'C:\\Users\\asus\\Masaüstü\\Takeout\\Posta\\sample.mbox'

# Create an empty list to store email data
email_data = []

# Iterate through the emails in the .mbox file
for message in mailbox.mbox(mbox_file_path):
    email_subject = message['subject']
    email_from = message['from']
    email_date = message['date']
    email_body = message.get_payload()  # Get the email's body text

    # Append email data to the list
    email_data.append([email_subject, email_from, email_date, email_body])

# Create a Pandas DataFrame from the email data
df = pd.DataFrame(email_data, columns=['Subject', 'From', 'Date', 'Body'])

# Display the DataFrame
print(df.head(5)) 

# Optionally, you can save the DataFrame to a CSV file
# df.to_csv('emails.csv', index=False)
