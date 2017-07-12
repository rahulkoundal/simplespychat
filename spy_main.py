#project is started


from spy_details1 import spy, Spy, ChatMessage, friends
from steganography.steganography import Steganography
from datetime import datetime
import sys
from termcolor import colored, cprint

STATUS_MESSAGES = ['Bob marley is back', 'Sachin not required introduction.', 'Dhoni is two step fast than game']


#print("*********Hello! Let 's get started****************")
text = colored("*********Hello! Let 's get started****************", 'blue', attrs=['reverse', 'blink'])
print(text)
question = colored("Do you want to continue as " + spy.salutation + " " + spy.name + " (Y/N)? ",'red',attrs=['reverse', 'blink'])
existing = raw_input(question)

#cprint('Hello, World!', 'green', 'on_blue')

#add_status() function to add status
#degination of the function
def add_status():

    updated_status_message = None

    if spy.current_status_message != None:

        print("Your current status message is %s \n' % (spy.current_status_message)")
    else:
        print("You don\'t have any status message currently \n")

        default = raw_input("Do you want to select from the older status (y/n)? ")

        if default.lower() == "n":
         new_status_message = raw_input("What status message do you want to set? ")


        if len(new_status_message) > 0:
            STATUS_MESSAGES.append(new_status_message)
            updated_status_message = new_status_message

        elif default.lower() == 'y':

         item_position = 1

         for message in STATUS_MESSAGES:
            print '%d. %s' % (item_position, message)
            item_position = item_position + 1

        message_selection = int(raw_input("\nChoose from the above messages "))

#len() calculate the length of the variable
    if len(STATUS_MESSAGES) >= message_selection:
            updated_status_message = STATUS_MESSAGES[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message:
        print("Your updated status message is: %s % (updated_status_message)")
    else:
        print("You current don't have any  status update")

    return updated_status_message

#add_friend function to add the friend

def add_friend():

    new_friend = Spy('','',0,0.0)

    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating = raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)

    if len(new_friend.name) > 0 and new_friend.age > 12 and new_friend.rating >= spy.rating:
        friends.append(new_friend)
        print("**************Friend is addded **************")
    else:
        print 'Sorry! Invalid entry. We can\'t add spy with the details you provided'

    return len(friends)

#select_a_friend() function to select a friend

def select_a_friend():
    item_number = 0
#for loop is staerted

    for friend in friends:
        print '%d. %s %s aged %d with rating %.2f is online' % (item_number +1, friend.salutation, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1
#return to return the value of the variable
    return friend_choice_position
#concatenation will take place

#send_message function for sending the message to the friends
#cases when spy send message 100 words
#cases when spy send a message with special words such as SOS, SAVE ME
#cases when the image contains no secret message
def send_message():
#calling to selct_a_friends function

    friend_choice = select_a_friend()


    original_image = raw_input("What is the name of the image?")
    #output path of the image
    output_path = "output.jpg"
    text = raw_input("What do you want to say? ")
 #steganography is used for the incrption and decruption
    Steganography.encode(original_image, output_path, text)

    new_chat = ChatMessage(text,True)

    friends[friend_choice].chats.append(new_chat)
#length validation
    if len(text) <= 0:
        print("u cannot send empty message!!!!")
    elif len(text) > 100:
        del friends[friend_choice]
        print("you exceed the message limit .. please try again later!!!!")
    else:
        Steganography.encode(original_image, output_path, text)

        new_chat = ChatMessage(text, True)
        friends[friend_choice].chats.append(new_chat)
        print("your secret message is ready.")

#special characters.
    if text.upper() == "SOS" or text.upper() == "SAVE ME" or text.upper() == "HELP":
        print("you will receive help soon...")


#read_message() function to read the message

def read_message():
    # calling to selct_a_friends function
    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")
#steganography to decodethe message

    secret_text = Steganography.decode(output_path)
    print secret_text

    new_chat = ChatMessage(secret_text,False)

    friends[sender].chats.append(new_chat)

    print("**************Your secret message has been saved********************")

#read_chat_history() function to read message

def read_chat_history():

    read_for = select_a_friend()

    print '\n6'

    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            text1 = colored( chat.time.strftime("%a, %d %b %Y %H:%M:%S +0000"), 'blue', attrs=['reverse', 'blink'])
            print(text1)
            cprint(' you said', 'green', 'on_red')
            print(chat.message)
            #print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:
            text1 = colored(chat.time.strftime("%a, %d %b %Y %H:%M:%S +0000"), 'blue', attrs=['reverse', 'blink'])
            print(text1)
            cprint(friends[read_for].name,'green','on_red')
            print(chat.message)
            #print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)

cprint('Hello, World!', 'green', 'on_blue')
def start_chat(spy):

    spy.name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete.\n********************************* Welcome****************\n " + spy.name + " your  age is: " \
              + str(spy.age) + "\n your   rating is: " + str(spy.rating) + "\n Proud to have you onboard"

        show_menu = True

        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menu_choice = int(menu_choice)

                if menu_choice == 1:
                    spy.current_status_message = add_status()
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menu_choice == 3:
                    send_message()
                elif menu_choice == 4:
                    read_message()
                elif menu_choice == 5:
                    read_chat_history()
                else:
                    show_menu = False
    else:
        print("Sorry you are not of the correct age to be a spy")

if existing.upper() == "Y":
    start_chat(spy)
elif existing.upper() =="N":

    spy = Spy('','',0,0.0)


    spy.name = raw_input("Welcome to spy chat, you must tell me your spy name first: ")

    if len(spy.name) > 0:
        spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

        spy.age = raw_input("What is your age?")
        spy.age = int(spy.age)

        spy.rating = raw_input("What is your spy rating?")
        spy.rating = float(spy.rating)

        start_chat(spy)
    else:
        print("Please enter a valid name")

