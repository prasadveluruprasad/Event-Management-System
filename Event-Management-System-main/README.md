**Overall Instruction** 

Installation of our software takes 5 steps. 

1.The first step is to install a python IDE/code editor so that the code can be run. 

2.The second step is to clone our project from github. 

3.The third step is to install all related packages listed in requirement.txt.  

4.The fourth step is to install and initialize the database so that the data can be stored. 

5.The last step is to run our software by following commands in section.

-----------------
**Packages installation**

All packages are listed in a requirements.txt file (fig 5.1 below) within the directory of capstone_project _bugmaker. All the packages should be installed with the corresponding version. Instead of installing them one by one, a quicker way to install all packages by using pip command can be found on https://stackoverflow.com/questions/7225900/how-to-install-packages-using-pip-according-to-the-requirements-txt-file-from-a



-------------------------

**Database Installation** 

The database used for our software is MySql database. If you have not installed MySql before,  you should download the correct version based on your operating system by going to this link https://dev.mysql.com/downloads/mysql/.  Also, a very useful installation guidance, summarizing all installation steps and all potential issues,  can be found on https://dev.mysql.com/doc/mysql-installation-excerpt/5.7/en/.

Important note : During the installation, the installer displays a window with your temporary root password (e.g fig 5 below). “This temporary password cannot be recovered so you must save this password for the initial login to MySQL, MySQL expires this temporary root password after the initial login and requires you to create a new password”. [3] To successfully connect the software to the database, the password for MySql is required to be set to be 12345678 so that our software has access to the data in MySql.



If you already have  a MySql database on your computer, you should change the password to 12345678 temporarily for testing our software.  The instruction for reset password can be found on this website. https://dev.mysql.com/doc/refman/8.0/en/resetting-permissions.html
Once Mysql has been installed and password has been set properly, you can proceed to initialize the database by following the below section.

-------------------------
**Database initialization** 

The following commands are used to initialize the database for the software. To start MySql, you should type the following command on terminal or prompt. The password should be exactly 12345678.

$  mysql -u root -p

$  Password: 12345678

To create a database,  exactly the following commands should be used to initialize a database.  The name of the database must be “eventManager” so that our software can connect to exactly this database.

$ mysql > create database eventManager;

Query OK, 1 row affected (0.01 sec)

Once the database is created, now you can run our software on another terminal or prompt by following the below guidance.

----------------------
How To Run Our System 

After successfully installing the database and all required packages (above section).

$ git clone the repository from github

$ cd capstone-project-bugmaker

$ python run.py

The website will be running on  http://127.0.0.1:5000/, open this link in the browser (Google Chrome is prefered). 

------------
FULL DESCRIPTION SHOWN IN REPORT

