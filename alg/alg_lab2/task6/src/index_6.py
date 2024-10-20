def find_maximum_subarray(prices):
    max_profit = 0
    current_profit = 0
    start = 0
    end = 0
    s = 0
    for i in range(1, len(prices)):
        current_profit += prices[i] - prices[i - 1]
        if current_profit < 0:
            current_profit = 0
            s = i
        if current_profit > max_profit:
            max_profit = current_profit
            start = s
            end = i

    return max_profit, start, end
def main():
    dates = []
    prices = []
    with open("input.txt", 'r') as file:
        name_firm = file.readline().strip()
        while (line := file.readline().strip()) != "":
            arr_file = line.split(" ")
            date = arr_file[0]
            price_str = arr_file[1]
            price = int(price_str)
            dates.append(date)
            prices.append(price)
    profit,buy_date, sell_date = find_maximum_subarray(prices)
    print(profit,buy_date, sell_date)
    period = "Сентябрь 2024"
    with open('output.txt', 'w') as f:
        f.write(f"Фирма: {name_firm}\n")
        f.write(f"Срок: {period}\n")
        f.write(f"Дата покупки: {dates[buy_date]}\n")
        f.write(f"Дата продажи: {dates[sell_date]}\n")
        f.write(f"Максимальная прибыль: {profit}\n")

if __name__ == "__main__":
    main()
