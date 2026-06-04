def simple_app(environ, start_response): #gunicorn --bind 0.0.0.0:8000 main:simple_app
    
    path = environ.get('PATH_INFO', '/')
    if path == "/api":
        status = "200 OK"
        reply = b"Happy-happy"

    else:
        status = "403 Forbidden"
        reply = b"NOPE"

    response_body = b"<html>" + reply + b"</html>"

    headers = [("Content-Type", "text/html"), ("SubServer", "wsgi"),  ("Content-Length", str(len(response_body)))]
    start_response(status, headers)

    return [response_body]


"""
root@DESKTOP-55GUE76:~# curl -vvv   http://0.0.0.0:8000/123; echo ""
*   Trying 0.0.0.0:8000...
* Connected to 0.0.0.0 (127.0.0.1) port 8000
> GET /123 HTTP/1.1
> Host: 0.0.0.0:8000
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< Server: gunicorn
< Date: Thu, 04 Jun 2026 22:42:58 GMT
< Connection: close
< Content-Type: text/html
< SubServer: wsgi
< Content-Length: 17
<
* Closing connection
<html>NOPE</html>
root@DESKTOP-55GUE76:~# curl -vvv   http://0.0.0.0:8000/api; echo ""
*   Trying 0.0.0.0:8000...
* Connected to 0.0.0.0 (127.0.0.1) port 8000
> GET /api HTTP/1.1
> Host: 0.0.0.0:8000
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: gunicorn
< Date: Thu, 04 Jun 2026 22:43:01 GMT
< Connection: close
< Content-Type: text/html
< SubServer: wsgi
< Content-Length: 24
<
* Closing connection
<html>Happy-happy</html>
"""

