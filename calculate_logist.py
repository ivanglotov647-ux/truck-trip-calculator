class Truck:
    def __init__(self, brand, fuel_consumption):
        self.brand=brand
        self.fuel_consumption=fuel_consumption
    def calculate_profit(self, distance, fuel_price, cargo_rate):
        fuel_need = distance / 100 * self.fuel_consumption
        fuel_cost = fuel_need * fuel_price
        total_profit = cargo_rate - fuel_cost
        return total_profit
def main():
        print("--- Настройка грузовика ---")
        u_brand = input("Какая марка авто? ")
        try:
            f_consumption = float(input("Сколько потребляет авто на 100км? "))
        except ValueError:
            print("Ошибка! Расход должен быть числом. Ставим стандартные 30 литров.")
            f_consumption = 30.0
        
        my_truck = Truck(u_brand, f_consumption)
        print(f"--- Калькулятор рейса для {my_truck.brand} ---")
        while True:
            try:
                dist = float(input("Какая дистанция рейса (км)? "))
                fuel_p = float(input("Какая цена топлива за литр? "))
                rate = float(input("Какая ставка за перевозку? "))
            except ValueError:
                print("Ошибка ввода. Введите числа.")
                continue
            profit = my_truck.calculate_profit(dist, fuel_p, rate)
        
            with open('logistic.txt', 'a', encoding='utf-8') as f:
                f.write(f'Рейс: {dist} км | Прибыль: {profit} руб.\n')
            
            print(f"Чистая прибыль с рейса выходит: {profit} руб.")
        
            answer = input("Посчитать еще один рейс? (да/нет): ")
        
            if answer.lower().startswith("н"):
                print("До встречи!")
                break

if __name__ == "__main__":
    main()
