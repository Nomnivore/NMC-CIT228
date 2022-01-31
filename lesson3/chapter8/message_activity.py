def show_messages(messages, sent):
    while messages:
        msg = messages.pop(0)
        print(msg)
        sent.append(msg)
