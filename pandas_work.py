import pandas as pd

df = pd.read_csv('NHANES.csv')

print("✅ Датафрейм загружен успешно.")
print(f"Размер датафрейма: {df.shape}")
print("\nПервые 5 строк:")
print(df.head())

df['BPAve'] = (1/3) * df['BPSysAve'] + (2/3) * df['BPDiaAve']

df['BMI'] = df['Weight'] / ((df['Height'] / 100) ** 2)

print("\n✅ Созданы столбцы 'BPAve' и 'BMI'.")

men_30_plus = df[(df['Gender'] == 'Male') & (df['Age'] >= 30)]
avg_bmi_men_30 = men_30_plus['BMI'].mean()

print(f"\n✅ Средний BMI для мужчин старше 30 лет: {avg_bmi_men_30:.2f}")

df_cleaned = df.dropna(subset=['TotChol'])

print(f"\n✅ Удалены строки без значения TotChol. Новый размер: {df_cleaned.shape}")

cholesterol_by_gender = df_cleaned.groupby('Gender')['TotChol'].mean()
print("\n📈 Средний холестерин по полу:")
print(cholesterol_by_gender)

df_cleaned['AgeGroup'] = pd.cut(df_cleaned['Age'], bins=[50, 60, 70], labels=['50-60', '60-70'])
cholesterol_by_age = df_cleaned.groupby('AgeGroup')['TotChol'].mean()
print("\n📈 Средний холестерин по возрастным группам (50-60 и 60-70):")
print(cholesterol_by_age)


if 'Depressed' in df_cleaned.columns:
    cholesterol_by_depression = df_cleaned.groupby('Depressed')['TotChol'].mean()
    print("\n📈 Средний холестерин по уровню депрессии:")
    print(cholesterol_by_depression)
else:
    print("\n⚠️ Столбец 'Depressed' отсутствует в данных. Пропускаем этот пункт.")