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
    plt.imshow(julia, extent=[xmin, xmax, ymin, ymax], cmap='magma', origin='lower')
    plt.colorbar(label='Итерации')
    plt.title(f'Множество Жюлиа для c = {c}')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    c = -0.8j
    xmin, xmax = -1.5, 1.5
    ymin, ymax = -1.5, 1.5
    max_iter = 300
    plot_julia(c, xmin, xmax, ymin, ymax, max_iter=max_iter)