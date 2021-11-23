import sqlite3


def add_exercise_records(user_id, training_date, exercise_num, exercise_name, sets, reps,
                         details, execution_weight, execution_details):
    cursorobj = con.cursor()
    print("""
                    INSERT INTO exercises VALUES(
                        """ + str(user_id) + """,
                        '""" + str(training_date).strip() + """',
                        """ + str(exercise_num) + """,
                        '""" + str(exercise_name) + """',
                        """ + str(sets) + """,
                        """ + str(reps) + """,
                        '""" + str(details) + """',
                        """ + str(execution_weight) + """,
                        '""" + str(execution_details) + """'
                    )
                    """)
    con.commit()


def shorten_list_to_last_filled(lst):
    for index in range(len(lst)):
        if not ''.join(lst[index:]):
            break
    return list(lst[:index])


def get_top_records(user_id, exercise_name, amount=3):
    cursorobj = con.cursor()
    cursorobj.execute("""
        SELECT * FROM (SELECT * FROM exercises WHERE user_id = """ + str(user_id) + """ AND name = '"""
                      + str(exercise_name) + """' ORDER BY date DESC) LIMIT """ + str(amount) + """
    """)
    rows = cursorobj.fetchall()

    executions = []

    for row in rows:
        execution = {
            'date': row[1],
            'sets': row[4],
            'reps': row[5],
            'details': row[6],
            'execution_weight': row[7],
            'execution_details': row[8]
        }
        executions.append(execution)
    return executions


con = sqlite3.connect('data\exercises.db')
