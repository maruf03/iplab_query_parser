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

## Author
```
Maruf Al Alif Khan
```
