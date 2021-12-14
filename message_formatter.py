def generate_training_description(training):
    """
    :param training: list of dictionaries, each one - with exercise details.
    :return: formatted text to be presented to the user
    """
    message = 'Тренировка состоит из упражнений:\n\n'

    for exercise in training:
        message += str(exercise['num']) + '. ' + exercise['name']
        if exercise['sets'] and exercise['reps']:
            message += '\n -  ' + str(exercise['sets']) + ' по ' + str(exercise['reps'])
        if exercise['details']:
            message += '\n - ' + exercise['details']
        if exercise['execution_weight']:
            message += '\n -- ' + str(exercise['execution_weight']) + ' кг'
        if exercise['execution_details']:
            message += '\n -- ' + exercise['execution_details']
        message += '\n\n'

    return message


def generate_execution_history_description(history):
    """
    :param history: list of dictionaries, each one - with exercise execution details
    :return: formatted text to be presented to the user
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
