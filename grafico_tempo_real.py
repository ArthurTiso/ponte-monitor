import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

plt.style.use("dark_background")

x_data = []
y_data = []

fig, ax = plt.subplots()

peso_atual = 0

def gerar_dados():
    global peso_atual
    
    incremento = random.uniform(1, 10) #substituir por 10 fixo? Já que lá eles incrementam de 10 em 10
    peso_atual += incremento
    
    if peso_atual > 120:
        peso_atual = 0
        
    return peso_atual

def atualizar(frame):

    peso = gerar_dados()

    x_data.append(len(x_data))
    y_data.append(peso)

    if len(x_data) > 50:
        x_data.pop(0)
        y_data.pop(0)

    ax.clear()

    ax.plot(x_data, y_data, color="cyan", linewidth=3, marker = "o")

    ax.set_title("Monitoramento da Ponte", fontsize = 16)
    ax.set_xlabel("Tempo", fontsize = 12)
    ax.set_ylabel("Peso suportado (kg)", fontsize = 12)

    #ax.grid(True, linestyle="--", alpha=0.5)

    ax.text(
    0.10,
    0.90,
    f"Peso atual: {peso:.2f} kg",
    transform=ax.transAxes,
    fontsize=14,
    color="white"
)

ani = animation.FuncAnimation(fig, atualizar, interval= 800)

plt.show()