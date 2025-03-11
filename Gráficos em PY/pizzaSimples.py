import matplotlib.pyplot as plt
import numpy as np

labels = ['Despesas', 'Lucro', 'Imposto', 'Beneficios']
sizes = [15, 30, 45, 10]

colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0.1, 0, 0, 0)

plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
plt.title('Gráfico de Pizza')
plt.axis('equal')
plt.show()