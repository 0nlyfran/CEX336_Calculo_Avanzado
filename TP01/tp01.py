# %% [markdown]
# <a href="https://colab.research.google.com/github/0nlyfran/CEX336_Calculo_Avanzado/blob/main/Calculo_Avanzado_TP01.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %% [markdown]
# #Camino
# ## Preparación
# ### Librerias
# - Preparo el entorno importando las librerias de utilidades
# ### Variables
# - Asigno valores relacionados a mi DNI a las variables

# %%
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Establezco valores a las variables
# DNI 30.517.845
a = 3
b = 5
c = 1
d = 7

# %% [markdown]
# Defino la función z = g(x)

# %%
def g_de_x(x, a, c, d):
    return ((10*((1+(1/(10000*d))) ** (-a * (x ** 2)))))

# %% [markdown]
# ## Grafico
# Preparo el entorno para la gráfica y grafico
# - Terreno: x e y
# - Calculó: z = g(x)
# 
# Nota para realizar la gráfica e calculado un y=0,2 o sea si "y" se mide en Km el resultado es un sendero de 200 metros de ancho.

# %%
terreno_x = np.linspace(-500, 500, 1000)
terreno_y = np.linspace(-0.1, 0.1, 100)
terreno_x, terreno_y = np.meshgrid(terreno_x, terreno_y)

z_camino = g_de_x(terreno_x, a, c, d)

#Gráfico la función en 3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(terreno_x, terreno_y, z_camino, cmap='viridis')

ax.set_title('Camino: 3D Plot z = g(x) = $10c(1+\\frac{1}{10000d})^{-ax^2}$')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_ylim(-5, 5)

plt.show()

# %% [markdown]
# #Montaña
# Preparo función superficie montaña

# %%
def terreno_montana(x, y, a, b, c, d):
    return 10 * c * ((1+(1/(10000*d))) ** ((-a * (x ** 2))-(b* (y**2))))

terreno_x_montana = np.linspace(-500, 500, 1000)
terreno_y_montana = np.linspace(-500, 500, 1000)
terreno_x_montana, terreno_y_montana = np.meshgrid(terreno_x_montana, terreno_y_montana)

z = terreno_montana(terreno_x_montana, terreno_y_montana, a, b, c, d)

#Gráfico la función en 3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(terreno_x_montana, terreno_y_montana, z, color='brown')

# Hago que el camino se pueda apreciar
terreno_x = np.linspace(-500, 500, 1000)
terreno_y = np.linspace(-10, 10, 100)
terreno_x, terreno_y = np.meshgrid(terreno_x, terreno_y)
ax.plot_surface(terreno_x, terreno_y, z_camino, color='g')

ax.set_title('Montaña con camino')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

ax.set_ylim(-400, 400)
ax.set_xlim(-400, 400)

plt.show()


