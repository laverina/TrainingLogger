import message_parser


# TODO cover parse_training and remove example from docstring
def test_training_parser():
    assert message_parser.parse_training(
        """Приседания со штангой
4 по 8
35-40 кг
--40
--cкорее всего с плохой техникой, наверное нужно было поменьше

Выпады (ходьба)
16 (8+8) 3 подхода
Носок передней ноги внутрь смотрит
--с 2мя гантелями по 10 кг
"""
    ) == [
        {
            'name':               'приседания со штангой',
            'num':                '1',
            'sets':               '4',
            'reps':               '8',
            'details':            '35-40 кг',
            'execution_weight':   '40',
            'execution_details': 'cкорее всего с плохой техникой, наверное нужно было поменьше'
        },
        {
            'name':              'выпады (ходьба)',
            'num':               '2',
            'sets':              '0',
            'reps':              '0',
            'details':           '16 (8+8) 3 подхода; носок передней ноги внутрь смотрит',
            'execution_weight':  '0',
            'execution_details': 'с 2мя гантелями по 10 кг'
        }
    ]


# TODO cover parse_date and remove example from docstring
"""
    Example input:
      запиши 2021-10-21

    Output:
      2021-10-21

    Example input:
      запиши

    Output:
      current date in yyyy-mm-dd format
"""
