# import datetime

from datetime import datetime

# class spy
# with detsils of name ,salutation,age ,rating as the argument
# self is used for calling in constructor funnction



class Spy:

    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None


# class chatmessage
# meassage and sent_by_me in the argumnet

class ChatMessage:
     #constructor of the class
    def __init__(self,message,sent_by_me):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me
# value is given
spy = Spy('bond', 'Mr.', 24, 4.7)

friend_one = Spy('Raja', 'Mr.', 4.9, 27)
friend_two = Spy('Mata Hari', 'Ms.', 4.39, 21)
friend_three = Spy('No', 'Dr.', 4.95, 37)

#list of friends
friends = [friend_one, friend_two, friend_three]
