
from flask import Flask

app = Flask(__name__)

app.secret_key = "Trust the process"

DATABASE = "exam_python_db"