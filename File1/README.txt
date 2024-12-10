Step 1: Install a relational database, in this case, I will be using MySQL Server into an Ubuntu Environment.
    sudo apt install mysql-server -y
    sudo systemctl status mysql
Step 2: It is a best practice to modify the user that will be allow to connect to the database in order to be able to connect the databese with any graphical utility (dbvisualizer, mysql workbench, etc)
    sudo mysql
    alter user 'root'@'localhost' identified with mysql_native_password by 'admin1234';
    exit;