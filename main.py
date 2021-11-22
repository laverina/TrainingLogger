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
            response_massage = training_formatter.generate_training_description(training)

            if received_message.startswith('запиши'):
                training_date = messagee_parser.parse_date(received_message)
                for i, exercise in enumerate(training):
                    exercise_num = i + 1
                    exercise_name = exercise[0]
                    exercise_details = []
                    for index in range(5):  # record up to 5 rows of exercise description
                        if len(exercise) < index + 2:
                            exercise_details.append('')
                        else:
                            exercise_details.append(exercise[index+1])
                    db.add_exercise_records(event.user_id, training_date, exercise_num, exercise[0], exercise_details)
                response_massage += '\n\nТренировка записана на дату ' + training_date

        elif received_message.startswith('подбери'):
            training = messagee_parser.parse_training(received_message)
            # todo чтение упражнений из БД, отбор последних записей
            # todo генерация ответа - training_formatter с деталями
            response_massage = 'тут будет подбор весов и параметров'

        else:
            response_massage = 'команда не распознана'

        vk.messages.send(
                user_id=event.user_id,
                random_id=randrange(10000),
                message=response_massage
            )
