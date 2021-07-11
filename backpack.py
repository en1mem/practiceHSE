
def getWeightAndPriceCollection(thingsBySizeAndPrice):
    weights = [thingsBySizeAndPrice[item].weight for item in thingsBySizeAndPrice]
    prices = [thingsBySizeAndPrice[item].price for item in thingsBySizeAndPrice]

    return weights, prices


def generateTable(thingsBySizeAndPrice, backpackSize):
    weight, price = getWeightAndPriceCollection(thingsBySizeAndPrice)
    tableSize = len(price)  # находим размеры таблицы

    # создаём таблицу из нулевых значений
    nullTable = [[0 for realTable in range(backpackSize + 1)] for nullTable in range(tableSize + 1)]

    for i in range(tableSize + 1):
        for a in range(backpackSize + 1):
            if i == 0 or a == 0:
                nullTable[i][a] = 0

            elif weight[i - 1] <= a:
                nullTable[i][a] = max(price[i - 1] + nullTable[i - 1][a - weight[i - 1]], nullTable[i - 1][a])

            else:
                nullTable[i][a] = nullTable[i - 1][a]
    return nullTable, weight, price


def generateItemList(thingsBySizeAndPrice, backpackSize):
    nullTable, weight, value = generateTable(thingsBySizeAndPrice, backpackSize)
    tableSize = len(value)
    res = nullTable[tableSize][backpackSize]
    tempOfSize = backpackSize
    listOfItems = []

    for i in range(tableSize, 0, -1):
        if res <= 0:
            break
        if res == nullTable[i - 1][tempOfSize]:
            continue
        else:
            listOfItems.append((weight[i - 1], value[i - 1]))
            res -= value[i - 1]
            tempOfSize -= weight[i - 1]

    result = []

    # по ключам формируем итоговый результат
    for search in listOfItems:
        for key, value in thingsBySizeAndPrice.items():
            if (value.weight, value.price) == search:
                result.append(key + value.toString())

    return result
