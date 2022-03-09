# Echo Server

Simple echo of http query/results and returns a 503 response.

## Usage

### Example:

```sh
docker run -it -p 8001:80 --rm bnef/echo-server
```

Then running: `curl -k -X POST -H "Arbitrary:Header" -H 'Content-Type: application/json' -d {aaa:bbb} http://localhost:8001/hello-world\?test\=2` would result in:

```txt
Note: Unnecessary use of -X or --request, POST is already inferred.
*   Trying ::1...
* TCP_NODELAY set
* Connected to localhost (::1) port 8001 (#0)
> POST /hello-world?test=2 HTTP/1.1
> Host: localhost:8001
> User-Agent: curl/7.64.1
> Accept: */*
> Arbitrary:Header
> Content-Type: application/json
> Content-Length: 9
> 
* upload completely sent off: 9 out of 9 bytes
* HTTP 1.0, assume close after body
< HTTP/1.0 200 OK
< Server: SimpleHTTP/0.6 Python/3.8.3
< Date: Tue, 14 Jul 2020 23:31:09 GMT
< Connection: close
< Content-Type: text/html;charset=utf-8
< Content-Length: 446
< 
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
        "http://www.w3.org/TR/html4/strict.dtd">
<html>
    <head>
        <meta http-equiv="Content-Type" content="text/html;charset=utf-8">
        <title>Error response</title>
    </head>
    <body>
        <h1>Error response</h1>
        <p>Error code: 200</p>
        <p>Message: OK.</p>
        <p>Error code explanation: 200 - Request fulfilled, document follows.</p>
    </body>
</html>
* Closing connection 0
```

Meanwhile in the original window:

```
ERROR:root:=POST===========================================================
ERROR:root:Host: localhost:8001
User-Agent: curl/7.64.1
Accept: */*
Arbitrary: Header
Content-Type: application/json
Content-Length: 9


ERROR:root:b'{aaa:bbb}'
172.17.0.1 - - [14/Jul/2020 23:31:09] code 200, message OK
172.17.0.1 - - [14/Jul/2020 23:31:09] "POST /hello-world?test=2 HTTP/1.1" 200 -
ERROR:root:=END============================================================
```

### Change response code

Change the response code by adding a parameter:

```
docker run -it -p 8001:80 --rm bnef/echo-server 500
```

### Help / Usage instructions

```txt
usage: [-h] [-p PORT] [response]

positional arguments:
  response

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT
```

## Build

```sh
docker build -t bnef/echo-server .
```

## Push

```sh
docker push bnef/echo-server
```
