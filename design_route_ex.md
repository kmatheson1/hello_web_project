## Sort Names Route Design Recipe

*Copy this design recipe template to test-drive a plain-text Flask route.*

## 1. Design the Route Signature

*Include the HTTP method, the path, and any query or body parameters.*

```
# EXAMPLE

# Request:
POST http://localhost:5001/sort-names

# With body parameters:
names=Joe,Alice,Zoe,Julia,Kieran

# Expected response (sorted list of names):
Alice,Joe,Julia,Kieran,Zoe

```

## 2. Create Examples as Tests

*Go through each route and write down one or more example responses.*

*Remember to try out different parameter values.*

*Include the status code and the response body.*

```python
# EXAMPLE

# POST /sort-name
# with Joe,Alice,Zoe,Julia,Kieran
#  Expected response (200 OK):
"""
Alice,Joe,Julia,Kieran,Zoe
"""

# POST /sort-names
# With names=Aaaaa,Aaaaaz,Aaaaab
#  Expected response (200 OK):
"""
Aaaaa,Aaaaab,Aaaaaz
"""

# POST /sort-names
# With no name
#  Expected response (200 OK):
"""
You didn't submit any names!
"""
```

## 3. Test-drive the Route

*After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.*

Here's an example for you to start with:

```python
"""
POST /sort-names
 with Aaaaa,Aaaaaz,Aaaaab
  Expected response (200 OK):
  Alice, Joe, Julia, Kieran, Zoe
"""
def test_get_home(web_client):
    response = web_client.get('/sort-name')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Joe, Julia, Kieran, Zoe'

"""
POST /sort-names
with Joe,Alice,Zoe,Julia,Kieran
  Expected response (200 OK):
  Aaaaa,Aaaaab,Aaaaaz
"""
def test_get_home(web_client):
    response = web_client.get('/sort-name')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Aaaaa, Aaaaab, Aaaaaz'

"""
POST /sort-names
with no names
  Expected response (200 OK):
  You didn't submit any names!
"""
def test_get_home(web_client):
    response = web_client.get('/sort-name')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'You didn\'t submit any names!'
```