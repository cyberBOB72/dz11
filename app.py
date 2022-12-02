from utils import *
from flask import Flask

candidates = load_candidates_from_json('candidates.json')

app = Flask(__name__)

@app.route("/")
def page_index():
  return get_all(response_json)

app.run()
