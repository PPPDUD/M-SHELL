print("mshell v1.0, made with food and Python.")

print("Loading command dictionary..")
import json

try:
    commands = open("commands.json")
    temp1 = commands.read()
    commands.close()

    commands = temp1
    del temp1

except FileNotFoundError:
    print("Commands file missing. Generating a default commands file..")
    commands = open("commands.json", "w")
    commands.write(json.dumps({"test":"print('hi')"}))
    commands.close()
    commands = open("commands.json")
    temp1 = commands.read()
    commands.close()
    commands = temp1
    del temp1
 

except Exception as e:
    print(str(e))
    while True:
        pass

try:
       commands = json.loads(commands)
except Exception as e:
    print(str(e))
    while True:
        pass
print(commands)

print("\nmshell has booted and will now begin prompting.")

while True:
    command = input("Command: ")
    if command in commands.keys():
        eval(commands[command])

    else:
        print("There are no commands with that name. Sorry.")
