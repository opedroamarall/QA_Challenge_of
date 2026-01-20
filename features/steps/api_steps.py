import requests
import uuid
from behave import given, when, then

BASE_URL = "https://demoqa.com"

#  SCENARIO: CREATE USER AND RENT BOOKS 

@given('I create a new user in the system')
def step_impl(context):
    context.user = f"pedro{str(uuid.uuid4())[:8]}"
    context.pwd = "Password123!"
    payload = {"userName": context.user, "password": context.pwd}
    resp = requests.post(f"{BASE_URL}/Account/v1/User", json=payload)
    
    assert resp.status_code == 201, f"Error in create a user: {resp.text}"
    context.user_id = resp.json()['userID']

@given('I generate an access token')
def step_impl(context):
    payload = {"userName": context.user, "password": context.pwd}
    resp = requests.post(f"{BASE_URL}/Account/v1/GenerateToken", json=payload)
    
    context.token = resp.json().get('token')
    assert resp.status_code == 200
    assert context.token is not None, "Token was not created"

@when('I list all available books')
def step_impl(context):
    resp = requests.get(f"{BASE_URL}/BookStore/v1/Books")
    assert resp.status_code == 200
    context.books = resp.json()['books']

@when('I rent two chosen books')
def step_impl(context):
    isbns = [
        {"isbn": context.books[0]['isbn']}, 
        {"isbn": context.books[1]['isbn']}
    ]
    headers = {
        'Authorization': f'Bearer {context.token}',
        'Content-Type': 'application/json'
    }
    payload = {
        "userId": context.user_id, 
        "collectionOfIsbns": isbns
    }
    resp = requests.post(f"{BASE_URL}/BookStore/v1/Books", json=payload, headers=headers)
    assert resp.status_code == 201, f"Error in rent the books: {resp.text}"

@then('the user should be authorized')
def step_impl(context):
    payload = {"userName": context.user, "password": context.pwd}
    resp = requests.post(f"{BASE_URL}/Account/v1/Authorized", json=payload)
    
    assert resp.status_code == 200
    assert resp.text == "true", f"User not authorized: {resp.text}"

@then('I should see the rented books in the user details')
def step_impl(context):
    headers = {
        'Authorization': f'Bearer {context.token}',
        'Content-Type': 'application/json'
    }
    resp = requests.get(f"{BASE_URL}/Account/v1/User/{context.user_id}", headers=headers)
    
    assert resp.status_code == 200
    rented_books = resp.json().get('books', [])
    assert len(rented_books) == 2, f"Expected 2 books, but found {len(rented_books)}"