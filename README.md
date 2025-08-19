# CLI-Archaeo-log-ist
Wondering what operational commands are being used on your devices?  Perhaps you’d like to automate operational processes and are looking to know what issues are most commonly encountered by your Ops team and how they troubleshoot those issues.  This script to parses command logs in order to see the most commonly used operational commands, as well as which users are running what commands (and frequency). 

Usage: 

> python command_log_parser.py input-directory outputfile

Sample output:

```
> python command_log_parser.py tmp-cli-logs/ output.txt
> cat output.txt

Here is a total list of commands and how many times they were used:
  - 'show system errors active detail' ran 15 time(s)
  - 'show chassis pic fpc-slot' ran 5 time(s)
  - 'show interfaces' ran 5 time(s)
  - 'show chassis routing-engine' ran 5 time(s)
  - 'show chassis environment fpc' ran 5 time(s)
  - 'show interfaces terse | match' ran 5 time(s)
  - 'show chassis hardware extensive | find FPC | match' ran 5 time(s)
  - 'show system error active detail' ran 5 time(s)
  - 'exit' ran 2 time(s)
  - 'show log interactive-commands | grep show' ran 1 time(s)
  - 'show configuration system' ran 1 time(s)
  - 'configure' ran 1 time(s)
  - 'file show interactive-commands' ran 1 time(s)
  - 'set system login user user3 class super-user authentication plain-text-password' ran 1 time(s)
  - 'show log interactive-commands' ran 1 time(s)
  - 'commit and-quit' ran 1 time(s)


-----------------------------------------------------------------
Here is a list of users and the commands they used:
  user1:
    - ran 'show system errors active detail' 15 time(s)
    - ran 'show chassis pic fpc-slot' 5 time(s)
    - ran 'show interfaces' 5 time(s)
    - ran 'show chassis routing-engine' 5 time(s)
    - ran 'show chassis environment fpc' 5 time(s)
    - ran 'show interfaces terse | match' 5 time(s)
    - ran 'show chassis hardware extensive | find FPC | match' 5 time(s)
    - ran 'show system error active detail' 5 time(s)
  user2:
    - ran 'set system login user user3 class super-user authentication plain-text-password' 1 time(s)
    - ran 'exit' 1 time(s)
    - ran 'configure' 1 time(s)
    - ran 'commit and-quit' 1 time(s)
  user3:
    - ran 'show configuration system' 1 time(s)
    - ran 'show log interactive-commands | grep show' 1 time(s)
    - ran 'exit' 1 time(s)
    - ran 'file show interactive-commands' 1 time(s)
    - ran 'show log interactive-commands' 1 time(s)
```
