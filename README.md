# Commandline Virus Scanner
_A simple virus scanner utilising VirusTotal public API. It's run as a script taking file paths separated with commas as arguments._

## Tool setup

Install [mise](https://mise.jdx.dev/getting-started.html), then run from the repository root:

```sh
mise trust
mise install
```

Tool versions are declared in `mise.toml`. Activate mise in your shell, or prefix
project commands with `mise exec --` (for example, `mise exec -- uv --version`).

## Features
Quickly scan files (including archives?) downloaded from the Internet without opening them on your computer. VirusTotal runs multiple scans with dozens of antivirus programmes and checks if a file is safe to use. It's all done in a matter of seconds (read more about VirusTotal <VirusTotal link>)

## How do you use it:
* GUI- should go without saying, otherwise I did a really poor job.
* command line
1. ...
2. ...
3. ...

## Prerequisites 
* Python 3 installed
* VirusTotal public API (it's free, but you need to register an account)
* Internet connection is necessary when you want to scan a file
* Add <scrypt name> to system PATH (optional):
- on <link Windows>
- on <link macOS>
- on Linux

## License

Install Python dependencies in a virtual environment with
`mise exec -- uv venv` and `mise exec -- uv pip install -r requirements.txt`.
The GUI additionally requires Tk support in the selected Python installation.
