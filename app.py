from utils import *
from flask import Flask, render_template

candidates = load_candidates_from_json('candidates.json')

app = Flask(__name__)


@app.route("/")
def page_index():
    candidate = candidates
    return render_template('list.html', candidate=candidate)


@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    candidate = get_candidate(uid, candidates)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<uid>")
def page_search(uid):
    candidate = get_candidates_by_name(uid, candidates)
    return render_template('search.html', candidate=candidate, count=len(candidate))


@app.route("/skill/<uid>")
def page_skill(uid):
    candidate = get_by_skill(uid, candidates)
    return render_template('skill.html', candidate=candidate, count=len(candidate), uid=uid)


app.run()
