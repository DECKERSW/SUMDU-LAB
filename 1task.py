import numpy as np
import matplotlib.pyplot as plt

# Задання діапазону x
x = np.linspace(-3, 3, 1000)

# Обчислення значень функції Y(x)
y = 2**x * np.sin(10*x)

# Побудова графіка
plt.plot(x, y, color='blue', linewidth=2, linestyle='solid', label=r'$Y(x) = 2^x \cdot \sin(10x)$')

# Додавання позначень осей та назви графіка
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Графік функції $Y(x) = 2^x \cdot \sin(10x)$')
plt.grid(True)

# Додавання легенди
plt.legend()

# Показ графіка
plt.show()
