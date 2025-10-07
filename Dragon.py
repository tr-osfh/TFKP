import numpy as np
import matplotlib.pyplot as plt


def harter_heighway_dragon(iterations):
    points = np.array([0 + 0j, 1 + 0j], dtype=complex)

    for _ in range(iterations):
        current = points[:-1]
        last = points[-1]

        segments = np.diff(points)

        rotated = segments * 1j

        new_points = last + np.cumsum(rotated[::-1])

        points = np.concatenate([points, new_points])

    return points


def plot_dragon(iterations=12, figsize=(10, 10)):
    points = harter_heighway_dragon(iterations)

    plt.figure(figsize=figsize)
    plt.plot(points.real, points.imag, color='darkblue', linewidth=0.7)
    plt.axis('equal')
    plt.axis('off') 
    plt.title(f'Дракон Хартера–Хейтуэя ({iterations} итераций)', fontsize=14)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_dragon(iterations=3)