from behave import given, when, then
import requests


@given("the API is available")
def step_api_available(context):
    context.base_url = "https://jsonplaceholder.typicode.com"


@when("I send a GET request for post 1")
def step_get_post(context):
    context.response = requests.get(
        f"{context.base_url}/posts/1"
    )


@then("the response status code should be 200")
def step_status_200(context):
    assert context.response.status_code == 200


@when('I create a post with title "{title}", body "{body}" and user id {user_id}')
def step_create_post(context, title, body, user_id):

    payload = {
        "title": title,
        "body": body,
        "userId": int(user_id)
    }

    context.response = requests.post(
        f"{context.base_url}/posts",
        json=payload
    )


@then("the response status code should be 201")
def step_status_201(context):
    assert context.response.status_code == 201