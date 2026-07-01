LOGIN_SUCCESS_USERS = [
    "standard_user",
    "problem_user",
    "performance_glitch_user",
    "visual_user",
    "error_user"
]

LOGIN_FAILED_USERS = [
    ("locked_out_user", "Epic sadface: Sorry, this user has been locked out."),
    ("", "Epic sadface: Username is required")
]

PASSWORD = "secret_sauce"

USER_DATA = {
    "first_name": "John",
    "last_name": "Doe",
    "postal_code": "12345",
}

CHECKOUT_NEGATIVE_CASES = [
    ("", "Doe", "12345", "Error: First Name is required"),
    ("John", "", "12345", "Error: Last Name is required"),
    ("John", "Doe", "", "Error: Postal Code is required")
]

BACKPACK = {
    "id": "sauce-labs-backpack",
    "name": "Sauce Labs Backpack"
}

BIKE_LIGHT = {
    "id": "sauce-labs-bike-light",
    "name": "Sauce Labs Bike Light"
}
