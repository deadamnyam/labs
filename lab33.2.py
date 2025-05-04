# Импорт необходимых библиотек
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

# 1. Загрузка данных elnino (актуальный способ)
elnino_data = sm.datasets.elnino.load()
df = pd.DataFrame(elnino_data.data, columns=elnino_data.names)

# 2. Преобразование и фильтрация данных (1990-2010)
df['YEAR'] = pd.to_datetime(df['YEAR'], format='%Y')
df = df[(df['YEAR'].dt.year >= 1990) & (df['YEAR'].dt.year <= 2010)]

# 3. Настройка стиля графиков
plt.style.use('seaborn-v0_8')
plt.figure(figsize=(12, 8))

# 4. Построение графиков для всех временных рядов
for column in df.columns[1:]:  # Пропускаем столбец 'YEAR'
    plt.plot(df['YEAR'], df[column], label=column, linewidth=2)

# 5. Настройка оформления
plt.title('Динамика показателей El Niño (1990-2010)', fontsize=14)
plt.xlabel('Год', fontsize=12)
plt.ylabel('Значения', fontsize=12)
plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True, linestyle='--', alpha=0.7)
plt.tight_layout()

# 6. Сохранение и отображение
plt.savefig('elnino_1990_2010.png', dpi=300, bbox_inches='tight')
plt.show()