import requests


def test_get():
    response = requests.get(
        "https://petstore.swagger.io/v2/pet/findByStatus?status=pending",
        headers={"accept": "application/json"}
                            )
    assert response.status_code == 200
    print(response.json())


def test_post():
    response = requests.post(
        "https://petstore.swagger.io/v2/pet",
        headers={"accept": "application/json",
                 "content-type": "application/json"},
        json={"id": 1999992323232,
              "category": {
                  "id": 0,
                  "name": "string"
              },
              "name": "doggie",
              "photoUrls": [
                  "string"
              ],
              "tags": [
                  {
                      "id": 0,
                      "name": "string"
                  }
              ],
              "status": "available"
              }
    )
    assert response.status_code == 200


def test_put():
    response = requests.put(
        "https://petstore.swagger.io/v2/pet",
        headers={"accept": "application/json"},
        json={"id": 1999992323232,
              "category": {
                  "id": 0,
                  "name": "diff"
              },
              "name": "test",
              "photoUrls": [
                  "string"
              ],
              "tags": [
                  {
                      "id": 0,
                      "name": "string"
                  }
              ],
              "status": "sold"
              }
    )
    assert response.status_code == 200


def test_get_id():
    response = requests.get("https://petstore.swagger.io/v2/pet/1999992323232")
    assert response.status_code == 200
    assert response.json().get("category").get("name") == "diff"
    assert response.json().get("name") == "test"
    assert response.json().get("status") == "sold"


def test_delete():
    response = requests.delete(
        "https://petstore.swagger.io/v2/pet/1999992323232")
    assert response.status_code == 200


def test_get_id_2():
    response = requests.get("https://petstore.swagger.io/v2/pet/1999992323232")
    assert response.status_code == 404
