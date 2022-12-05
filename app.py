from utils import *
from flask import Flask

candidates = load_candidates_from_json('candidates.json')

app = Flask(__name__)


@app.route("/")
def page_index():
    return get_all_candidates(candidates)


@app.route("/candidate/<int:uid>")
def page_candidates(uid):
    return get_candidate(uid, candidates)


@app.route("/search/<uid>")
def page_search(uid):
    return get_candidates_by_name(uid, candidates)


@app.route("/skill/<uid>")
def page_skill(uid):
    return get_by_skill(uid, candidates)


app.run()
