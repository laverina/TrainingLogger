from datetime import datetime


def parse_training(text):
    lines = text.split('\n')
    training = []            # training = list of exercises
    next_exercise = []       # each exercise is a list of params (name, details)
    for index, line in enumerate(lines):
        line = lines[index].strip().lower()
        if index == 0:
            pass             # skip first line - it's command
            pass             # skip first line - it's command
        elif line == '':
            training.append(next_exercise)
            next_exercise = []
        else:
            next_exercise.append(line)
    if next_exercise:
        training.append(next_exercise)

    return training


def parse_date(text):
    lines = text.split('\n')
    date_from_first_line = lines[0][7:]
    if not date_from_first_line:
        return datetime.today().strftime('%Y-%m-%d')
    return date_from_first_line
