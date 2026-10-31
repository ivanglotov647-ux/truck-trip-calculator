def calculate_profit(distance, fuel_price, cargo_rate, fuel_per_100=30):
    fuel_need = distance / 100 * fuel_per_100
    fuel_cost = fuel_need * fuel_price
    total_profit = cargo_rate - fuel_cost
    return total_profit

def main():
    print("---Калькулятор рейса---")
    while True:
        try:
            dist = float(input("Какая дистанция рейса (км)? "))
            fuel_p = float(input("Какая цена топлива за литр? "))
            rate = float(input("Какая ставка за перевозку? "))
        except ValueError:
            print("Ошибка ввода. Введите числа.")
            continue

        profit = calculate_profit(dist, fuel_p, rate)
        
        with open('logistic.txt', 'a', encoding='utf-8') as f:
            f.write(f'Рейс: {dist} км | Прибыль: {profit} руб.\n')
            
        print(f"Чистая прибыль с рейса выходит: {profit} руб.")
        
        answer = input("Посчитать еще один рейс? (да/нет): ")
        
        if answer.lower().startswith("н"):
            print("До встречи!")
            break

if __name__ == "__main__":
    main()