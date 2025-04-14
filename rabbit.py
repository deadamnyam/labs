class Rabbit:
  # Функция для вычисления количества пар кроликов через n месяцев  при максимальном возрасте m месяцев
 def rabbit_pairs(n, m):
     # Создаем массив dp для хранения количества  кроликов каждого возраста (от 1 до m месяцев)
    dp = [0] * (m + 1)
    dp[1] = 1  # Изначально есть 1 пара новорожденных кроликов (возраст 1 месяц)
    for month in range(2, n + 1):  # Проходим по каждому месяцу от 2 до n
        new_dp = [0] * (m + 1)  # Создаем новый временный массив для следующего месяца
        for age in range(1, m): #Старение кроликов на 1 месяц
            new_dp[age + 1] += dp[age]
        for age in range(2, m + 1): #Размножение кроликов (каждая взрослая пара = 1 новая пара)
            new_dp[1] += dp[age]
        dp = new_dp  # Обновляем основной массив
    total_pairs = sum(dp) # Суммируем все пары кроликов всех возрастов
    return total_pairs
 n = 33
 m = 2
 print(rabbit_pairs(n, m))

