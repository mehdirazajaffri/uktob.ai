# Flask Project

This is a Flask project that provides various APIs for performing specific tasks.

## Getting Started

To run the Flask project locally, follow these steps:

1. Clone the repository:

```bash
   cd server
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
```

The application will be accessible at http://localhost:5000.

# APIs Documentation
Sum Endpoint
Endpoint: /sum
Method: POST
Description: Accepts a JSON object containing a list of numbers and returns their sum.
Request Payload:

```json
    {
    "numbers": [1, 2, 3, 4, 5]
    }
```