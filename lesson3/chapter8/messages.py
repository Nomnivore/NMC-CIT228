# import message_activity
# from message_activity import *
# import message_activity as ma
# from message_activity import show_messages as sm
from message_activity import show_messages


my_messages = [
    "Hello, world!",
    "It is fun to work with python again.",
    "I do miss some of the magic of Ruby",
    "I think this can be more performant though, and there is probably syntactic sugar awaiting discovery!"
]


sent_messages = []
print("\n---- Using List Copy ----")  # 8.11
show_messages(my_messages[:], sent_messages)

# ---- 8.15
# message_activity.show_messages(my_messages, sent_messages)
# ma.show_messages(my_messages, sent_messages)
# sm(my_messages, sent_messages)
# ----

print("---- Checking Lists ----")
print(my_messages)
print(sent_messages)

print("\n---- Displaying Messages ----")  # 8.10
show_messages(my_messages, sent_messages)

print("---- Checking Lists ----")
print(my_messages)
print(sent_messages)


