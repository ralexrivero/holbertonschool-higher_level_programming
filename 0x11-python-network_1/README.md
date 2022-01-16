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

```bash
vagrant@ubuntu-jammy:$ ./1-hbtn_header.py https://intranet.hbtn.io
dfef1727-13a2-4f8c-8f97-a08c50411724
vagrant@ubuntu-jammy:$ ./1-hbtn_header.py https://intranet.hbtn.io
dc51682b-1ddd-42d8-9cca-7363bc362144
vagrant@ubuntu-jammy:$
```

```bash
root@e382c2227c62:/# ./2-post_email.py http://0.0.0.0:5000/post_email hr@holbertonschool.com
Your email is: hr@holbertonschool.com
root@e382c2227c62:/#
```

```bash
root@e382c2227c62:/# ./3-error_code.py http://0.0.0.0:5000
Index
root@e382c2227c62:/# ./3-error_code.py http://0.0.0.0:5000/status_401Error code: 401
root@e382c2227c62:/# ./3-error_code.py http://0.0.0.0:5000/doesnt_exist
Error code: 404
root@e382c2227c62:/# ./3-error_code.py http://0.0.0.0:5000/status_500Error code: 500
root@e382c2227c62:/#
```

```bash
vagrant@ubuntu-jammy:$ ./4-hbtn_status.py | cat -e
Body response:$
        - type: <class 'str'>$
        - content: OK$
vagrant@ubuntu-jammy:$
```

```bash
vagrant@ubuntu-jammy:$ ./5-hbtn_header.py https://intranet.hbtn.io
c5c8e0f9-e4f7-4994-ba06-0f9feb8f1300
vagrant@ubuntu-jammy:$
vagrant@ubuntu-jammy:$ ./5-hbtn_header.py https://intranet.hbtn.io
fe09f7af-91f3-46c3-be63-2710cd4598d9
vagrant@ubuntu-jammy:$
```

## Author

<!-- social media and professional portfolio-->
<!-- twitter -->
[![Twitter](https://img.shields.io/twitter/follow/ralex_uy?style=social)](https://twitter.com/ralex_uy) <!-- linkedin --> [![Linkedin](https://img.shields.io/badge/LinkedIn-+21K-blue?style=social&logo=linkedin)](https://www.linkedin.com/in/ronald-rivero/) <!-- github --> [![Github](https://img.shields.io/github/followers/ralexrivero?style=social)](https://github.com/ralexrivero/) <!-- vagrant --> [![Vagrant](https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A)](https://app.vagrantup.com/ralexrivero) <!-- docker --> [![Docker](https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A)](https://hub.docker.com/u/ralexrivero)
