Hello there, this is the first file. Enjoy :)

Step 1: Install a relational database, in this case, I will be using MySQL Server into an Ubuntu Environment.
    sudo apt install mysql-server -y
    sudo systemctl status mysql
Step 2: It is a best practice to modify the user that will be allow to connect to the database in order to be able to connect the databese with any graphical utility (dbvisualizer, mysql workbench, etc)
    sudo mysql
    alter user 'root'@'localhost' identified with mysql_native_password by 'admin1234';
    exit;
Step 3: Optional install DBVisualizer or any other graphical utility.
Step 4: Create a database
    mysql --user=root -p
    CREATE DATABASE Prueb1;
    SHOW DATABASES;
    USE prueb1;
    CREATE TABLE firsttable(id INT NOT NULL PRIMARY KEY, name VARCHAR(20), password VARCHAR(20));
    INSERT INTO firsttable VALUE (1,"root","admin1234");
    SELECT * FROM firsttable;
Step 5: Create connection file using python (FIle into this directory).
Step 6: Install driver to connect mysql with python 
    sudo apt-get install python3-pymysql(Ubuntu)
    pip install pymysql
Step 7: Validate connector.
    import pymysql
    python3 connection.py
Step 8: Follow the instructions into the python file.