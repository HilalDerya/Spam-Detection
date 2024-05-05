import mailbox

mb = mailbox.mbox('C:\\Users\\asus\\Masaüstü\\Takeout\\Posta\\sample.mbox')

# Check if there's at least one message in the mbox
if len(mb) > 0:
    # Get the headers of the first message
    first_message = mb[0]
    for key in first_message.keys():
        print(key)
else:
    print("The mbox file is empty or does not contain any messages.")


