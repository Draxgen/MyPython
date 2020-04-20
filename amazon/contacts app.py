'''
Contacts app
'''
contactList = []

def contacts(query):
    global contactList
    command, argument = query.split(' ', 1)
    if command == 'add':
        contactList.append(argument)
        return
    elif command == 'find':
        matching = [s for s in contactList if argument in s]
        print(len(matching))

if __name__ == "__main__":
    contacts('add hack')
    contacts('add hackhaton')
    contacts('find ack')
    contacts('find tem')
