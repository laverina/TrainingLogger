from datetime import datetime
import re


def parse_training(text):
    """
    :param text: string with description of training
    :return: list of dictionaries - each dictionary with structured exerciese decsription

    Example input:
      Приседания со штангой
      4 по 8
      35-40 кг
      --40
      --cкорее всего с плохой техникой, наверное нужно было поменьше

      Выпады (ходьба)
      16 (8+8) 3 подхода
      Носок передней ноги внутрь смотрит
      --с 2мя гантелями по 10 кг

    Output:
      [
          {
            'name':               'приседания со штангой',
            'num':                1,
            'sets':               4,
            'reps':               8,
            'details':            '35-40 кг',
            'execution_weight':   40,
            'execution_details': 'cкорее всего с плохой техникой, наверное нужно было поменьше':
          },
          {
            'name':              'выпады (ходьба)',
            'num':               2,
            'sets':              0,
            'reps':              0,
            'details':           '16 (8+8) 3 подхода; носок передней ноги внутрь смотрит',
            'execution_weight':  0,
            'execution_details': 'с 2мя гантелями по 10 кг'
          }
      ]
    """
    lines = text.split('\n')
    training = []            # training = list of exercises
    next_exercise = {}       # each exercise is a dictionary
    for index, line in enumerate(lines):
        line = lines[index].strip().lower()
        if index == 0:
            pass             # skip first line - it's command
        elif line == '':
            if next_exercise:
                next_exercise['details'] = '; '.join(next_exercise['details'])
                next_exercise['execution_details'] = '; '.join(next_exercise['execution_details'])
                training.append(next_exercise)
            next_exercise = {}
        else:
            if not next_exercise:                        # first line is always name
                next_exercise['name'] = line
                next_exercise['num'] = 1 + len(training)
                next_exercise['sets'] = 0
                next_exercise['reps'] = 0
                next_exercise['details'] = []
                next_exercise['execution_weight'] = 0
                next_exercise['execution_details'] = []
            elif line.startswith('--'):                  # lines starting with -- contain execution details
                if not next_exercise['execution_weight'] and re.search('^\\d+[.|,]*\\d+$', line[2:].strip()):
                    next_exercise['execution_weight'] = line[2:].strip()
                else:
                    next_exercise['execution_details'].append(line[2:])
            else:                                        # other lines contain training plan details
                if not next_exercise['sets'] and re.search('^\\d+[ ]*по[ ]*\\d+$', line.strip()):
                    next_exercise['sets'] = line.split('по')[0].strip()
                    next_exercise['reps'] = line.split('по')[1].strip()
                else:
                    next_exercise['details'].append(line)

    if next_exercise:
        next_exercise['details'] = '; '.join(next_exercise['details'])
        next_exercise['execution_details'] = '; '.join(next_exercise['execution_details'])
        training.append(next_exercise)

    return training


def parse_date(text):
    lines = text.split('\n')
    date_from_first_line = lines[0][7:]
    if not date_from_first_line:
        return datetime.today().strftime('%Y-%m-%d')
    return date_from_first_line
