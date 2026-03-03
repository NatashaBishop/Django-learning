is Python installed?: 

    python --version 
package manager PIP needed to install Django. PIP is included with Python from version 3.4. 

    pip --version 
navigate to project directory, create Virtual Environment. venv is a part of Python:

    python -m venv myenv #where myenv is just a chosen name for Virtual Environment

virtual environment will create a folder named "myenv" with subfolders and files: 

    myenv
        Include
        Lib
        Scripts
        .gitignore
        pyvenv.cfg 
activate the environment (Windows):  

    myenv\Scripts\activate.bat # activate  virtual environment every time in command prompt to work on the project
After virtual environment is created, activate: install Django while in virtual environment 

    (myenv) ... $ python -m pip install Django
