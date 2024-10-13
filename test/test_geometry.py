from pathlib import Path

from auster_aero.geometry import read_lednicer_airfoil_file, read_selig_airfoil_file


def test_read_selig_airfoil_file():
    filepath = Path("test/test_data/NACA0012_selig.dat")
    selig_airfoil = read_selig_airfoil_file(filepath=filepath)
    print(selig_airfoil)


def test_read_lednicer_airfoil_file():
    filepath = Path("test/test_data/NACA0012_lednicer.dat")
    lednicer_airfoil = read_lednicer_airfoil_file(filepath=filepath)
    print(lednicer_airfoil)


if __name__ == "__main__":
    # test_read_selig_airfoil_file()
    test_read_lednicer_airfoil_file()
