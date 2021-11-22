def generate_training_description(training):
    message = 'тренировка состоит из упражнений:\n\n'

    for index, exercise in enumerate(training):
        message += str(index + 1) + '. ' + ' | '.join(exercise) + '\n'

    return message
