# Counting things in your project
## How many lines of code do i have in general?
### Windows
- Open PowerShell in your project directory and add the below command.
- Why powershell and not cmd? because it has many features that makes it easier to count LOC.
```bash
Get-ChildItem -Recurse -Include *.cpp *.h | Get-Content | Measure-Object -Line
```

### Unix / Linux / MacOS
1. Using command line tools
```bash
wc -l filename
```
2. Using CLOC
```bash
# On Ubuntu/Debian
sudo apt-get install cloc

# On macOS with Homebrew
brew install cloc

# Use
cloc path/to/your/project
```
