from pathlib import Path

import matplotlib.pyplot as plt

from auster_aero.geometry import read_lednicer_airfoil_file
from auster_aero.visualization import plot_airfoil


def test_plot_airfoil():
    filepath = Path("test/test_data/NACA747A315_lednicer.dat")
    lednicer_airfoil = read_lednicer_airfoil_file(filepath=filepath)
    fig, ax = plot_airfoil(lednicer_airfoil, height_mm=100, width_mm=150, dpi=300)
    plt.show()


if __name__ == "__main__":
    test_plot_airfoil()
