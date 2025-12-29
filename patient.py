from datetime import date
import matplotlib.pyplot as plt

class Patient:
    def __init__(self, name, birth_date, diagnosis):
        self.name = name
        self.birth_date = birth_date
        self.diagnosis = diagnosis
        self.temperatures = []

    def get_age(self):
        today = date.today()
        age = today.year - self.birth_date.year
        if today.month < self.birth_date.month or \
           (today.month == self.birth_date.month and today.day < self.birth_date.day):
            age -= 1
        return age

    def add_temperature(self):
        while True:
            try:
                temp = float(input("Введите температуру тела (0 для завершения): "))
                if temp == 0:
                    break
                self.temperatures.append(temp)
                print(f"Температура {temp}°C добавлена.")
            except ValueError:
                print("Пожалуйста, введите число.")

    def calculate_average_temperature(self):
        if not self.temperatures:
            return None
        return sum(self.temperatures) / len(self.temperatures)

    def show_temperature_curve(self):
        if not self.temperatures:
            print("Нет данных о температуре.")
            return

        print(f"\nТемпературная кривая для {self.name}:")
        for i, temp in enumerate(self.temperatures, 1):
            print(f"  Измерение {i}: {temp}°C")

        avg = self.calculate_average_temperature()
        print(f"\nСредняя температура: {avg:.2f}°C")

    def show_temperature_curve(self):
        if not self.temperatures:
            print("Нет данных о температуре.")
            return
    
        plt.figure(figsize=(10, 5))
        plt.plot(range(1, len(self.temperatures) + 1), self.temperatures, marker='o', linestyle='-', color='red')
        plt.title(f"Температурная кривая: {self.name}")
        plt.xlabel("Измерение")
        plt.ylabel("Температура (°C)")
        plt.grid(True)
        plt.axhline(y=36.6, color='green', linestyle='--', label='Норма (36.6°C)')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    patient = Patient(
        name="Иван Иванов",
        birth_date=date(1990, 5, 15),
        diagnosis="Грипп"
    )

    print(f"Пациент: {patient.name}")
    print(f"Диагноз: {patient.diagnosis}")
    print(f"Возраст: {patient.get_age()} лет")

    print("\n--- Ввод температур ---")
    patient.add_temperature()

    patient.show_temperature_curve()
