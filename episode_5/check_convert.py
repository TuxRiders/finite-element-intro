from fenics import *

xml_file = "helix.xml"
mesh = Mesh(xml_file)

U = FunctionSpace(mesh, 'P', 1)
u = Function(U)

vtkfile = File('test.pvd')
vtkfile << (u)

cd = MeshFunction('size_t', mesh, "helix_physical_region.xml");
fd = MeshFunction('size_t', mesh, "helix_facet_region.xml");
