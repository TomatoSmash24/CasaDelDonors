# CasaDelDonors
Web Application for users to donate items to charity.

# To edit and set up the development environment:

## 1) Clone the repo to any folder/directory of your choice.
Run this command:
```bash
git clone https://github.com/TomatoSmash24/CasaDelDonors.git/CasaDelDonors.git
```
OR
<hr>
Clone the repo using GitHub Desktop.

## 2) Create a Virtual Environment
Virtual environments are required to ensure that dependencies are kept distinct and installed only for that particular project.

Use an IDE, preferably Visual Studio Code and create the virtual environment.

## 3) Activate the virtual environment
Enter the virtual environment (say, venv) by running the following command in the VS Code Command Prompt terminal:
```shell
venv\scripts\activate
```
This will activate the virtual environment (venv). This can be verified by checking for a header that says '(venv)' before or above your command prompt.
When you close the command prompt, the virtual environment will be deactivated automatically.
or if you want to deactivate the virtual environment manually, run:
```shell
deactivate
```
<hr>

**ALWAYS make sure that you are in the virtual environment before running the application, because all the modules for the application are installed in the virtual environment. Hence, if the virtual environment is not active, you will get a `ModuleNotFoundError` error, as the modules are installed in the virtual environment, not in the default Python installation.**


## 4) Install the required modules using pip
For example:
```shell
pip install flask
```
The above command installs flask in the environment.
Again, make sure that you are in the virtual environment before installing the required modules.

## 5) Run the application
Run the application by running the following command in the VS Code Command Prompt terminal:
```shell
python app.py
```
Once the application is running, go to your preferred web browser and visit `localhost:5000` to view it.

Use `ctrl+c` to stop the application.
<hr>
