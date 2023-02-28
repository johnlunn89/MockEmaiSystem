#Establish Class and uses init function to create attributes, some with default arguements

class Email():

    def __init__(self, email_contents, from_address="john.lunn@email.com", has_been_read=False, is_spam=False,):
        self._has_been_read = has_been_read
        self._email_contents = email_contents
        self._is_spam = is_spam
        self._from_address = from_address

# below I have created methods for the Class

    def mark_as_read(self):
        self._has_been_read = True

    def mark_as_spam(self):
        self._is_spam = True

    def show(self):
        print(self._email_contents, self._from_address, self._has_been_read, self._is_spam)

    def __str__(self):
        return f"Email Contents: {self._email_contents}\n" \
               f"From: {self._from_address}\n" \
               f"Read?: {self._has_been_read}\n" \
               f"Spam? {self._is_spam}\n"

# below are my functions

def get_count(list):
    length = (len(list))
    print(f"There are {length} emails in the inbox.")
    return length

def get_email(list):
    i = int(input("Please enter the number of the email you would like to view: "))
    i = i-1
    list[i].mark_as_read()
    print(list[i])
    return list

def get_and_mark_spam(list):
    i = int(input("Please enter the number of the email you would like to mark as spam: "))
    i = i-1
    list[i].mark_as_spam()
    print(list[i])

def get_unread_email(list):
    for i in range(len(list)):
        if list[i]._has_been_read == False:
            print(list[i])

def get_spam_email(list):
    for i in range(len(list)):
        if list[i]._is_spam == True:
            print(list[i])

def delete(list):
    list.clear()

def add_email(list):
    email_contents = ()
    new_email = Email(email_contents)
    new_email._email_contents = input("Please the content of your email: ")
    new_email._from_address = input("Please enter email address of the sender: ")
    new_email._is_spam = False
    new_email._has_been_read = False
    list.append(new_email)
    return list


# empty list initialisation, pre-created objects containing email contents(other arguments are pre-set)

inbox = []
email1 = Email("Hi, Please could you send me the invoice?")
email2 = Email("Hi, Please could you send a copy of my tax return?")
email3 = Email("Hi, You have been selected for a prize draw, please reply to learn more.")
email4 = Email("Hi, Your grandma's birthday is coming up, will you be visiting?")
email5 = Email("Hi, Please find your train tickets attached.")

inbox = [email1, email2, email3, email4, email5]

# #An Email Simulation
user_choice = ""

while user_choice != "quit":
    user_choice = input("What would you like to do - read/mark spam/send/delete all/quit?: ")
    if user_choice == "read":
        get_count(inbox)
        read_choice = input("Type 'c' to choose an email to read, 'u' to read"
                            " all unread or 's' to read all spam: ").lower()
        if read_choice == "c":
            while True:
                try:
                    get_email(inbox)
                except ValueError:
                    print("Not a valid entry, please try again...")
                except IndexError:
                    print("That email does not exist, please try again...")
                break
        if read_choice == "u":
            get_unread_email(inbox)
        if read_choice == "s":
            get_spam_email(inbox)
        elif read_choice not in ("c", "u", "s"):
            print("oops, wrong input, please try again...")
    elif user_choice == "mark spam":
        get_and_mark_spam(inbox)
    elif user_choice == "send":
        add_email(inbox)
        print(inbox)
    elif user_choice == "delete all":
        print(inbox)
        delete(inbox)
        print(inbox)
    elif user_choice == "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")
