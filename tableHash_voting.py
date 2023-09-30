# Простая тестовая программа для проверки голосования человека на выбоварх

voted = {}


def check_voter(name):
    if voted.get(name):
        print('kick them out!')
    else:
        voted[name] = True
        print('let them vote!')


check_voter('Josh')
check_voter('Max')
check_voter('Lara')

print(voted)

check_voter('Max')
check_voter('Lara')
check_voter('Tom')

print(voted)
