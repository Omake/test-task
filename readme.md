# Project guide

## Short description

This project provides API methods for creating, deleting, modifying as well as viewing users.


## Installation and run

Place the project files in your directory. Then install the necessary dependencies. By using commands:


```sh
pip install -r requirements.txt
```

Please use this command to start the server:

```sh
python manage.py runserver
```

## Usage

The methods of this project require token authentication.
> Note: The POST method used to create a user does not require authentication.

### Methods

| Method | URL | Request Method | Description |
| ------ | ------ | ------ | ------ | 
| Authenticate | http://127.0.0.1:8000/api-token-auth/ | POST |  Used to get a token
| Create | http://127.0.0.1:8000/api/v1/users/ | POST | User creation
| Get users | http://127.0.0.1:8000/api/v1/users/ | GET | Get users list
| Get user | http://127.0.0.1:8000/api/v1/users/<User_ID>/ | GET | Get user info by ID
| Patch | http://127.0.0.1:8000/api/v1/users/<User_ID>/ | PATCH |Changes user attributes (It is preferable to use to change a single field)
| Put | http://127.0.0.1:8000/api/v1/users/<User_ID>/ | PUT | Changes user attributes
| Delete | http://127.0.0.1:8000/api/v1/users/<User_ID>/ | DELETE | Changes the value of the is_active field to "0" and deactivates the user.

### Authentication

Send your username and password to receive your token

URL: http://127.0.0.1:8000/api-token-auth/
Request Method: POST

```sh
{
    "username": "my_test_username",
    "password": "AHJGSDAGSJD2"
}
```

Successful response:

```sh
{
    "token": "3046faade6342c0784e609429c77e73d8f61d79b"
}
```

To use token just add an Authorization parameter to your header

```sh
Authorization: Token 3046faade6342c0784e609429c77e73d8f61d79b
```

### Create

Request Parameters

username - Char
> 150 characters or fewer. Letters, digits and @/./+/-/_ only.


first_name - Char
> 30 characters or fewer.

last_name - Char
> 150 characters or fewer.

password - Char
> 8 - 128 characters. Must contain at least one capital letter and a one number

is_active - Bool
> True, for activated user



URL: http://127.0.0.1:8000/api/v1/users/

Request Method: POST

```sh
{
    "username": "my_test_username",
    "first_name": "test",
    "last_name": "user",
    "password": "AHJGSDAGSJD2",
    "is_active": true
}
```


Successful response:

```sh
{
    "id": 23,
    "username": "my_test_username",
    "first_name": "test",
    "last_name": "user",
    "is_active": true,
    "last_login": null,
    "is_superuser": false
}
```

### Get users

Used to get a list of all users

URL: http://127.0.0.1:8000/api/v1/users/

Request Method: GET


```sh
[
    {
        "id": 1,
        "username": "new_test_user2sss",
        "first_name": "VASYA",
        "last_name": "ivanovvv",
        "is_active": true,
        "last_login": null,
        "is_superuser": true
    },
    {
        "id": 2,
        "username": "test_usr",
        "first_name": "kirill",
        "last_name": "ivanov",
        "is_active": true,
        "last_login": null,
        "is_superuser": false
    },
    ...
]
```


### Get user

It is used to get information about the user by ID.


URL: http://127.0.0.1:8000/api/v1/users/<user_id>

Request Method: GET

Successful response:

```sh
{
    "id": 3,
    "username": "test_usr33",
    "first_name": "VASYA",
    "last_name": "ivanovvv",
    "is_active": false,
    "last_login": null,
    "is_superuser": false
}
```

### Patch

Request Parameters

username - Char
> 150 characters or fewer. Letters, digits and @/./+/-/_ only.


first_name - Char
> 30 characters or fewer.

last_name - Char
> 150 characters or fewer.

password - Char
> 8 - 128 characters. Must contain at least one capital letter and a one number

is_active - Bool
> True, for activated user



URL: http://127.0.0.1:8000/api/v1/users/<user_id>

Request Method: PATCH

```sh
{
    "username": "my_test_username",
    "first_name": "test",
    "last_name": "user",
    "password": "AHJGSDAGSJD2",
    "is_active": true
}
```


Successful response:

```sh
{
    "id": 23,
    "username": "my_test_username",
    "first_name": "test",
    "last_name": "user",
    "is_active": true,
    "last_login": null,
    "is_superuser": false
}
```

### Put

Request Parameters

username - Char
> 150 characters or fewer. Letters, digits and @/./+/-/_ only.


first_name - Char
> 30 characters or fewer.

last_name - Char
> 150 characters or fewer.

password - Char
> 8 - 128 characters. Must contain at least one capital letter and a one number

is_active - Bool
> True, for activated user



URL: http://127.0.0.1:8000/api/v1/users/<user_id>

Request Method: PUT

```sh
{
    "username": "my_test_username",
    "first_name": "test",
    "last_name": "user",
    "password": "AHJGSDAGSJD2",
    "is_active": true
}
```


Successful response:

```sh
{
    "id": 23,
    "username": "my_test_username",
    "first_name": "test",
    "last_name": "user",
    "is_active": true,
    "last_login": null,
    "is_superuser": false
}
```

### Delete

Used to set is_active to False and deactivating user



URL: http://127.0.0.1:8000/api/v1/users/<user_id>

Request Method: DELETE

Successful response:

```sh
HTTP Code 204
```