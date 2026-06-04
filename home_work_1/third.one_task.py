# 3. два wsgi приложения
#    1. первое возвращает "Hello" и статус "200 OK" если запрос идёт на
#       /api, и "Error" с статусом "403 Forbidden" иначе

def simple_app(environ, start_response): #gunicorn --bind 0.0.0.0:8000 main:simple_app
    headers = [("Content-Type", "text/plain")]

    path = environ.get('PATH_INFO', '/')

    if path == "/api":
        status = "200 OK"
        start_response(status, headers)
        return [b"Happy-happy"]

    else:
        status = "403 Forbidden"
        start_response(status, headers)
        return [b"NOPE"]
    
"""
curl -vvv   http://0.0.0.0:8000/api; echo ""
*   Trying 0.0.0.0:8000...
* Connected to 0.0.0.0 (127.0.0.1) port 8000
> GET /api HTTP/1.1
> Host: 0.0.0.0:8000
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/1.1 200 OK
< Server: gunicorn
< Date: Thu, 04 Jun 2026 21:44:24 GMT
< Connection: close
< Transfer-Encoding: chunked
< Content-Type: text/plain
<
* Closing connection
Happy-happy

curl -vvv   http://0.0.0.0:8000/123; echo ""
*   Trying 0.0.0.0:8000...
* Connected to 0.0.0.0 (127.0.0.1) port 8000
> GET /123 HTTP/1.1
> Host: 0.0.0.0:8000
> User-Agent: curl/8.5.0
> Accept: */*
>
< HTTP/1.1 403 Forbidden
< Server: gunicorn
< Date: Thu, 04 Jun 2026 21:44:18 GMT
< Connection: close
< Transfer-Encoding: chunked
< Content-Type: text/plain
<
* Closing connection
NOPE
"""
