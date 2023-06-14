# Flask Project for Uktob.ai

## Getting Started

To run the Flask project locally, follow these steps:
1. Clone the repository:

```bash
    git clone https://github.com/mehdirazajaffri/uktob.ai.git
    cd server
```
or
- Create Virtual Enviornment if you wish
```bash
    python -m venv venv
    source venv/bin/activate  # For Unix/Linux
    venv\Scripts\activate  # For Windows
```

``` bash
    pip install -r requirements.txt
```

```bash
    export FLASK_APP=app.py  # For Unix/Linux
    set FLASK_APP=app.py  # For Windows
```

```bash
    flask run
    or
    python app.py
```

The application will be accessible at http://localhost:5000.

## APIs Documentation
### Sum Endpoint
- Endpoint: /sum
- Method: POST
- Description: Accepts a JSON object containing a list of numbers and returns their sum.
- Request Payload:

-   ```json
        {
        "numbers": [1, 2, 3, 4, 5]
        }
    ```

### Concatenate Endpoint
- Endpoint: /concatenate
- Method: POST
- Description: Accepts a JSON object containing a list of strings and returns their concatenated result.
- Request Payload:

```json
    {
  "strings": ["Hello", " ", "World!"]
    }
```

- Response
```json

{
  "concatenated": "Hello World!"
}

```

### User Registration Endpoint
- Endpoint: /register
- Method: POST
- Description: Registers a new user with a username and password.
- Request Payload:

```json
    {
  "username": "john",
  "password": "pass123"
    }
```
- Response
```json
{
  "message": "Registration successful."
}
```

### User Login Endpoint
- Endpoint: /login
- Method: POST
- Description: Logs in a user with a username and password.
- Request Payload:

```json

{
  "username": "mehdiraza",
  "password": "pass123"
}
```

- Response
```json

{
  "message": "Access granted."
}

or

{
  "message": "Access denied."
}

```

### APIs with cURL

Here are some examples of how to use the APIs using cURL:

```bash
curl -X POST -H "Content-Type: application/json" -d '{"numbers": [1, 2, 3, 4, 5]}' http://localhost:5000/sum

curl -X POST -H "Content-Type: application/json" -d '{"strings": ["Hello", " ", "World!"]}' http://localhost:5000/concatenate

curl -X POST -H "Content-Type: application/json" -d '{"username": "mehdiraza", "password": "pass123"}' http://localhost:5000/register

curl -X POST -H "Content-Type: application/json" -d '{"username": "mehdiraza", "password": "pass123"}' http://localhost:5000/login
```



# React App for Uktob.ai

In the project directory, you can run:

```bash
    cd frontend
    npm install
```

### `npm start`

```bash
    npm start
```

App will be available at http://localhost:3000/