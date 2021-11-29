import pytest
import training_formatter


def test_basic_case():
    assert training_formatter.generate_training_description([
      {
        'num': 1,
        'name': 'приседания со штангой',
        'sets': 4,
        'reps': 8,
        'details': '',
        'execution_weight': 40,
        'execution_details': ''
      }
    ]) == """Тренировка состоит из упражнений:\n\n1. приседания со штангой\n -  4 по 8\n -- 40 кг\n\n"""

