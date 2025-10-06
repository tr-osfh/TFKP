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
    plt.imshow(mandelbrot, extent=[xmin, xmax, ymin, ymax], cmap='hot', origin='lower')
    plt.colorbar(label='Итерации')
    plt.title('Множество Мандельброта')
    plt.xlabel('Re(c)')
    plt.ylabel('Im(c)')
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    # 1. Полный вид (классический)
    xmin, xmax = -2.0, 1.0
    ymin, ymax = -1.5, 1.5

    ## 2. Увеличение на "шею" - много спиралей
    #xmin, xmax = -0.75, -0.65
    #ymin, ymax = 0.1, 0.2
#
    ## 3. Еще большее увеличение на спирали
    #xmin, xmax = -0.745, -0.735
    #ymin, ymax = 0.11, 0.12
#
    ## 4. Область с мини-копиями Мандельброта
    #xmin, xmax = -1.25, -1.15
    #ymin, ymax = 0.25, 0.35
#
    ## 5. Интересные спиральные структуры
    #xmin, xmax = 0.28, 0.38
    #ymin, ymax = 0.48, 0.58
#
    ## 6. Еще одна область с фрактальной структурой
    #xmin, xmax = -0.1, 0.1
    #ymin, ymax = 0.7, 0.9
    max_iter = 100

    plot_mandelbrot(xmin, xmax, ymin, ymax, max_iter=max_iter)