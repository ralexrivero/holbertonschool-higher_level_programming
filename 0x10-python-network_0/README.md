# 0x10. Python - Network #0

## Objetives

* What a URL is
* What HTTP is
* How to read a URL
* The scheme for a HTTP URL
* What a domain name is
* What a sub-domain is
* How to define a port number in a URL
* What a query string is
* What an HTTP request is
* What an HTTP response is
* What HTTP headers are
* What the HTTP message body is
* What an HTTP request method is
* What an HTTP response status code is
* What an HTTP Cookie is
* How to make a request with cURL
* What happens when you type google.com in your browser (Application level)

## Environment

* ```vi```, ```vim```, ```emacs```
* ```Ubuntu 20.04 LTS```
* Bash scripting
* ```curl```
* ```python```
* ```pycodestyle``` 2.7.*
* documented classes and functions

## Execute the code

```bash
root@ead65a4ee2aa:#./0-body_size.sh 0.0.0.0:5000
10
root@ead65a4ee2aa:#
```

```bash
root@ead65a4ee2aa:#./1-body.sh 0.0.0.0:5000/route_1 ; echo ""
Route 2
root@ead65a4ee2aa:#
```

```bash
root@ead65a4ee2aa:#./2-delete.sh 0.0.0.0:5000/route_3 ; echo ""
I'm a DELETE request
root@ead65a4ee2aa:#
```

```bash
root@ead65a4ee2aa:#./3-methods.sh 0.0.0.0:5000/route_4
OPTIONS, HEAD, PUT
root@ead65a4ee2aa:#
```

```bash
root@ead65a4ee2aa:# ./4-header.sh 0.0.0.0:5000/route_5 ; echo ""
Hello Holberton School!
root@ead65a4ee2aa:#

```

```bash
root@ead65a4ee2aa:# ./5-post_params.sh 0.0.0.0:5000/route_6 ; echo ""
POST params:
	email: test@gmail.com
	subject: I will always be here for PLD
root@ead65a4ee2aa:#
```

```bash
root@ead65a4ee2aa:#0x10-python-network_0$ ./6-main.py
6
4
2
None
2
4
root@ead65a4ee2aa:#
```

```bash
root@ead65a4ee2aa:# ./100-status_code.sh 0.0.0.0:5000 ; echo ""
200
root@ead65a4ee2aa:#
root@ead65a4ee2aa:#  ./100-status_code.sh 0.0.0.0:5000/nop ; echo ""
404
root@ead65a4ee2aa:#

```

```bash
0# cat my_json_0
{
    "name": "John Doe",
    "age": 33
}
root@ead65a4ee2aa:# ./101-post_json.sh 0.0.0.0:5000/route_json my_json_0 ; echo ""
Valid JSON
root@ead65a4ee2aa:# cat my_json_1
I'm a JSON! really!
root@ead65a4ee2aa:# ./101-post_json.sh 0.0.0.0:5000/route_json my_json_1 ; echo ""
Not a valid JSON
root@ead65a4ee2aa:#
root@ead65a4ee2aa:# cat my_json_2
{
    "name": "John Doe",
    "age": 33,
}
root@ead65a4ee2aa:# ./101-post_json.sh 0.0.0.0:5000/route_json my_json_2 ; echo ""
Not a valid JSON
root@ead65a4ee2aa:#
```

```bash
root@ead65a4ee2aa:# ./102-catch_me.sh ; echo ""
You got me!
root@ead65a4ee2aa:#
```

## Author

<!-- social media and professional portfolio-->
<div>
<!-- twiter -->
<a href="https://twitter.com/ralex_uy" target="_blank"> <img align="left" alt="Ronald Rivero | Twitter" src="https://img.shields.io/twitter/follow/ralex_uy?style=social"/> </a>
<!-- linkedin -->
<a href="https://www.linkedin.com/in/ronald-rivero/" target="_blank"> <img align="left" alt="Ronald Rivero | LinkedIn" src="https://img.shields.io/badge/LinkedIn-+21K-blue?style=social&logo=linkedin"/> </a>
<!-- github -->
<a href="https://github.com/ralexrivero/" target="_blank"> <img align="left" src="https://img.shields.io/github/followers/ralexrivero?style=social" alt="Ralex | Github"> </a>
<!-- vagrant -->
<a href="https://app.vagrantup.com/ralexrivero" target="_blank"> <img align="left" src="https://img.shields.io/static/v1?label=&message=Vagrant%20Profile&color=1868F2&logo=vagrant&labelColor=2F333A" alt="Vagrantup profile"></a>
<!-- docker -->
<a href="https://hub.docker.com/u/ralexrivero" target="_blank"> <img align="left" src="https://img.shields.io/static/v1?label=&message=Docker%20Profile&color=2496ED&logo=Docker&labelColor=2F333A" alt="Docker profile"></a>

</br>
</div>
