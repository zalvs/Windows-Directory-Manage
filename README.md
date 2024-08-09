# Windows Directory Manager

Windows Directory Manager is a Python script designed to streamline the process of creating and managing directories on a Windows operating system. This script is particularly useful for system administrators and developers who need to automate file management tasks on Windows systems.

- Create directories on a specified path
- List the contents of directories
- Robust error handling to manage potential issues during execution

## Features

- **Create Directories**: The script checks whether a specified directory exists and creates it if it doesn't. This feature is handy for setting up directory structures as part of an automated workflow.
- **List Directory Contents**: After creating a directory, the script lists all files and subdirectories within it, providing an easy way to verify the contents.
- **Error Handling**: Includes comprehensive error handling to manage issues such as permissions errors or other unexpected exceptions.

## Tech

Windows Directory Manager is built using Python's standard libraries, ensuring that it is lightweight and easy to run without requiring additional dependencies.

- [Python 3.x] - A versatile and powerful programming language.
- [subprocess] - Python's built-in library for running system commands.

## Installation

Windows Directory Manager requires [Python](https://www.python.org/) 3.x to run.

Clone the repository, navigate to the directory, and run the script:

```sh
git clone https://github.com/yourusername/windows-dir-manager.git
cd windows-dir-manager
python directory_manager.py
```

## Usage

To use the script, simply specify the base path where you want to create the directory and the name of the directory you want to create:

```python
caminho_base = r"H:\FIAP\alberico"
nome_pasta = "ExemploPasta"
criar_pasta_e_listar_conteudo(caminho_base, nome_pasta)
```

## Development

Want to contribute? Great!

You can contribute by forking the repository, making changes, and submitting a pull request.

### To make changes:

Open your favorite terminal and run these commands:

```sh
# To run the script
python directory_manager.py
```



[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [Python 3.x]: <https://www.python.org/>
   [subprocess]: <https://docs.python.org/3/library/subprocess.html>

