import pytest

# === Example Code Below ===

"""
GET /emoji
"""
def test_get_emoji(web_client):
    response = web_client.get("/emoji")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == ":)"

# === End Example Code ===

# Test Driving Routes Exercises

"""
When: I make a POST request to /count_vowels
And: I send "eee" as the body parameter text
Then: I should get a 200 response with 3 in the message
"""
def test_post_count_vowels_eee(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eee'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 3 vowels in "eee"'

"""
When: I make a POST request to /count_vowels
And: I send "eunoia" as the body parameter text
Then: I should get a 200 response with 5 in the message
"""
def test_post_count_vowels_eunoia(web_client):
    response = web_client.post('/count_vowels', data={'text': 'eunoia'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 5 vowels in "eunoia"'

"""
When: I make a POST request to /count_vowels
And: I send "mercurial" as the body parameter text
Then: I should get a 200 response with 4 in the message
"""
def test_post_count_vowels_mercurial(web_client):
    response = web_client.post('/count_vowels', data={'text': 'mercurial'})
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'There are 4 vowels in "mercurial"'

"""
POST /sort-names
with Aaaaa,Aaaaaz,Aaaaab
Expected response (200 OK):
Alice, Joe, Julia, Kieran, Zoe
"""
def test_post_sort_names_1(web_client):
    response = web_client.post('/sort-names', data={
        'names': 'Alice,Joe,Julia,Kieran,Zoe'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Alice, Joe, Julia, Kieran, Zoe'

"""
POST /sort-names
with Joe,Alice,Zoe,Julia,Kieran
Expected response (200 OK):
Aaaaa,Aaaaab,Aaaaaz
"""
def test_post_sort_names_2(web_client):
    response = web_client.post('/sort-names', data={
        'names': 'Aaaaa,Aaaaab,Aaaaaz'
    })
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Aaaaa, Aaaaab, Aaaaaz'

"""
POST /sort-names
with no names
Expected response (200 OK):
You didn't submit any names!
"""
def test_post_sort_names_3(web_client):
    response = web_client.post('/sort-names')
    assert response.status_code == 400
    assert response.data.decode('utf-8') == "You didn't submit any names!"

# Test Driving Routes Challenge

"""
# GET /names?add=Kieran
#  Expected response (200 OK):
James, Leo, Kieran
"""
def test_get_names_one_name(web_client):
    response = web_client.get('/names?add=Kieran')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'James, Kieran, Leo'

"""
# GET /names?name=Hannah
#  Expected response (200 OK):
James, Leo, Hannah
"""
def test_get_names_one_name_dif(web_client):
    response = web_client.get('/names?add=Hannah')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hannah, James, Leo'

"""# GET /names
#  Expected response (400 OK):
No name provided
"""
def test_get_names_no_names(web_client):
    response = web_client.get('/names')
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
    assert response.data.decode('utf-8') == 'Hannah, James, Kieran, Leo'

"""
# GET /names?name=Hannah,Kieran
#  Expected response (200 OK):
James, Kieran, Leo, Hannah
"""
def test_get_names_multiple_name_sort(web_client):
    response = web_client.get('/names?add=Hannah,Kieran')
    assert response.status_code == 200
    assert response.data.decode('utf-8') == 'Hannah, James, Kieran, Leo'