# Commandline Virus Scanner
_A simple virus scanner utilising VirusTotal public API. It's run as a script taking file paths separated with commas as arguments._

## Features
Quickly scan files (including archives?) downloaded from the Internet without opening them on your computer. VirusTotal runs multiple scans with dozens of antivirus programmes and checks if a file is safe to use. It's all done in a matter of seconds (read more about VirusTotal <VirusTotal link>)

## How do you use it:
1. Open command prompt (Windows) or Terminal (macOS and Linux)
2. Type in path to the script and path to the file(s) you want to scan, for example:
> "C:\Users\janek\Downloads\main.py" "C:\Users\janek\Desktop\suspicious file.exe", "D:\Games\Half Life 3\crack.zip"

> main.py ".\Desktop\suspicious file.exe", ".\Half Life 3\crack.zip" -- if you don't want to type full path to Commandline Virus Scanner add it to your system PATH (read below how). You can also provide relative paths instead of absolute paths.

> main.py <drag and drop file you want to scan here>

## Prerequisites 
* Python 3 installed
* VirusTotal public API (it's free, but you need to register an account)
* Internet connection is necessary when you want to scan a file
* Add <scrypt name> to system PATH (optional):
- on <link Windows>
- on <link macOS>
- on Linux

## License
