main_dict = {}
exit_conditions = {"exit", "quit", ":q", "q"}
known_commands = {'add', 'change', 'phone', 'show_all', '?'}

def input_error(func):
    def inner(*args):
        try:
            return func(*args)
        except IndexError:
            return(f"{func.__name__}: Ask me someting")
        except TypeError:
            return(f"{func.__name__}: Check arguments")
    return inner

@input_error
def answer_func(query):                       # input command parser
    command = query.split()[0]
    args = query.split()[1:]
    if command in known_commands:
        if command == 'add':
            return add(*args)
        elif command == 'change':
            return change(*args)
        elif command == 'phone':
            return phone(*args)
        elif command == 'show_all':
            return show_all()
        elif command == '?':
            return f'Try commands: {", ".join(known_commands|exit_conditions)}'
    else:
        return "Wrong command!"

def check_args(name, phone):
    if name == '':
        return 'Empty name'
    elif phone == '':
        return 'Empty phone'
    elif check_phone(phone) == None:
        return 'Wrong phone number'
    
def check_phone(phone):
    if phone.startswith('+') and phone[1:].isnumeric() and len(phone[1:]) == 12:
        return phone
    elif phone.isnumeric() and len(phone) == 12:
        return f'+{phone}'
    elif phone.isnumeric() and len(phone) == 10:
        return f'+38{phone}'
    else:
        return None

@input_error    
def add(name='', phone=''):
    if not check_args(name, phone):
        if name in main_dict:
            return f'Name "{name}" exists, use "change" to override phone'
        else:
            main_dict[name] = check_phone(phone)
    else:
        return check_args(name, phone)
        
@input_error
def change(name='', phone=''):
    if not check_args(name, phone):   
        if name in main_dict:
            main_dict[name] = check_phone(phone)
        else:
            return f'Name "{name}" dosn\'t exists, use "add" to add contact'
    else:
        return check_args(name, phone)
    
@input_error
def phone(name=''):
    if name == '':
        return 'Empty name'
    if name in main_dict:
        return main_dict[name]
    else:
        return f'Name "{name}" doesn\'t exists'

def show_all():
    contacts = ''
    for key,val in main_dict.items():
        contacts = contacts + f'{key}\t{val}\n'
    return contacts

#-------------------------------------

def main():
    while True:
        query = input(">>> ").lower()
        if query in exit_conditions:
            print("Good bye!")
            break
        elif query == 'hello':
            print("How can I help you?")
        else:
            respond = answer_func(query)
            if respond == None:
                pass
            else:
                print(respond)

if __name__ == '__main__':
    main()

