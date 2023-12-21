def handle_add_command(args):
    if len(args) >= 2:
        command = args[0]
        content = ' '.join(args[1:])
        with open('data.py', 'a') as file:
            file.write(f'\n{{"command": "{command}", "content": "{content}"}}')
        print("OK")
    else:
        print("Error")

def handle_cat_command(args):
    if args:
        name = args[0]
        found = False
        with open('data.py', 'r') as file:
            for line in file:
                if f'"command": "{name}"' in line:
                    content = line.split('"content": "')[1].split('"')[0]
                    print(content)
                    found = True
                    break
        if not found:
            print("Error")

while True:
    command = input("#> ").split(' ')

    match command:
        case ["quit"]:
            break
        case ["add", "note", *args]:
            handle_add_command(args)
        case ["cat", *args]:
            handle_cat_command(args)
