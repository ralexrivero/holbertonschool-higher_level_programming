# 0x14. JavaScript - Web scraping

## General


* JavaScript programming
* SON data
* Request and fetch API
* Read and write a file using fs module

## Environment

* OS: ``ubuntu``
* IDE: ``Vim``, ``VS Code``
* Language: ``JavaScript``
* Style guidelines: ``semistandard`` ``Airbnb style``
* Node.js 

* Shebang: ``#!/usr/bin/node``


### install Node 10

```bash
$ curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
$ sudo apt-get install -y nodejs
```

### Install semi-standard

```bash
$ sudo npm install semistandard --global
```

### Install request module and use it

```bash
$ sudo npm install request --global
$ export NODE_PATH=/usr/lib/node_modules
```

## Run the code

> reading file and parsing it with Node.js

```bash
ralex@ralex-nb:$ cat cisfun 
C is super fun!
ralex@ralex-nb:$ ./0-readme.js cisfun
C is super fun!

ralex@ralex-nb:$ ./0-readme.js doesntexist
{ [Error: ENOENT: no such file or directory, open 'doesntexist']
  errno: -2,
  code: 'ENOENT',
  syscall: 'open',
  path: 'doesntexist' }
ralex@ralex-nb:$ 
```

> write to a file

```bash
ralex@ralex-nb:$ ./1-writeme.js my_file.txt "Python is cool"
ralex@ralex-nb:$ cat my_file.txt ; echo ""
Python is cool
ralex@ralex-nb:$ 
```



## Author
<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+22K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)