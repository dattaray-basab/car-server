import pytest
import json
import os.path

from requests import request

overriding_directives = {"DEFAULT_SPEED": 20, "NUM_OF_SEQUENTIAL_ROUNDS": 1, "NUM_OF_SELECTION_ROUNDS": 1}

@pytest.fixture(scope="module")
def fixture_eval():
    site_addr = 'http://127.0.0.1:5000/'

    yield site_addr

def test_get_home(fixture_eval):
    site_addr = fixture_eval

    rel_addr = ''

    url = os.path.join( site_addr, rel_addr )

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = request("GET", url, headers=headers)

    print()
    print(str(response.content))
    json_object = json.loads( response.content )
    assert type(json_object) == dict
    print(f'num of items = {len(json_object)}')
    print(json_object)
    print(f'HTTP_STATUS_CODE: {response.status_code}')
    assert response.status_code == 200

def test_get_cars(fixture_eval):
    site_addr = fixture_eval

    rel_addr = 'cars'

    url = os.path.join( site_addr, rel_addr )

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    response = request("GET", url, headers=headers)

    print()
    print(str(response.content))
    json_object = json.loads( response.content )
    assert type(json_object) == list
    print(f'num of items = {len(json_object)}')
    print(json_object)
    print(f'HTTP_STATUS_CODE: {response.status_code}')
    assert response.status_code == 200

def test_post_a_car(fixture_eval):
    site_addr = fixture_eval

    rel_addr = 'cars'

    url = os.path.join( site_addr, rel_addr )

    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
    }
    car = {
        "year": 1979,
        "make": "cheyy",
        "model": "pinto",
        "owner_id": 1
    }
    payload = json.dumps(car)

    response = request("POST", url, headers=headers, data=payload)

    print(str(response.content))
    print(f'HTTP_STATUS_CODE: {response.status_code}')
    assert response.status_code == 200
    x = 1
