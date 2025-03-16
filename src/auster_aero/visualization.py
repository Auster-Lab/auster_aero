import matplotlib.pyplot as plt
import numpy as np

from auster_aero import quantity
from auster_aero.geometry import Airfoil


def plot_airfoil(airfoil: Airfoil, height_mm: float, width_mm: float, dpi: int = 300):
    """
    Plots the airfoil shape with specified dimensions and resolution.

    Args:
        airfoil (Airfoil): The airfoil object containing the points to plot.
        height_mm (float): The height of the plot in millimeters.
        width_mm (float): The width of the plot in millimeters.
        dpi (int, optional): The resolution of the plot in dots per inch. Default is 300.

    Returns:
        tuple: A tuple containing the figure and axes objects of the plot.
    """
    height_in = quantity(height_mm, "millimeter").to("inch")
    width_in = quantity(width_mm, "millimeter").to("inch")

    max_height = airfoil.points[:, 1].max()
    min_height = airfoil.points[:, 1].min()
    max_thickness = max_height - min_height

    leading_edge_x = airfoil.points[:, 0].min()
    trailing_edge_x = airfoil.points[:, 0].max()
    chord = trailing_edge_x - leading_edge_x

    fig, ax = plt.subplots(figsize=(width_in.magnitude, height_in.magnitude), dpi=dpi)
    ax.plot(airfoil.points[:, 0], airfoil.points[:, 1], color="firebrick", linewidth=1.0)
    ax.set_xticks(np.linspace(leading_edge_x - chord / 10, trailing_edge_x + chord / 10, 13))
    ax.set_xticks(
        np.linspace(leading_edge_x - chord / 10, trailing_edge_x + chord / 10, 61), minor=True
    )
    ax.set_yticks(np.linspace(-0.3 * chord, 0.3 * chord, 7))
    ax.set_yticks(np.linspace(-0.3 * chord, 0.3 * chord, 31), minor=True)
    ax.set(
        title=airfoil.name,
        xlabel="chord",
        ylabel="thickness",
        aspect="equal",
        xlim=[leading_edge_x - chord / 10, trailing_edge_x + chord / 10],
        ylim=[-0.3 * chord, 0.3 * chord],
    )
    ax.grid(True, which="both", linewidth=0.2)
    ax.grid(which="minor", linestyle="--", linewidth=0.2, alpha=0.75)

    return fig, ax
