# JSON based query Parser

This is an academic project for Internet Programming Lab, Department of Computer Science and Engineering, University of Dhaka

## Installation
```
git clone https://github.com/maruf03/iplab_query_parser.git
cd iplab_query_parser
```

### Windows
```
python.exe -m venv venv
venv\Scripts\activate.ps1
pip install -r requirements.txt
```

### *nix (MacOS, Linux, BSD)
```
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Run
```
python main.py
```

## Configuration
Modify config.json file
```
{
    "sqlite": {
        "driver": "sqlite3",
        "url": "db/database.db"
    },
    "mysql": {
        "host": "localhost",
        "user": "root",
        "password": "",
        "database": "test"
    },
    "postgres": {
        "host": "localhost",
        "user": "postgres",
        "password": "",
        "database": "test"
    }
}
```

## Query Format
The queries are pure JOSN objects. There are 5 types of queries.

### CREATE Table Query
```
{
    "database": "sqlite", // other alternatives are "postgres" and "mysql"
    "type": "create",  
    "model": {
        "name": "Student",
        "schema": {
            "name": "string",
            "age": "int",
            "address": "string",
            "phone": "string",
            "email": "string"
        }
    }
}
```

### INSERT Row Query
```
{
    "database": "sqlite",
    "type": "add",
    "model": {
        "name": "Student",
        "data": {
            "name": "Alif",
            "age": 25,
            "address": "Dhaka",
            "phone": "01922216159",
            "email": "maruf.alif03@gmail.com"
        }
    }
}
```

### GET Row Query
```
{
    "database": "sqlite",
    "type": "get",
    "model": {
        "name": "Student",
        "where": {
            "name": "Alif"
        },
        "select": {
            "name": true,
            "age": true,
            "address": true
        }
    }
}
```

### UPDATE Row Query
```
{
    "database": "sqlite",
    "type": "update",
    "model": {
        "name": "Student",
        "data": {
            "age": 22
        },
        "where": {
            "id": 1
        }
    }
}
```

### DELETE Row Query
```
{
    "database": "sqlite",
    "type": "delete",
    "model": {
        "name": "Student",
        "where": {
            "name": "Alif"
        }
    }
}
```

## Author
```
Maruf Al Alif Khan
```
