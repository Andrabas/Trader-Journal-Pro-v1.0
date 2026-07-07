trades = []
profits = []

print("TRADER JOURNAL PRO")
print("Журнал угод запущено")

trade = ""

while trade != "stop":
    trade = input("Введіть угоду або stop: ")

    if trade != "stop":
        profit = float(input("Введіть прибуток або збиток: ").replace(",", "."))
        trades.append(trade)
        profits.append(profit)

print("----- ЖУРНАЛ УГОД -----")

number = 1

win_trades = 0
loss_trades = 0
for i in range(len(trades)):
    print(f"{number}. {trades[i]} | P/L: {profits[i]}")

    if profits[i] > 0:
        win_trades = win_trades + 1

    elif profits[i] < 0:
        loss_trades = loss_trades + 1

    number = number + 1

print("Усього угод:", len(trades))

total_profit = sum(profits)
print("Загальний результат:", total_profit)

if total_profit > 0:
    print("Результат дня: прибутковий день")

elif total_profit < 0:
    print("Результат дня: збитковий день")

else:
    print("Результат дня: беззбитковий день")  

print("Прибуткових угод: ", win_trades)
print("Збиткових угод:", loss_trades)

win_rate = win_trades / len(trades) * 100
win_rate = round(win_rate, 2)
print("Win Rate:", win_rate, "%")

average_profit = total_profit / len(trades)
average_profit = round(average_profit, 2)
print("Середній результат на угоду:", average_profit)
  
best_trade = max(profits)
worst_trade = min(profits)

print("Найкраща угода:", best_trade)
print("Найгірша угода:", worst_trade)

