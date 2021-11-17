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
cat 0-list_databases.sql | mysql -hlocalhost -uroot -p
cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p
```

Passing arguments to the SQL commands:

```bash
cat 3-list_tables.sql | mysql -hlocalhost -uroot -p mysql
cat 4-first_table.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
cat 6-list_values.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
cat 7-insert_value.sql | mysql -hlocalhost -uroot -p hbtn_0c_0
cat 8-count_89.sql | mysql -hlocalhost -uroot -p hbtn_0c_0 | tail -1
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