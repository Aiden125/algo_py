money = int(input())
arr = list(map(int, input().split()))

jhStock = 0
jhMoney = money
smStock = 0
smMoney = money

upCount = 0
downCount = 0

def sell(money, stock, todayPrice):
    money += stock * todayPrice
    stock = 0
    return [money, stock]

def buy(money, stock, todayPrice):
    stock += int(money / todayPrice)
    money = money % todayPrice
    return [money, stock]

for i in range(0, len(arr)):
    if i > 0 and arr[i-1] < arr[i]:
        upCount += 1
        downCount = 0
    elif i > 0 and arr[i-1] > arr[i]:
        downCount += 1
        upCount = 0

    if upCount >= 3:
        smMoney, smStock = sell(smMoney, smStock, arr[i])
    if downCount >= 3:
        smMoney, smStock = buy(smMoney, smStock, arr[i])
    
    if i+1 != len(arr):
        jhMoney, jhStock = buy(jhMoney, jhStock, arr[i])
    elif i+1 == len(arr):
        jhMoney, jhStock = sell(jhMoney, jhStock, arr[i])
        smMoney, smStock = sell(smMoney, smStock, arr[i])

if jhMoney > smMoney:
    print('BNP')
elif jhMoney < smMoney:
    print('TIMING')
else:
    print("SAMESAME")