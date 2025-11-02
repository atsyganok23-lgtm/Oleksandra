#Task 4
#Створити лист із днями тижня.
#В один рядок (ну або як завжди) створити словник виду: {1: "Monday", 2:...
#Також в один рядок або як вдасться створити зворотний словник {"Monday": 1,
weekdays = {i+1: weekday for i,
    weekday in enumerate(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])}
print ("Словник 1", weekdays)

weekdays = {weekday: i+1 for i, weekday in enumerate(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])}
print ("Словник 2", weekdays)