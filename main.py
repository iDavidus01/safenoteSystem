user = input("Login: ")


def add_command(args):
    if len(args) >= 3:
        command = args[0]
        access_type = args[-1]
        content = ' '.join(args[1:-1])
        with open('data.py', 'a') as file:
            file.write(f'\n{{"command": "{command}", "content": "{content}", "owner": "{user}", "access": "{access_type}"}}')
        print("OK")
    else:
        print("Error")


def cat_command(args):
    if args:
        name = args[0]
        found = False
        with open('data.py', 'r') as file:
            for line in file:
                if f'"command": "{name}"' in line and (f'"owner": "{user}"' in line or f'"access": "u-r"' in line):
                    access_type = line.split('"access": "')[1].split('"')[0]
                    if access_type in ["u-n", "u-r", "u-x"]:
                        content = line.split('"content": "')[1].split('"')[0]
                        print(content)
                        found = True
                        break
                    else:
                        print("Nie masz do tego uprawnien")
                        found = True
                        break
        if not found:
            print("Error")


def edit_command(args):
    if args:
        name = args[0]
        found = False
        with open('data.py', 'r') as file:
            lines = file.readlines()
        with open('data.py', 'w') as file:
            for line in lines:
                if f'"command": "{name}"' in line and f'"owner": "{user}"' in line:
                    access_type = line.split('"access": "')[1].split('"')[0]
                    if access_type in ["u-n", "u-x", "u-r"]:
                        content = line.split('"content": "')[1].split('"')[0]
                        new_content = input(f"Napisz nowa tresc '{name}': ")
                        line = line.replace(content, new_content)
                        found = True
                file.write(line)
        if found:
            print("OK")
        else:
            print("Error")


while True:
    command = input("#> ").split(' ')

    match command:
        case ["quit"]:
            break
        case ["add", "note", *args]:
            add_command(args)
        case ["cat", *args]:
            cat_command(args)
        case ["edit", "note", *args]:
            edit_command(args)
