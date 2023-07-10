# функция вычисляет стоимость со скидкой
def getDiscount(initialPrice, procent):
    return round((initialPrice - initialPrice * procent / 100), 2)

# скидка
print('Введите значение скидки в процентах:')
procent = int(input())

# создаем массив данных
print('Введите количество продуктов:')
amountProducts = int(input())
priceProducts = []

print('Введите значения цен без скидки:')
for i in range(amountProducts):
    item = int(input())
    priceProducts.append(item)
    
print('Цены без скидки:', priceProducts)

# получаем цены со скидкой
discountPrices = []    

for i in range(amountProducts):
    discountPrices.append(getDiscount(priceProducts[i], procent))
    
print('Цены со скидкой:', discountPrices)
