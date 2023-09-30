#Нерешенный пример с рекурсией, программа не работает
class Object:
    def __init__(self, object):
        self.object = object

    def is_a_box(self):
        if self.object == 'box':
            return True
        else:
            False

    def is_a_key(self):
        if self.object == 'key':
            return True
        else:
            False


# !!! Работающая рекурсивная функция !!!
# рекурсивная функция для поиска ключа в коробке
def look_for_key(box):
    for item in box:
        if item.is_a_box():
            look_for_key(item)
        elif item.is_a_key():
            return print("found the key!")
        else:
            return print("the key wasn't found")


object1 = Object('box')
object2 = object1[Object('key')]

look_for_key(object2)