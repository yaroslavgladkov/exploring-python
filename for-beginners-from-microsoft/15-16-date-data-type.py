from datetime import datetime, timedelta

birthday = '11/11/1111'
#birthday = input('When is your birthday (dd/mm/yyyy)? ')

birthday_date = datetime.strptime(birthday, '%d/%m/%Y')

print('Birthday:' + str(birthday_date))

one_day = timedelta(days=1)
birthday_eve = birthday_date - one_day
print('Day before birthday: ' + str(birthday_eve))

one_week = timedelta(weeks=1)
birthday_eve = birthday_date - one_week
print('Week before birthday: ' + str(birthday_eve))

now = datetime.now()

print(f'Day: {now.day}, Hour: {now.hour}, Minute: {now.minute}')
