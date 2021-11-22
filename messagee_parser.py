from datetime import datetime


def parse_training(text):
    lines = text.split('\n')
    training = []            # training = list of exercises
    next_exercise = {}       # each exercise is a dictionary
    for index, line in enumerate(lines):
        line = lines[index].strip().lower()
        if index == 0:
            pass             # skip first line - it's command
        elif line == '':
            if next_exercise:
                training.append(next_exercise)
            next_exercise = {}
        else:
            if not next_exercise:
                next_exercise['name'] = line              # first line is always name
                next_exercise['num'] = 1 + len(training)  # order number from current list length
                next_exercise['details'] = []
                next_exercise['execution_details'] = []
            else:
                # record up to 5 rows with execution details marker
                if line.startswith('--') and len(next_exercise['execution_details']) < 5:
                    next_exercise['execution_details'].append(line[2:])
                # and up to 5 without
                elif len(next_exercise['details']) < 5:
                    next_exercise['details'].append(line)

    if next_exercise:
        training.append(next_exercise)

    return training


def parse_date(text):
    lines = text.split('\n')
    date_from_first_line = lines[0][7:]
    if not date_from_first_line:
        return datetime.today().strftime('%Y-%m-%d')
    return date_from_first_line
