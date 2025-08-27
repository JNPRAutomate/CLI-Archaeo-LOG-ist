# -------------------------------------
#   Author: Sotirios Kougiouris
#   Date: 9 / 3 / 2024
#   Description: A script to parse command logs in routers in order to see the most commonly used commands, as well as which users are running what commands.
#   Usage: python command_log_parser.py input-directory outputfile
# -------------------------------------

import os
import re
import sys

# global variables for the total commands and the users/commands
commands_count = {}
user_commands = {}

def parse_file(path, excluded):
    # the regular expression pattern matching string to use for each line of the command
    pattern = r"User '(.+)', command '(.+)'"

    with open(path, 'r') as file:
        for line in file:
            # searching for the right pattern
            match = re.search(pattern, line)
            if match:
                user = match.group(1)
                full_command = match.group(2).strip()

                # excluding unwanted parts from command
                command = ""
                for word in full_command.split():
                    if(any(i.isdigit() for i in word) or (word in excluded)):
                        break
                    command += word + ' '
                command = command.strip()

                if command != '':
                    # getting the total count of the all the commands
                    commands_count[command] = commands_count.get(command, 0) + 1

                    # filling the dictionary with the users and commands
                    user_commands[user] = user_commands.get(user, {})
                    user_commands[user][command] = user_commands[user].get(command, 0) + 1

def main(input_dir, output_file):
    # getting any unwanted commands
    print('Please enter the command/word that you want ignored and press ENTER:\n  (i.e. everything after this word will not be considered)\n  (numbers are already excluded)\n  (for multiple, enter them with A SPACE in between)\n  (simply press ENTER to skip)')
    # checking the Python version because raw_input() and input() have changed from Python 2 -> 3
    if(sys.version_info[0] < 3):
        excluded = raw_input().split()
    else:
        excluded = input().split()

    # excluding any Python files from the files to read
    log_files = [(input_dir + '/' + i) for i in os.listdir(input_dir) if (not i.endswith('.py'))]
    if not log_files:
        print("No files found in the current directory")
        return

    for file in log_files:
        # get the users and commands for each file
        parse_file(file, excluded)

    # writing the users and the comands
    with open(output_file, "w") as f:
        # printing commands by count
        if commands_count:
            f.write("Here is a total list of commands and how many times they were used:\n")
            # had to do some dictionary manipulation here to make it sorted
            for command in sorted(commands_count, key=commands_count.get, reverse=True):
                f.write("  - '" + command + "' ran " + str(commands_count[command]) + " time(s)\n")
        else:
            f.write("No commands found!\n")

        # printing commands by user
        if user_commands:
            f.write("\n\n-----------------------------------------------------------------\nHere is a list of users and the commands they used:\n")
            for user, commands in user_commands.items():
                f.write("  " + user + ":\n")
                for command in sorted(commands, key=commands.get, reverse=True):
                    # had to do some dictionary manipulation here to make it sorted
                    f.write("    - ran '" + command + "' " + str(commands[command]) + " time(s)\n")
        else:
            f.write("No users or commands found!\n")

if __name__ == "__main__":
    try:
        # getting command line options
        input_dir = sys.argv[1]
        output_file = sys.argv[2]
        main(input_dir, output_file)
    except Exception as e:
        print("\n\nSomething went wrong:\n" + str(e))
        print("\nUsage:\n    python command_log_parser.py input-directory outputfile\n\n")
