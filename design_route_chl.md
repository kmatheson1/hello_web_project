## x Route Design Recipe

*Copy this design recipe template to test-drive a plain-text Flask route.*

## 1. Design the Route Signature

*Include the HTTP method, the path, and any query or body parameters.*

```markdown
# EXAMPLE

# names route
GET /names?add=<string>


```

## 2. Create Examples as Tests

*Go through each route and write down one or more example responses.*

*Remember to try out different parameter values.*

*Include the status code and the response body.*

```python
# EXAMPLE

# GET /names?add='Kieran'
#  Expected response (200 OK):
"""
James, Leo, Kieran
"""

# GET /names?name=Hannah
#  Expected response (200 OK):
"""
James, Leo, Hannah
"""

# GET /names
#  Expected response (400 OK):
"""
No name provided
"""

# GET /names?name=Hannah,Kieran
#  Expected response (200 OK):
"""
James, Leo, Hannah, Kieran
"""

# GET /names?name=Hannah,Kieran
#  Expected response (200 OK):
"""
James, Kieran, Leo, Hannah
"""
```

## 3. Test-drive the Route

*After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour.*

Here's an example for you to start with:

```python
"""
# GET /names?add=Kieran
#  Expected response (200 OK):
James, Leo, Kieran
"""
def test_get_names_one_name(web_client):
    response = web_client.get('/names?add=Kieran')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'James, Leo, Kieran'

"""
# GET /names?name=Hannah
#  Expected response (200 OK):
James, Leo, Hannah
"""
def test_get_names_one_name_dif(web_client):
    response = web_client.get('/names?add=Hannah')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'James, Leo, Hannah'

"""# GET /names
#  Expected response (400 OK):
No name provided
"""
def test_get_names_one_name_dif(web_client):
    response = web_client.get('/name')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == 'No name provided'

"""
# GET /names?name=Hannah,Kieran
#  Expected response (200 OK):
James, Leo, Hannah, Kieran
"""
def test_get_names_multiple_name(web_client):
    response = web_client.get('/names?add=Hannah,Kieran')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'James, Leo, Hannah, Kieran'

"""
# GET /names?name=Hannah,Kieran
#  Expected response (200 OK):
James, Kieran, Leo, Hannah
"""
def test_get_names_multiple_name_sort(web_client):
    response = web_client.get('/names?add=Hannah,Kieran')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'James, Kieran, Leo, Hannah'

```