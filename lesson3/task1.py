from string import digits
while True:
    country = input ("Enter a country")
    if country == 'exit':
        print('stop the program')
        break

    if country.isalpha():
        print('you have entered:',country.capitalize())