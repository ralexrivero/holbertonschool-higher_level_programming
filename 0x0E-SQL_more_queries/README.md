# 0x0E. SQL - More queries

```sql
███    ███ ██    ██ ███████  ██████  ██
████  ████  ██  ██  ██      ██    ██ ██
██ ████ ██   ████   ███████ ██    ██ ██
██  ██  ██    ██         ██ ██ ▄▄ ██ ██
██      ██    ██    ███████  ██████  ███████
                                ▀▀
```

## Learning Objectives

### General

* How to create a new MySQL user
* How to manage privileges for a user to a database or table
* What’s a PRIMARY KEY
* What’s a FOREIGN KEY
* How to use NOT NULL and UNIQUE constraints
* How to retrieve datas from multiple tables in one request
* What are subqueries
* What are JOIN and UNION

## Environment

<div>
<!-- Ubuntu --> <a href="https://ubuntu.com/" target="_blank"><img height="24px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/ubuntu-icon.svg" alt="Ubuntu"> </a> <!-- GNU Bash --> <a href="https://www.vim.org/" target="_blank"><img height="24px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/gnu-bash-logo.svg" alt="GNU Bash"> <!-- Vim --> <a href="https://www.vim.org/" target="_blank"><img height="24px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/Vimlogo.svg" alt="Vim text editor"> </a> <!-- MySQL --> <a href="" target="_blank"><img height="24px" src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/mysql.svg" alt="MySQL" > </a>
</div>

* OS: Ubuntu 14.04 LTS
* Terminal: Bash
* Editor: VIM 7.4.52
* Language: SQL
* MySQL 8.0.27

>MySQL installation:

```bash
sudo apt update
sudo apt install mysql-server
```

> Connect to MySQL:

```bash
sudo mysql
```

> Container on demand:

```bash
service mysql start
```

## how to execute the SQL commands

```bash
root@41744616e849:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password:
ERROR 1141 (42000) at line 3: There is no such grant defined for user 'user_0d_1' on host 'localhost'
root@41744616e849:~$ echo "CREATE USER 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password:
root@41744616e849:~/$ echo "GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';" |  mysql -hlocalhost -uroot -p
Enter password:
root@41744616e849:~/$ cat 0-privileges.sql | mysql -hlocalhost -uroot -p
Enter password:
Grants for user_0d_1@localhost
GRANT SELECT, INSERT, UPDATE, DELETE, CREATE, DROP, RELOAD, SHUTDOWN, PROCESS, FILE, REFERENCES, INDEX, ALTER, SHOW DATABASES, SUPER, CREATE TEMPORARY TABLES, LOCK TABLES, EXECUTE, REPLICATION SLAVE, REPLICATION CLIENT, CREATE VIEW, SHOW VIEW, CREATE ROUTINE, ALTER ROUTINE, CREATE USER, EVENT, TRIGGER, CREATE TABLESPACE, CREATE ROLE, DROP ROLE ON *.* TO `user_0d_1`@`localhost`
GRANT APPLICATION_PASSWORD_ADMIN,AUDIT_ADMIN,BACKUP_ADMIN,BINLOG_ADMIN,BINLOG_ENCRYPTION_ADMIN,CLONE_ADMIN,CONNECTION_ADMIN,ENCRYPTION_KEY_ADMIN,FLUSH_OPTIMIZER_COSTS,FLUSH_STATUS,FLUSH_TABLES,FLUSH_USER_RESOURCES,GROUP_REPLICATION_ADMIN,INNODB_REDO_LOG_ARCHIVE,INNODB_REDO_LOG_ENABLE,PERSIST_RO_VARIABLES_ADMIN,REPLICATION_APPLIER,REPLICATION_SLAVE_ADMIN,RESOURCE_GROUP_ADMIN,RESOURCE_GROUP_USER,ROLE_ADMIN,SERVICE_CONNECTION_ADMIN,SESSION_VARIABLES_ADMIN,SET_USER_ID,SHOW_ROUTINE,SYSTEM_USER,SYSTEM_VARIABLES_ADMIN,TABLE_ENCRYPTION_ADMIN,XA_RECOVER_ADMIN ON *.* TO `user_0d_1`@`localhost`
ERROR 1141 (42000) at line 4: There is no such grant defined for user 'user_0d_2' on host 'localhost'
root@41744616e849:~/$
```

Passing arguments to the SQL commands:

```bash

```

## Autor

>```Ronald Rivero```

## Connect

<br>
<div>
<!-- Twitter -->
<a href="https://twitter.com/ralex_uy" target="_blank"> <img align="left" alt="Ronald Rivero | Twitter" src="https://img.shields.io/twitter/follow/ralex_uy?style=social"/> </a>
<!-- Linkedin -->
<a href="https://www.linkedin.com/in/ronald-rivero/" target="_blank"> <img align="left" alt="Ronald Rivero | LinkedIn" src="https://img.shields.io/badge/LinkedIn-Follow-blue?style=social&logo=linkedin"/> </a>
<!-- Github -->
<a href="https://github.com/ralexrivero/" target="_blank"> <img align="left" src="https://img.shields.io/github/followers/ralexrivero?style=social" alt="Ralex | Github"> </a>
</br>
</div>