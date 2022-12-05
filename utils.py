import json


def load_candidates_from_json(data):
    """
    Загрузка кандидатов.
    """
    with open(data, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_all_candidates(data):
    """
    Список всех.
    """
    result = '<h1>Все кандидаты</h1><br />'
    for name in data:
        result += f"""<p><a href="http://127.0.0.1:5000/candidate/{name['id']}">{name['name']}</a></p>
                  """
    return result


def get_candidate(id, data):
    """
    Одного кандидата по его id.
    """
    result = '<h1>'
    for name in data:
        if id == name['id']:
            result += f"""{name['name']}</h1><br />
                       <p>{name['position']}</p><br />
                       <img scr="{name['picture']}" width=200/><br />
                       <p>{name['skills']}</p>
                       """
    return result


def get_candidates_by_name(name_candidate, data):
    """
    Одного кандидата по имени.
    """
    result = '<h1>Найдено кандидатов:</h1><br />'
    for name in data:
        if name_candidate.lower() in name['name'].lower():
            result += f"""<p><a href="http://127.0.0.1:5000/candidate/{name['id']}">{name['name']}</a></p><br />
                       """
    return result


def get_by_skill(skill_name, data):
    """
    Вернет кандидатов по навыку.
    """
    sum_candidates = []
    result = f"""<h1>Найдено со скиллом {skill_name}: """
    for name in data:
        if skill_name.lower() in name['skills'].lower():
            sum_candidates.append(name['name'])

    result += f"""{len(sum_candidates)}</h1><br />"""

    for name in data:
        if skill_name.lower() in name['skills'].lower():
            result += f"""<p><a href="http://127.0.0.1:5000/candidate/{name['id']}">{name['name']}</a></p><br />"""

    return result
