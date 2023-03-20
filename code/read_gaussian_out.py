from ase import io
from ase.visualize import view

neutral_MM_path = '/Users/tdprice/Desktop/methoxymethanol_gaussian/MM.xyz'
atoms = io.read(neutral_MM_path)
#view(atoms)
print(atoms.get_chemical_symbols())
c6_o9 = 1.3987
c6_o8 = 1.4091
c6_h0 = 1.0895
c6_h1 = 1.0926
o9_c7 = 1.4226
o8_h5 = 0.9639
c7_h2 = 1.0856
c7_h3 = 1.0897
c8_h4 = 1.0937
C1 = 6
O2 = 9
O3 = 8
H5 = 0
H6 = 1
C4 = 7
H10 = 5
O8 = 3
H7 = 2
H9 = 3
H8 = 4

'''atoms.set_angle(O2, C1, O3, 113.2563)
atoms.set_angle(O2, C1, H5, 105.495)
atoms.set_angle(O2, C1, H6, 110.8969)
atoms.set_angle(O3, C1, H5, 111.5654)
atoms.set_angle(O3, C1, H6, 105.0661)
atoms.set_angle(H5, C1, H6, 110.6742)
atoms.set_angle(C1, O2, C4, 112.1398)
atoms.set_angle(C1, O3, H10, 107.3191)
atoms.set_angle(O2, C4, H7, 106.799)
atoms.set_angle(O2, C4, H8, 110.4084)
atoms.set_angle(O2, C4, H9, 111.2858)
atoms.set_angle(H7, C4, H8, 109.4349)
atoms.set_angle(H7, C4, H9, 109.7638)
atoms.set_angle(H8, C4, H9 , 109.1133)
atoms.set_dihedral(O3, C1, O2, C4, 67.4385)
atoms.set_dihedral(H5, C1, O2, C4, -170.265)
atoms.set_dihedral(H6, C1, O2, C4, -50.3964)
atoms.set_dihedral(O2, C1, O3, H10, 64.7163)
atoms.set_dihedral(H5, C1, O3, H10, -54.134 )
atoms.set_dihedral(H6, C1, O3, H10, -174.103)
atoms.set_dihedral(C1, O2, C4, H7, 177.9081)
atoms.set_dihedral(C1, O2, C4, H8, 59.0153)
atoms.set_dihedral(C1, O2, C4, H9, -62.3102)
atoms.set_angle(O2, C4, H7, 106.799)
atoms.set_angle(O2, C4, H8, 110.4084)
atoms.set_angle(O2, C4, H9, 111.2858)
atoms.set_distance(C1, O2, 1.3987, fix=0)
atoms.set_distance(C1, O3, 1.4091, fix=0)
atoms.set_distance(C1, H5, 1.0895, fix=0)
atoms.set_distance(C1, H6, 1.0926, fix=0)
atoms.set_distance(O2, C4, 1.4226, fix=0)
atoms.set_distance(O3, H10, 0.9639, fix=0)
atoms.set_distance(C4, H7, 1.0856, fix=0)
atoms.set_distance(C4, H8, 1.0937, fix=0)
atoms.set_distance(C4, H9, 1.0897, fix=0)
view(atoms)'''

#First excited  conformer
atoms.set_angle(O2, C1, O3, 113.8441)
atoms.set_angle(O2, C1, H5, 105.8695)
atoms.set_angle(O2, C1, H6, 109.6035 )
atoms.set_angle(O3, C1, H5, 106.563 )
atoms.set_angle(O3, C1, H6, 110.117 )
atoms.set_angle(H5, C1, H6, 110.7248 )
atoms.set_angle(C1, O2, C4, 112.4451)
atoms.set_angle(C1, O3, H10, 108.9099)
atoms.set_angle(O2, C4, H7, 107.1106)
atoms.set_angle(O2, C4, H8, 110.809)
atoms.set_angle(O2, C4, H9, 111.4946)
atoms.set_angle(H7, C4, H8, 109.1535)
atoms.set_angle(H7, C4, H9, 108.8603)
atoms.set_angle(H8, C1, H9 , 109.3456)
atoms.set_dihedral(O3, C1, O2, C4, 68.6637)
atoms.set_dihedral(H5, C1, O2, C4, -174.614)
atoms.set_dihedral(H6, C1, O2, C4, -55.1559)
atoms.set_dihedral(O2, C1, O3, H10, -86.3434)
atoms.set_dihedral(H5, C1, O3, H10, 157.3386 )
atoms.set_dihedral(H6, C1, O3, H10, 37.198)
atoms.set_dihedral(C1, O2, C4, H7, 171.8162)
atoms.set_dihedral(C1, O2, C4, H8, 52.8533)
atoms.set_dihedral(C1, O2, C4, H9, -69.1881)
atoms.set_angle(O2, C4, H7, 107.1106)
atoms.set_angle(O2, C4, H8, 110.809)
atoms.set_angle(O2, C4, H9, 111.4946)
atoms.set_distance(C1, O2, 1.3987, fix=0)
atoms.set_distance(C1, O3, 1.4091, fix=0)
atoms.set_distance(C1, H5, 1.0895, fix=0)
atoms.set_distance(C1, H6, 1.0926, fix=0)
atoms.set_distance(O2, C4, 1.4226, fix=0)
atoms.set_distance(O3, H10, 0.9639, fix=0)
atoms.set_distance(C4, H7, 1.0856, fix=0)
atoms.set_distance(C4, H8, 1.0937, fix=0)
atoms.set_distance(C4, H9, 1.0897, fix=0)

view(atoms)