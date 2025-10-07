import numpy as np
import matplotlib.pyplot as plt

def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    X, Y = np.meshgrid(x, y)
    C = X + Y * 1j

    mandelbrot = np.zeros(C.shape, dtype=int)
    Z = np.zeros(C.shape, dtype=complex)

    for i in range(max_iter):
        mask = np.abs(Z) <= 2
        Z[mask] = Z[mask] * Z[mask] + C[mask]
        mandelbrot[mask] = i

    mandelbrot[np.abs(Z) <= 2] = max_iter
    return mandelbrot

def plot_mandelbrot(xmin, xmax, ymin, ymax, width=800, height=800, max_iter=100):
    mandelbrot = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

    plt.figure(figsize=(10, 8))
    plt.imshow(mandelbrot, extent=[xmin, xmax, ymin, ymax], cmap='magma', origin='lower')
    plt.colorbar(label='Итерации')
    plt.title('Множество Мандельброта')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    xmin, xmax = -0.748, -0.747
    ymin, ymax = 0.102, 0.103
    max_iter = 2000
    plot_mandelbrot(xmin, xmax, ymin, ymax, max_iter=max_iter)