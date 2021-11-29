def generate_training_description(training):
    """
    :param training: list of dictionaries, each one - with exercise details.
    :return: formatted text to be presented to the user


    Example input:
    [
      {
        'num': 1,
        'name': 'приседания со штангой',
        'sets': 4,
        'reps': 8,
        'details': '35-40 кг',
        'execution_weight': 40,
        'execution_details': 'cкорее всего с плохой техникой, наверное нужно было поменьше'
      },
      {
        'num': 2,
        'name': 'выпады (ходьба)',
        'sets': 0,
        'reps': 0,
        'details': '16 (8+8) 3 подхода; носок передней ноги внутрь смотрит',
        'execution_weight': 0,
        'execution_details': 'с 2мя гантелями по 10 кг'
      }
    ]


    Output:
      Тренировка состоит из упражнений:
      1. приседания со штангой'
      4 по 8
      - 35-40 кг
      -- 40 кг
      -- cкорее всего с плохой техникой, наверное нужно было поменьше

      2. выпады (ходьба)
      - 16 (8+8) 3 подхода; носок передней ноги внутрь смотрит
      -- с 2мя гантелями по 10 кг

    """
    message = 'Тренировка состоит из упражнений:\n\n'

    for exercise in training:
        message += str(exercise['num']) + '. ' + exercise['name']
        if exercise['sets'] and exercise['reps']:
            message += '\n -  ' + exercise['sets'] + ' по ' + exercise['reps']
        if exercise['details']:
            message += '\n - ' + exercise['details']
        if exercise['execution_weight']:
            message += '\n -- ' + exercise['execution_weight'] + ' кг'
        if exercise['execution_details']:
            message += '\n -- ' + exercise['execution_details']
        message += '\n\n'
    return message


def generate_execution_history_description(history):
    """
    :param history: list of dictionaries, each one - with exercise execution details
    :return: formatted text to be presented to the user

    Example input:
    [
      {
        'exercise_name': 'приседания со штангой',
        'execution_history': [
          {
            'date': 2021-11-21,
            'sets': 4,
            'reps': 10,
            'details': '',
            'executions_weight': 35,
            'execution_details': '',
          },
          {
            'date': 2021-11-14,
            'sets': 5,
            'reps': 5,
            'details': '',
            'executions_weight': 40,
            'execution_details': 'последний подход тяжело',
          },
        ]
      },
      {
        'exercise_name': 'выпады (ходьба)',
        'execution_history': [
          {
            'date': 2021-11-21,
            'sets': 0,
            'reps': 0,
            'details': '16 (8+8) 3 подхода; носок передней ноги внутрь смотрит',
            'executions_weight': 0,
            'execution_details': 'с 2мя гантелями по 10 кг',
          }
        ]
      },
    ]

    Output:
      Последние записи об упражнениях:

      приседания со штангой
      2021-11-21
       - 4 по 10
       -- 35 кг
      2021-11-21
       - 5 по 5
       -- 40 кг [последний подход тяжело]

       выпады (ходьба)
       2021-11-21
       # TODO FIX current code doesn't show information on details if sets and reps are not provided
       # TODO FIX current code doesn't show information on execution details if weight not provided
    """
    message = 'Последние записи об упражнениях:\n\n'
    for exercise in history:
        message += exercise['exercise_name']
        for record in exercise['execution_history']:
            message += '\n' + record['date']
            if record['sets'] and record['reps']:
                message += '\n - ' + str(record['sets']) + ' по ' + str(record['reps'])
                if record['details']:
                    message += ' [' + record['details'] + ']'
            if record['execution_weight']:
                message += '\n --' + str(record['execution_weight']) + ' кг'
                if record['execution_details']:
                    message += ' [' + record['execution_details'] + ']'

        message += '\n\n'
    return message
