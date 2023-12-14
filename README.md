# CasaDelDonors

Web Application for users to donate items to charity.

# To edit and set up the development environment:

## 1) Clone the repo to any folder/directory of your choice.

Run this command:

```bash
git clone https://github.com/TomatoSmash24/CasaDelDonors.git
```

### OR

Clone the repo using GitHub Desktop by going to `Code` option in the repo main page and clicking `Open With Github Desktop`

<hr>
To pull the latest changes:

```bash
git pull
```

<hr>

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

### OR

```shell
pip install -r requirements.txt
```

This will install all the required modules for the application in the virtual environment.

## 5) Run the application

Run the application by running the following command in the VS Code Command Prompt terminal:

```shell
python app.py
```

Once the application is running, go to your preferred web browser and visit `localhost:5000` to view it.

Use `ctrl+c` to stop the application.

<hr>

## 6) HOW TO CONTRIBUTE

Once you've done all of the above, and have a working version of your code installed,
you are now ready to contribute.

### 1. Download Git

Download the command line tool for Git from [here](https://git-scm.com/downloads).
Run through the installation wizard choosing the defaults, you should be fine. Check if everything
works correctly by opening a new instance of the command prompt and running `git --version`. You
should get no errors.

### 2. Fork the repository

Click the "Fork" button in the top right corner of the project's GitHub page. This creates a copy of the repository in your GitHub account.

### 3. Clone the fork of the repository in your local

The fork of the repository is YOUR version of the repository where you can go wild and
make changes without affecting the stable master version you downloaded earlier. Make sure to
clone the fork of the repository in a different, empty directory.

Create an empty folder for your fork of the repository and open it using command prompt
Then run:

```powershell
git clone https://github.com/<YOUR USERNAME>/CasaDelDonors.git
```

Replace \<YOUR USERNAME> with your Github username.
<hr>

Once you've cloned it, add a remote origin to the master branch so that you can pull the changes made in the master version into your version.

You can achieve this by running
```powershell
git remote add upstream https://github.com/TomatoSmash24/CasaDelDonors.git
```

Now you can regularly run
```
git pull upstream master
```
to pull all the changes from the master branch (this version) into your local version.

Note that `git pull upstream master` only works if you haven't made any changes, so before you make changes YOU MUST RUN `git pull upstream master`.

This will pull all changes from the remote version into this version.

### 4. Make your changes

You can still run your code here. Make changes, and they will reflect.
Just make sure you are not running both web servers at the same time.

Once you are done making changes, you can commit them to Git by running

```
git add .
git commit -m "<PROVIDE A SHORT DESCRIPTION OF CHANGES YOU MADE HERE (REQUIRED)>"
git push origin master
```
Remember -  you are commiting only to your version of the file(that is, the forked version), hence once the changes are pushed, you will have to create a pull request for merging the changes to the main repo.

### 5. Create a pull request

Navigate to the fork of the repository on your Github account and you should see a
prompt to create a pull request for the branch you just pushed. Click on
"Compare & pull request." Write a suitable title and description
for your pull request and click "Create pull request."

#### That's it you are done. If you navigate to the main repo (this one) and go to pull requests, you should see your pull request, pending review. I shall review it and merge it into the main version.

<!-- Navigate to the folder where you want to clone the repository. To make sure you are in the right
directory, run `dir` in the command prompt.  It should list the project files, including `.gitignore`

In case your current terminal working directory is not the project directory, [navigate to
the project directory using the terminal](https://riptutorial.com/cmd/example/8646/navigating-in-cmd)

If you cannot figure out how navigation in the terminal works, simply open the project in
Visual Studio Code and use the in-built terminal.

Make sure git works and that you are in the correct working directory before proceeding.  -->

<hr>
