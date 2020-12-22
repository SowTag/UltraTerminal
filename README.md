# UltraTerminal
A custom terminal made to simplify the customization of your everyday terminal.

### Compatible with Windows, Linux and MacOS (untested)

## Installation:
```bash
git clone http://github.com/SowTag/UltraTerminal.git
cd UltraTerminal
python UltraTerminal.py
```
\* In some cases you may need to use `python3` or `python -3` instead of just `python`.

## To-do:
- [ ] Fixing arrow keys (^[[A and other characters being typed instead of navigating through the input)
- [ ] Change variables while running the script itself
- [ ] More compatibility when being used as main terminal and in-terminal programs (such as nano).

### Packages used:
| Package name | Usage | Methods used
|--|--|--|
| colorama | Coloring the input field | Fore, Back, init() and Style.|
| os | Executing commands and getting OS name. | popen(), name and system() |
| getpass | Getting current user username. | getuser() |
| socket | Getting system hostname | gethostname() |
