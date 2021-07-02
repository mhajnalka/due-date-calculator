from datetime import datetime, timedelta


# Starter function that prepares data for the calculate function
def starter():

    # We try processing the input value, if invalid the user can try entering it again
    try:
        input_date = datetime.strptime(input('Enter input date (YYYY-MM-DD 00:00:00): '), '%Y-%m-%d %H:%M:%S')
        if input_date.hour < 9 or input_date.hour > 17:
            raise ValueError('Input date has to be between 9AM and 5PM.')

        turnaround = int(input('Enter turnaround time (hours): '))

        if turnaround < 0:
            raise ValueError('Turnaround time cannot be a negative number.')

        calculate(input_date=input_date,
                  turnaround=turnaround)

    except ValueError as err:

        print(err)
        while True:
            answer = input('Would you like to try again? (Y/N)')
            if answer not in ('Y', 'N', 'y', 'n'):
                continue
            elif answer in ('Y', 'y'):
                starter()
            return


# Function to calculate due date based on an input date and the turnaround time
def calculate(input_date: datetime, turnaround: int):
    if turnaround < 0:
        return

    # Values that will be added to timedelta
    days_to_add = turnaround//8
    hours_to_add = turnaround % 8
    under40_weekend = 0
    over40_weekend = (turnaround // 40) * 2

    # For cases when its less then 40 hours
    if (input_date.isocalendar()[1] != (input_date + timedelta(days=days_to_add,
                                                               hours=hours_to_add)).isocalendar()[1])\
            or ((input_date + timedelta(days=days_to_add,
                                        hours=hours_to_add)).weekday() >= 5):
        under40_weekend += 2

    # Adding the calculated values to the input date in form of timedelta
    if (turnaround//40) > 0:
        due_date = input_date + timedelta(days=(days_to_add+over40_weekend),
                                          hours=hours_to_add)
    else:
        due_date = input_date + timedelta(days=(days_to_add+under40_weekend),
                                          hours=hours_to_add)
    print(f'The due date is: {due_date}')
    return due_date


# Main function that calls starter function
if __name__ == '__main__':
    starter()
