import sqlite3


def update_lists_to_len(list, desired_length):
    len_diff = desired_length - len(list)
    for i in range(len_diff):
        list.append('')
    return list


def add_exercise_records(user_id, training_date, exercise_num, exercise_name, exercise_details,
                         execution_details=['', '', '', '', '']):
    cursorobj = con.cursor()
    exercise_details = update_lists_to_len(exercise_details, 5)
    execution_details = update_lists_to_len(execution_details, 5)
    cursorobj.execute("""
                    INSERT INTO exercises VALUES(
                        """ + str(user_id) + """,
                        '""" + str(training_date) + """',
                        """ + str(exercise_num) + """,
                        '""" + str(exercise_name) + """',
                        '""" + str(exercise_details[0]) + """',
                        '""" + str(exercise_details[1]) + """',
                        '""" + str(exercise_details[2]) + """',
                        '""" + str(exercise_details[3]) + """',
                        '""" + str(exercise_details[4]) + """',
                        '""" + str(execution_details[0]) + """',
                        '""" + str(execution_details[1]) + """',
                        '""" + str(execution_details[2]) + """',
                        '""" + str(execution_details[3]) + """',
                        '""" + str(execution_details[4]) + """'
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
            'details': shorten_list_to_last_filled(row[4:8]),
            'execution_details': shorten_list_to_last_filled(row[9:13]),
        }
        executions.append(execution)
    return executions


con = sqlite3.connect('data\exercises.db')
