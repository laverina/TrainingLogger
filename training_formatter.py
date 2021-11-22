def generate_training_description(training):
    message = 'тренировка состоит из упражнений:\n\n'

    for exercise in training:
        message += str(exercise['num']) + '. ' + exercise['name']
        if exercise['details']:
            message += '\n -  ' + ' | '.join(exercise['details'])
        if exercise['execution_details']:
            message += '\n -- ' + ' | '.join(exercise['execution_details'])
        message += '\n\n'
    return message
