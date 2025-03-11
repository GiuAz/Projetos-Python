import matplotlib.pyplot as plt
import numpy as np

X = np.linspace(0, 10, 100)
Y = X ** 2

plt.plot(X, Y, color='red', linestyle='--', label='Y = X^2')
plt.title('Grafico em Linhas Simples')
plt.xlabel('EIXO X')
plt.ylabel('EIXO Y')
plt.grid(True)
plt.show()
