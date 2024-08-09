This repository contains a Python script designed to simplify the process of creating and managing directories on a Windows operating system. The script leverages Python's subprocess module to interact with the Windows command line, allowing for seamless creation and listing of directories directly from the script. It's particularly useful for automating file management tasks on Windows systems.

Features:
Create Directories: The script checks for the existence of a specified directory and creates it if it doesn't already exist. This is particularly useful for automating tasks that require setting up specific directory structures.

List Directory Contents: After creating a directory, the script can list all files and subdirectories within it, providing a quick overview of the directory's contents.

Error Handling: The script includes robust error handling to manage issues such as attempting to create an already existing directory, or encountering unexpected errors during execution. This ensures that the script runs smoothly and provides clear feedback in case of any issues.

No External Dependencies: The script relies on Python's standard libraries, specifically the subprocess module, making it lightweight and easy to run without requiring additional installations.

Use Cases:
Automated Setup Scripts: Use this script as part of a larger automation process to set up directory structures on new machines or within projects.

File Management: Automate the creation and organization of directories for different tasks, such as sorting files into specific folders or setting up directories for data storage.

System Administration: Helps in managing directories on Windows servers or workstations, providing an easy way to script repetitive file system tasks.

Getting Started:
Clone the Repository:

sh
Copiar código
git clone https://github.com/yourusername/windows-dir-manager.git
cd windows-dir-manager
Run the Script:
Modify the caminho_base and nome_pasta variables in the script to specify your desired directory path and name, then execute the script.

python
Copiar código
python directory_manager.py
Customize:
You can easily extend this script by adding more functionality, such as deleting directories, moving files, or integrating it into larger automation workflows.

Requirements:
Python 3.x
Windows OS
Contributing:
Contributions are welcome! Feel free to submit pull requests with enhancements, bug fixes, or additional features.
