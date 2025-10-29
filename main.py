from sklearn.metrics import mean_absolute_percentage_error
import math


y = [3.2, 4.7, 4, 5.6, 5.6, 6.2, 5.1, 6.4]
y_hat = [4, 4.3, 4.6, 4.9, 5.2, 5.5, 5.8, 6.1]


mape_value = mean_absolute_percentage_error(y, y_hat) * 100

# Zaokrouhlení NAHORU na dvě desetinná místa
rounded_up = math.ceil(mape_value * 100) / 100

# Výsledek (jen číslo, jak chce úloha)
print(rounded_up)
