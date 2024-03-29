import requests

# Base URL of your FastAPI application
BASE_URL = "http://mater.systems:8084"


def test_get_candies():
    response = requests.get(f"{BASE_URL}/candies")
    assert response.status_code == 200
    print("GET /candies test passed.")


def test_get_categories():
    response = requests.get(f"{BASE_URL}/categories")
    assert response.status_code == 200
    print("GET /categories test passed.")


def test_get_candies_by_category(category="chocolate"):
    response = requests.get(f"{BASE_URL}/candies/category/{category}")
    assert response.status_code == 200
    print(f"GET /candies/category/{category} test passed.")


def test_get_candies_by_keyword(keyword="sugar"):
    response = requests.get(f"{BASE_URL}/candies/keyword/{keyword}")
    assert response.status_code == 200
    print(f"GET /candies/keyword/{keyword} test passed.")


def test_get_candies_by_name(name="mars"):
    response = requests.get(f"{BASE_URL}/candies/name/{name}")
    assert response.status_code == 200
    print(f"GET /candies/name/{name} test passed.")


def test_get_candies_by_price_range(low=1.0, high=5.0):
    response = requests.get(
        f"{BASE_URL}/candies/price/", params={"low": low, "high": high}
    )
    assert response.status_code == 200
    print("GET /candies/price test passed.")


def test_get_candy_by_id(id=1):
    response = requests.get(f"{BASE_URL}/candy/{id}")
    assert response.status_code == 200
    print(f"GET /candy/{id} test passed.")


def test_get_candy_image(id=1):
    response = requests.get(f"{BASE_URL}/image/{id}")
    assert response.status_code == 200
    print(f"GET /image/{id} test passed.")


def test_update_candy():
    candy_id = 1
    key = "name"
    value = "New Candy Name"
    response = requests.put(
        f"{BASE_URL}/candy/", params={"id": candy_id, "key": key, "value": value}
    )
    assert response.status_code == 200
    print("PUT /candy/ test passed.")


def test_add_new_candy():
    new_candy = {"name": "Test Candy", "category": "Test Category", "price": 1.99}
    response = requests.post(f"{BASE_URL}/candy/", json=new_candy)
    assert response.status_code == 200
    print("POST /candy/ test passed.")


def test_delete_candy(id=2):
    response = requests.delete(f"{BASE_URL}/candy/{id}")
    assert response.status_code == 200
    print(f"DELETE /candy/{id} test passed.")


def run_tests():
    test_get_candies()
    test_get_categories()
    # Add other tests here
    # You may want to add a pause or setup/teardown steps for creating/deleting test data
    test_add_new_candy()  # Example: Add a candy to test deletion
    test_delete_candy(
        id=2
    )  # Ensure this ID matches the candy added by test_add_new_candy


if __name__ == "__main__":
    run_tests()
