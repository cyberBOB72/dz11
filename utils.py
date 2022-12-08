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
    return load_candidates_from_json(data)


def get_candidate(id, data):
    """
    Одного кандидата по его id.
    """
    for name in data:
        if id == name['id']:
            return name
    return 'Not Found'


def get_candidates_by_name(name_candidate, data):
    """
    Одного кандидата по имени.
    """
    result = []
    for name in data:
        if name_candidate.lower() in name['name'].lower():
            result.append(name)
    return result


def get_by_skill(skill_name, data):
    """
    Вернет кандидатов по навыку.
    """
    result = []
    for name in data:
        skills = name['skills'].lower().split(', ')
        if skill_name.lower() in skills:
            result.append(name)
    return result 
