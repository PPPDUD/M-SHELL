# M-SHELL
M-SHELL is a free (as in freedom and also pricing) Python shell where its userbase does all of the work.

By default, each copy will provide one command: test.
The "test" command just says "hi".

To develop your own commands, save a Python file containing all of your code and name it with a .ms extension.
To install a command, download and run the supplied "M-SHELL Installer" and type in the name of the file or website where the command's definition is stored (e.g, "rickroll.ms").

After installing a new command, your M-SHELL copy will require restarting for the changes to apply.

To uninstall a command, do the following steps:
1. Open the installer.
2. Type in the name of any command file (it won't affect the uninstallation).
3. Make the command name the name of the command you want to uninstall.
4. Confirm the uninstallation of the command by typing "Y" and pressing ENTER.

We welcome everyone to produce and provide commands for the community to utilize. To advertise your commands, click here: https://scratch.mit.edu/discuss/topic/664186/.

# Errors and their causes
Starting with version 1.3, whenever errors occur, they are documented on-screen instead of closing the window. Common errors and their causes are listed below:

<h2><code>Forbidden command</h2></code>
This error appears after attempting to install a command under an invalid name. Valid names cannot be named "install", and cannot have uppercase characters.

<h2><code>Expecting property name enclosed in double quotes: line x column xx (char x) / Expecting ',' delimiter: line 1 column xx (char xx)</h2></code>
These errors occur when the commands.json file has been improperly tampered with. Try deleting the file and trying again.

<h2><code>Expecting value: line x column x (char x)</h2></code>
This error happens when severe tampering with commands.json has occured. Examples include blanking out or completely replacing the file.

<h2><code>Commands file missing. Generating a default commands file..</h2></code>
This error occurs whenever the program cannot find commands.json. It happens on first usage and will be fixed automactially.

# Malware detection
Starting with version 1.5, all copies of M-SHELL have extremely strict antiviruses built in. If you have 1.5, you might notice alot of threat warnings. Here are some tips to prevent this in your commands:

1. Never use files. Use getData(key), setData(key, value) and delData(key) instead. M-SHELL 1.5 will handle the rest on your behalf.
2. Never use exec() and eval(). Not only do they pose vulnerabilities depending on the use case, but they can be used to bypass the antivirus.
3. Don't use exit() and sys.exit(). Both can cause severe frustration for the user, so they are flagged.

# Official commands available for download
The following commands can be installed using the `install` command and providing a URL:
1. https://mojavesoft.net/dataWrite.ms - A simple command for storing data on 1.5 and later. Doesn't work on pre-1.5 copies.
2. https://mojavesoft.net/antivirus-test.ms - Triggers the 1.5 antivirus. When executed, prints "Hello, world!", and then "20".
3. https://mojavesoft.net/dataRead.ms - Reads data created using dataWrite.
4. https://mojavesoft.net/dataDelete.ms - Deletes data created using dataWrite.
