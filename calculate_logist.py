import pandas as pd
class Truck:
    def __init__(self, brand, fuel_consumption):
        self.brand=brand
        self.fuel_consumption=fuel_consumption
    def __str__(self):
        return f"---Фура марки {self.brand} (расход: {self.fuel_consumption} л/100км)---"
    def calculate_profit(self, distance, fuel_price, cargo_rate):
        fuel_need = distance / 100 * self.fuel_consumption
        fuel_cost = fuel_need * fuel_price
        total_profit = cargo_rate - fuel_cost
        return total_profit
class Refrigerator(Truck):
    def __init__(self, brand, fuel_consumption, temperature):
        super().__init__(brand, fuel_consumption)
        self.temperature = temperature
    def __str__(self):
        return f"---Рефрижератор. Фура марки:{self.brand} (расход: {self.fuel_consumption} л/100км) Температурный режим {self.temperature}---"
    def show_temp(self):
        print(f"В кузове поддерживается температура: {self.temperature}")
def main():
    print("--- Настройка грузовика ---")
    u_brand = input("Какая марка авто? ")
    try:
        f_consumption = float(input("Сколько потребляет авто на 100км? "))
    except ValueError:
        print("Ошибка! Расход должен быть числом. Ставим стандартные 30 литров.")
        f_consumption = 30.0
    choice=int(input("Какой тип авто? (1 - обычная фура, 2 - рефрижератор)"))
    if choice==1:
        my_truck = Truck(u_brand, f_consumption)
        print(my_truck)
    elif choice == 2:
        temp=int(input("Какой температурный режим?"))
        my_truck = Refrigerator(u_brand, f_consumption, temp)
        print(my_truck)
    else:
        print("Неверный выбор. Создаем обычную фуру по умолчанию.")
        my_truck = Truck(u_brand, f_consumption)
    all_trips = []    
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
            f.write(f'{my_truck} Рейс: {dist} км | Прибыль: {profit} руб.\n')
        trip_info = {
            "Марка авто": my_truck.brand,
            "Дистанция": dist,
            "Чистая прибыль": profit
        } 
        all_trips.append(trip_info)   
        print(f"Чистая прибыль с рейса выходит: {profit} руб.")
        
        answer = input("Посчитать еще один рейс? (да/нет): ")
        
        if answer.lower().startswith("н"):
            new_df = pd.DataFrame(all_trips)
            try:
                old_df = pd.read_excel('logistic_report.xlsx')
                final_df = pd.concat([old_df,new_df], ignore_index=True)
            except FileNotFoundError:
                final_df = new_df
            final_df.to_excel("logistic_report.xlsx", index=False)
            print("Отчет сохранен в logistic_report.xlsx\n" "До встречи!")
            break

if __name__ == "__main__":
    main()
