
from backpack import generateItemList


class Thing:
    name: str
    price: int
    weight: int

    def __init__(self, price, size):
        self.price = price
        self.weight = size

    def toString(self):
        return " parameters:" + \
               " price = " + self.price.__str__() + \
               " weight = " + self.weight.__str__()


class TestScenario:
    maxSize: int
    thingsBySizeAndPrice: dict

    def __init__(self, maxSize, thingsBySizeAndPrice):
        self.maxSize = maxSize
        self.thingsBySizeAndPrice = thingsBySizeAndPrice

    def isEmpty(self):
        return not self.thingsBySizeAndPrice and not self.maxSize


def backpackWithTesting(test):
    if not test:
        backpack()
    else:
        mainLogic(test.thingsBySizeAndPrice, test.maxSize)


def backpack():
    # preparing things
    print("Введите вместимость рюкзака")
    backpackSize: int = int(input())

    print("Введите предметы и их характерестики вида: *название предмета*,*цена*,*вес* (", " - разделитель)")
    print("Для окончания перечисления введите *end*")

    thingsBySizeAndPrice = dict()

    eternalIterator: int = 1
    while eternalIterator == 1:
        thing: str = input()

        if thing == "end":
            break

        helpArray = thing.split(",")

        name: str = helpArray[0]
        price: int = int(helpArray[1])
        size: int = int(helpArray[2])
        currentThing = Thing(price, size)

        thingsBySizeAndPrice[name] = currentThing

    mainLogic(thingsBySizeAndPrice, backpackSize)


def mainLogic(thingsBySizeAndPrice, backpackSize):
    result = generateItemList(thingsBySizeAndPrice, backpackSize)
    print(result)


# ниже представлены варианты для тестирования, можно выбрать любой,
# раскоментировав его и закоментировав предыдущий ctrl + "/"

# testObject = TestScenario(35, {"Магнитофон": Thing(3000, 30), "Ноутбук": Thing(2000, 20), "Гитара": Thing(1500, 15)})

# testObject = TestScenario(4, {"Магнитофон": Thing(3000, 4), "Ноутбук": Thing(2000, 3), "Гитара": Thing(1500, 1)})

testObject = TestScenario(6, {
    "Вода": Thing(10, 3),
    "Книга": Thing(3, 1),
    "Еда": Thing(9, 2),
    "Куртка": Thing(5, 2),
    "Камера": Thing(6, 1)
})

# testObject = TestScenario(35, {
#     "Магнитофон": Thing(3000, 4),
#     "Ноутбук": Thing(2000, 3),
#     "Гитара": Thing(1500, 1),
#     "Iphone": Thing(2000, 1)
# })

backpackWithTesting(testObject)

# если нужно протестировать мануально,
# то раскоментируйте код ниже
# backpackWithTesting(0)
