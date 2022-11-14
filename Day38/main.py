import requests
from datetime import datetime

URL = ""


def show_records(num_of_items):
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()
    #print(data)
    workouts = data['workouts']
    if len(workouts) < num_of_items:
        start_idx = 0
    else:
        start_idx = -num_of_items

    #workouts_for_10days = workouts[start_idx:]
    workouts_for_10rows = workouts[start_idx:]
    for workout in workouts_for_10rows:
        print(workout)


exercise = 'push up'
quantity = 20


def write_today_workout(excercise: str, quantity: int):
    today = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    date = today.split()[0]
    time = today.split()[1]

    print(excercise)
    print(quantity)
    today_workout = {
        'workout': {
            'date': date,
            'time': time,
            'exercise': exercise,
            'quantity': quantity
        }
    }

    response = requests.post(URL, json=today_workout)
    print(response.text)


# Get one row data
def get_object(object_id):
    response = requests.get(f'{URL}/{object_id}')
    response.raise_for_status()
    workout = response.json()['workout']
    print(workout)
    return workout


def update_object(object_id, workout):
    print(f"id: {object_id}")
    print(f'workout: {workout}')
    data = {'workout': workout}
    response = requests.put(f'{URL}/{object_id}', json=data)
    response.raise_for_status()


# MAIN
loop_end = False
while not loop_end:
    # TODO#1: print menu.
    menu = int(input("\nWhich job do you want? : \n"
                     "1. show 10 day's records\n"
                     "2. Write today's record\n"
                     "3. Change record\n"
                     "4. Exit)\n"))
    if menu == 1:
        num_of_items_to_show = 10
        show_records(num_of_items_to_show)
    elif menu == 2:
        exercise = input("What exercise did you do?: ")
        quantity = int(input("How many?: "))
        write_today_workout(exercise, quantity)
    elif menu == 3:
        object_id = int(input("Which object do you want to change? input 'object id': "))
        # get and show original data(row).
        workout = get_object(object_id)
        # prompt and get quantity
        quantity = int(input("Input quantity: "))
        workout['quantity'] = quantity
        del workout['id']

        update_object(object_id, workout)

    elif menu == 4:
        loop_end = True



