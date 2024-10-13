from dataclasses import dataclass
from pathlib import Path

import numpy as np
import numpy.typing as npt


@dataclass
class Airfoil:
    name: str
    upper_points: npt.NDArray[np.floating]
    lower_points: npt.NDArray[np.floating]
    points: npt.NDArray[np.floating]


def read_selig_airfoil_file(filepath: Path | str) -> Airfoil:
    """Reads a selig style airfoil coordinates file and returns an Airfoil object with the data.

    Args:
        filepath (Path | str): the filepath to the file, as a string or a pathlib.Path object

    Returns:
        Airfoil: Airfoil object with the airfoil data.
    """
    if isinstance(filepath, str):
        filepath = Path(filepath)

    file_lines = filepath.read_text().splitlines()

    name = file_lines[0].strip()
    upper_points = []
    lower_points = []
    points = []

    side = "upper"

    for line in file_lines[1:]:
        coord_data = line.strip().split()
        point_coord = [float(coord_data[0]), float(coord_data[1])]

        points.append(point_coord)

        if (point_coord[0] == 0.0) and (point_coord[1] == 0.0):
            upper_points.append(point_coord)
            lower_points.append(point_coord)
            side = "lower"

        elif side == "upper":
            upper_points.append(point_coord)

        elif side == "lower":
            lower_points.append(point_coord)

    points = np.array(points)
    upper_points = np.array(upper_points)
    lower_points = np.array(lower_points)

    # Reverse the order of the upper points to go from leading edge to trailing edge
    upper_points = np.flip(upper_points, axis=0)

    return Airfoil(
        name=name,
        upper_points=upper_points,
        lower_points=lower_points,
        points=points,
    )


def read_lednicer_airfoil_file(filepath: Path) -> Airfoil:
    """Reads a lednicer style airfoil coordinates file and returns an Airfoil object with the data.

    Args:
        filepath (Path | str): the filepath to the file, as a string or a pathlib.Path object

    Returns:
        Airfoil: Airfoil object with the airfoil data.
    """

    if isinstance(filepath, str):
        filepath = Path(filepath)

    file_lines = filepath.read_text().splitlines()

    name = file_lines[0].strip()
    n_points_data = file_lines[1].strip().split()
    n_upper_points = int(n_points_data[0].replace(".", ""))
    n_lower_points = int(n_points_data[1].replace(".", ""))

    upper_points = []

    for i in range(3, 3 + n_upper_points):
        line = file_lines[i]
        coord_data = line.strip().split()
        point_coord = [float(coord_data[0]), float(coord_data[1])]
        upper_points.append(point_coord)

    upper_points = np.array(upper_points)

    lower_points = []

    for i in range(4 + n_upper_points, 4 + n_upper_points + n_lower_points):
        line = file_lines[i]
        coord_data = line.strip().split()
        point_coord = [float(coord_data[0]), float(coord_data[1])]
        lower_points.append(point_coord)

    lower_points = np.array(lower_points)

    # Reverse upper points and remove repeated leading edge from the lower points
    points = np.row_stack([np.flip(upper_points, axis=0), lower_points[1:]])

    return Airfoil(
        name=name,
        upper_points=upper_points,
        lower_points=lower_points,
        points=points,
    )
