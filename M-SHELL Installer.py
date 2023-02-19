print("M-SHELL Command Installer v1.0")
import json, requests

try:
    commands = open("commands.json")
    temp1 = commands.read()
    commands.close()

    commands = temp1
    del temp1
except:
    print("The commands.json file is either missing or invalid.")
    while True:
        pass

try:
       commands = json.loads(commands)
except Exception as e:
   print("The commands.json file is invalid.")
   while True:
       pass
while True:
    source = input("Please specify a file or website to source from: ")
    try:
        file = open(source)
        data = file.read()
        file.close()
    except:
        try:
            data = requests.get(source).text
        except:
            print("The URL or filename is invalid.")
            print("\n")
            continue

    command_name = input("Please provide a name for this command: ")
    print("Installing command..")
    if not command_name in commands.keys():
        commands[command_name] = data

        temp1 = open("commands.json", "w")

        temp1.write(json.dumps(commands))
        temp1.close()
        del temp1

    else:
        answer = input("Error: The command already exists. Remove it? (Y/N) ").lower()
        if answer == "y":
            print("Uninstalling command..")
            del commands[command_name]

            temp1 = open("commands.json", "w")

            temp1.write(json.dumps(commands))
            temp1.close()
            del temp1
            print("Command uninstalled.")
        else:
            print("Operation cancelled.")

    print("\n")
        
            
