from fenics import *

t_end = 10.0
dt = 0.1
k = 300
u_in = 20
u_out = -20

xml_file = "helix.xml"
mesh = Mesh(xml_file)
fd = MeshFunction('size_t', mesh, "helix_facet_region.xml");

V = FunctionSpace(mesh, 'P', 1)

bc1 = DirichletBC(V, Constant(u_in), fd, 3)
bc2 = DirichletBC(V, Constant(u_out), fd, 2)
bc = [bc1, bc2]

u = TrialFunction(V)
v = TestFunction(V)
u_n = Function(V)

F = u*v*dx + dt*k*dot(grad(u), grad(v))*dx - u_n*v*dx
a, L = lhs(F), rhs(F)

u = Function(V)
t = 0
vtkfile = File('output/output.pvd')

num_steps = int(t_end/dt)
for n in range(num_steps):
    t += dt
    solve(a == L, u, bc)
    u_n.assign(u)
    vtkfile << (u, t)
