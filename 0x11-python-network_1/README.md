# 0x11. Python - Network #1

<!-- ansi regular -->
```bash
███    ██ ███████ ████████ ██     ██  ██████  ██████  ██   ██ 
████   ██ ██         ██    ██     ██ ██    ██ ██   ██ ██  ██  
██ ██  ██ █████      ██    ██  █  ██ ██    ██ ██████  █████  
██  ██ ██ ██         ██    ██ ███ ██ ██    ██ ██   ██ ██  ██ 
██   ████ ███████    ██     ███ ███   ██████  ██   ██ ██   ██ 
```

## Objetives

* How to fetch internet resources with the Python package ``urllib``
* How to decode ``urllib`` body response
* How to use the Python package ``requests`` #requestsiswaysimplerthanurllib
* How to make HTTP ``GET`` request
* How to make HTTP ``POST``/``PUT``/etc. request
* How to fetch ``JSON`` resources
* How to manipulate data from an external service

## Environment

* ```Ubuntu 20.04 LTS```
* ``Ubuntu 14.04``
* ```vim```, ```VSCode```
* Bash scripting
* ```curl```
* ```python```
* ```pycodestyle``` 2.7.*
* ```PEP 8``` 1.7
* documented classes and functions

* vagrant: [Ubuntu 14 jammy 64](https://app.vagrantup.com/ubuntu/boxes/jammy64)

```bash
$ vagrant init ubuntu/jammy64
$ vagrant up
$ vagrant ssh
vagrant init ubuntu/jammy64 $
```

## Test docstrings

> `python3 -c 'print(__import__("my_module").__doc__)'`

```bash
vagrant@ubuntu-jammy:$ python3 -c 'print(__import__("0-hbtn_status").__doc__)'

fetch https://intranet.hbtn.io/status with urllib

vagrant@ubuntu-jammy:$

```

## Run the code

```bash
vagrant@ubuntu-jammy:$ ./0-hbtn_status.py | cat -e
Body response:$
        - type: <class 'bytes'>$
        - content: b'OK'$
        - utf8 content: OK$
vagrant@ubuntu-jammy:$
```

## Author

<!-- social media and professional portfolio-->
<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+21K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)
