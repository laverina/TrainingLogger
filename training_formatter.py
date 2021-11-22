def generate_training_description(training):
    message = 'Тренировка состоит из упражнений:\n\n'

    for exercise in training:
        message += str(exercise['num']) + '. ' + exercise['name']
        if exercise['details']:
            message += '\n -  ' + ' | '.join(exercise['details'])
        if exercise['execution_details']:
            message += '\n -- ' + ' | '.join(exercise['execution_details'])
        message += '\n\n'
    return message


def generate_execution_history_description(history):
    message = 'последние записи об упражнениях:\n\n'

    print(history)

    for exercise in history:
        message += exercise['exercise_name']
        for record in exercise['execution_history']:
            message += '\n' + record['date']
            if record['details']:
                message += '\n -  ' + ' | '.join(record['details'])
            if record['execution_details']:
                message += '\n -- ' + ' | '.join(record['execution_details'])

        message += '\n\n'
    return message
