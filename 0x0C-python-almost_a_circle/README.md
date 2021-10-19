# 0x0C. Python - Almost a circle
```
       _                     _                  _          _      
      | |                   | |                (_)        | |     
  __ _| |_ __ ___   ___  ___| |_    __ _    ___ _ _ __ ___| | ___ 
 / _` | | '_ ` _ \ / _ \/ __| __|  / _` |  / __| | '__/ __| |/ _ \
| (_| | | | | | | | (_) \__ \ |_  | (_| | | (__| | | | (__| |  __/
 \__,_|_|_| |_| |_|\___/|___/\__|  \__,_|  \___|_|_|  \___|_|\___|
                                                                  
                                                                  
```
## Learning Objectives
### General

- What is Unit testing and how to implement it in a large project
- How to serialize and deserialize a Class
- How to write and read a JSON file
- What is *args and how to use it
- What is **kwargs and how to use it
- How to handle named arguments in a function

## Environment
<div>
<a  href="https://www.cprogramming.com/"  target="_blank"><img  height="24px"  src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/python-logo-inkscape.svg"  alt="C programming language"  ></a> <a  href="https://ubuntu.com/"  target="_blank"><img  height="24px"  src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/ubuntu-icon.svg"  alt="C programming language"></a> <a  href="https://www.vim.org/"  target="_blank"><img  height="24px"  src="https://raw.githubusercontent.com/ralexrivero/xelar_theme_profile/main/icons/Vimlogo.svg"  alt="C programming language"></a>
</div>

- Language: Python
- OS: Ubuntu 14.04 LTS
- Editor: VIM 7.4.52
- Compiler: Python 3.4.3
- Style guidelines: [pycodestyle (version 2.7.*)](https://pypi.org/project/pycodestyle/)

## Documentation
- Modules: ```python3 -c 'print(__import__("my_module").__doc__)'```
- Classes: ```python3 -c 'print(__import__("my_module").MyClass.__doc__)'```
- Functions (inside and outside a class): ```python3 -c 'print(__import__("my_module").my_function.__doc__)'```
and ```python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'```

## Python Unit Tests

- unittest module
- File extension ``` .py ```
- Files and folders star with ```test_```
- Organization:for ```models/base.py```, unit tests in: ```tests/test_models/test_base.py```
- Execution command: ```python3 -m unittest discover tests```
- or: ```python3 -m unittest tests/test_models/test_base.py```

## Turtle graphics module

- [Turtle graphics module](https://docs.python.org/3.0/library/turtle.html)
- install: ```sudo apt-get install python3-tk```
- Make GUI available outside vagran machine, add this line in Vagrantfile: ```config.ssh.forward_x11 = true```

## Autor

```
Ronald Rivero
```

### Connect me!

<br>
<div>

<a  href="https://twitter.com/ralex_uy"  target="_blank">  <img  align="left"  alt="Ronald Rivero | Twitter"  src="https://img.shields.io/twitter/follow/ralex_uy?style=social"/>  </a>

<a  href="https://www.linkedin.com/in/ronald-rivero/"  target="_blank">  <img  align="left"  alt="Ronald Rivero | LinkedIn"  src="https://img.shields.io/badge/LinkedIn-+19K-blue?style=social&logo=linkedin"/>  </a>

<a  href="https://github.com/ralexrivero/"  target="_blank">  <img  align="left"  src="https://img.shields.io/github/followers/ralexrivero?style=social"  alt="Ralex | Github">  </a>
</br>
</div>