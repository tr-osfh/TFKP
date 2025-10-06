import numpy as np
import matplotlib.pyplot as plt


def julia_set(c, xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    Z = X + Y * 1j

    julia = np.zeros(Z.shape, dtype=int)

    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] * Z[mask] + c
        julia[mask] = i

    julia[np.abs(Z) <= 2] = max_iter
    return julia


def plot_julia(c, xmin, xmax, ymin, ymax, width=800, height=800, max_iter=100):
    julia = julia_set(c, xmin, xmax, ymin, ymax, width, height, max_iter)

    plt.figure(figsize=(10, 8))
    plt.imshow(julia, extent=[xmin, xmax, ymin, ymax], cmap='hot', origin='lower')
    plt.colorbar(label='Итерации')
    plt.title(f'Множество Жюлиа для c = {c}')
    plt.xlabel('Re(z₀)')
    plt.ylabel('Im(z₀)')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # Измените параметры ниже для разных форм множества Жюлиа
    c = -0.7 + 0.27015j
    xmin, xmax = -1.5, 1.5
    ymin, ymax = -1.5, 1.5
    max_iter = 100

    ## 1. Кролик Дуади
    #c = -0.7 + 0.27015j
#
    ## 2. Дендрит (ветвистое)
    #c = -0.4 + 0.6j
#
    ## 3. Сан-Марко
    #c = -0.8 + 0.156j
#
    ## 4. Красивый пример из задания
    #c = -0.5251993 + 0.5251993j
#
    ## 5. Простая связная форма
    #c = -0.75 + 0j
#
    ## 6. Три лепестка
    #c = 0 + 1j
#
    ## 7. Снежинка
    #c = -0.5 + 0.5j
#
    ## 8. Пыль Кантора (несвязное)
    #c = -1 + 0j

    plot_julia(c, xmin, xmax, ymin, ymax, max_iter=max_iter)