from utils import *
from flask import Flask, render_template

candidates = load_candidates_from_json('candidates.json')

app = Flask(__name__)


@app.route("/")
def page_index():
    candidates = get_all_candidates(candidates)
    return render_template('list.html', candidates=candidates)


@app.route("/candidate/<int:uid>")
def page_candidate(uid):
    candidate = get_candidate(uid, candidates)
    return render_template('card.html', candidate=candidate)


@app.route("/search/<uid>")
def page_search(uid):
    candidates = get_candidates_by_name(uid, candidates)
    return render_template('search.html', candidates=candidates, count=len(candidates))


@app.route("/skill/<uid>")
def page_skill(uid):
    candidates = get_by_skill(uid, candidates)
    return render_template('skill.html', candidates=candidates, count=len(candidates))


app.run()
