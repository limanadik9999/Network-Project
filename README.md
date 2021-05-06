# Network-Project

Web Application for a Social Network with a focus on creating events. 

To run the PRoject on local machine you need:

1. Install Python from https://www.python.org/downloads/
For windows please do not forget to check option"Add Pthon to enviroment variables" or do it manually after insatllation Python 3 by default will be installed in C:\Users\\AppData\Local\Programs\Python\Python35-32\ So this path has to be added to Path variable in windows environment.
2. Install PyCharm from https://www.jetbrains.com/pycharm/
For Windows also please add PyCharm in environment variables by checking suggested option during installation or do it manually after.
3. Open PyCharm -> Open Project from unpacked zip archive
4. Execute commands in PyCharm terminal: 


for Mac:
pip3 install virtualenv
virtualenv newenv
source newenv/bin/activate
pip3 install django
pip3 install djoser
pip3 install pillow
python3 manage.py runserver


for Windows:
pip install virtualenv
virtualenv newenv
newenv\Scripts\activate.bat
pip install django
pip install djoser
pip install pillow
python manage.py runserver


5. click on the link in Terminal
http://127.0.0.1:8000/
