import configparser
from random import randrange
import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType
import messagee_parser
import training_formatter
import db

config = configparser.ConfigParser()
config.read('config.ini')
token = config['VK']['token']
vk_session = vk_api.VkApi(token=token)
longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():

    # since there's no protection from SQL injections right now, bot will work only for my user_id
    if event.type == VkEventType.MESSAGE_NEW and event.from_user and event.to_me and event.user_id == 241190476:

        received_message = event.text

        if received_message.startswith('распарси') or received_message.startswith('запиши'):
            training = messagee_parser.parse_training(received_message)
            response_message = training_formatter.generate_training_description(training)

            if received_message.startswith('запиши'):
                training_date = messagee_parser.parse_date(received_message)
                for exercise in training:
                    db.add_exercise_records(event.user_id, training_date, exercise['num'], exercise['name'],
                                            exercise['details'], exercise['execution_details'])
                response_message += '\n\nТренировка записана на дату ' + training_date + '.'

        elif received_message.startswith('покажи'):
            training = messagee_parser.parse_training(received_message)
            execution_history = []
            for exercise in training:
                exercise_history = db.get_top_records(event.user_id, exercise['name'])
                execution_history.append({'exercise_name': exercise['name'],
                                          'execution_history': exercise_history
                                          })

            response_message = training_formatter.generate_execution_history_description(execution_history)
            print(execution_history)

        else:
            response_message = 'команда не распознана'

        vk.messages.send(
                user_id=event.user_id,
                random_id=randrange(10000),
                message=response_message
            )
