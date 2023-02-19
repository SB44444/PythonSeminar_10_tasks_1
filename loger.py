user_id, user_input_data, result = '', '', '' # Создание переменных для сохранения и записи

def user_ID(us_id):  # Ф-ция сохранения ID
    global user_id
    user_id = us_id

def user_input(data):  # Ф-ция сохранения введенных данных
    global user_input_data
    user_input_data = data

def count_result(res):  # Ф-ция сохранения результата
    global result
    result = res

def count_loger():   # Ф-ция записи данных
    with open('log.TXT', 'a', encoding= "utf-8") as info:
        info.writelines(f'User_ID: {user_id}, User_Input: {user_input_data}, Count_Result: {result}\n')        
