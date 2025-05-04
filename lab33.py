# 1. Импорт библиотек
from sklearn.datasets import load_wine  # для загрузки данных
import matplotlib.pyplot as plt  # для графиков

# 2. Загрузка данных
wine = load_wine()
data = wine.data  # таблица с данными
target = wine.target  # классы (0, 1, 2)

# 3. Выбор столбцов:
# alcohol - первый столбец (индекс 0)
# proline - последний столбец (индекс 12)
alcohol = data[:, 0]
proline = data[:, 12]

# 4. Настройка графика
plt.figure(figsize=(10, 6))

# 5. Цвета для каждого класса
colors = ['red', 'purple', 'yellow']
labels = ['Class 0', 'Class 1', 'Class 2']

# 6. Рисуем точки
for i in range(3):
    plt.scatter(
        alcohol[target == i],  # X для класса i
        proline[target == i],  # Y для класса i
        c=colors[i],          # цвет
        label=labels[i]       # подпись
    )

# 7. Подписи осей и заголовок
plt.xlabel('Alcohol')
plt.ylabel('Proline')
plt.title('Alcohol vs Proline in Wine Dataset')
plt.legend()  # показываем легенду

# 8. Сохранение графика (опционально)
plt.savefig('wine_plot.png')

# 9. Показываем график
plt.show()
