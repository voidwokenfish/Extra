class Goods:
    def __init__(self, name, cost, amount):
        self.name = name
        self.cost = int(cost)
        self.amount = int(amount)


goods = []
with open("./list_of_goods.txt", "r", encoding="utf-8") as file:
    for line in file.readlines():
        gugugaga = line.split(':')
        aboba = Goods(name=gugugaga[0],cost=gugugaga[1],amount=gugugaga[2])
        goods.append(aboba)


class Storage:
    def __init__(self, goods: list):
        self.goods = goods

our_storage = Storage(goods)



mean = 0
count_all = 0
summ = 0
max_price = 0
min_price = 100000
max_index = 0
min_index = 0
set_goods = set()

for good in our_storage.goods:
    price = good.cost
    summ += price
    count_all += 1
    if price > 100:
        set_goods.add(good.name)
    if price > max_price:
        max_price = price
        max_index = our_storage.goods.index(good)
        print(f'максимальная цена: {max_price}')
        print(f'индекс максимальной цены {max_index}')
    if price < min_price:
        min_price = price
        min_index = our_storage.goods.index(good)
        print(f'минимальная цена: {min_price}')
        print(f'индекс минимальной цены: {min_index}')

dict_goods = {}
dict_goods['mean'] = summ / count_all
dict_goods['summ'] = summ
dict_goods['count_all'] = count_all

print(dict_goods)
print(set_goods)


def work_with_list(list_goods, is_max_min):
    list_result = []
    max = 0
    min = 999999

    for good in list_goods:
        price = good.cost

        if price > max:
                max = price

        if price < min:
                min = price

    if is_max_min:
            for good in list_goods:
                price = good.cost
                name = good.name

                if price == max:
                    list_result.append(name)
    else:
            for good in list_goods:
                price = good.cost
                name = good.name

                if price == min:
                    list_result.append(name)

    return list_result


list_goods_max = work_with_list(our_storage.goods, is_max_min=True)
list_goods_min = work_with_list(our_storage.goods, is_max_min=False)
print(list_goods_max)
print(list_goods_min)