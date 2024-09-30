import KvN_tools as kvn
import numpy as np

# Set up the grid
n_qubits = 10
n_grid = 2**n_qubits
grid_extent = (-2,2)
x = np.linspace(*grid_extent, n_grid)
x0 = 1
dx = x[1]-x[0]

# Set up time
n_steps = 30000
delta = 0.001
t = np.linspace(0, n_steps*delta, n_steps)

# Set up the initial state (delta or gaussian)
psi = kvn.psi0(x,x0, type='gaussian', plot=False, std=0.03)

# Generate the Hamiltonian to solve generic quadratic ODE, 
# i.e. x' = ax^2 + bx + c where a,b,c are in params list
params = (-1,0,0)

H = kvn.KvN_hamiltonian(x, params, deriv_type='FFT')
psi_store = kvn.time_evolution(H, psi, delta, n_steps)

#################################################################
# Plotting code

#kvn.plot_evolution(x, psi_store, t, save=False,  vmax=0.05)
#kvn.plot_mode(x, psi_store, t, plot_analytical=False, params=(-1,0,0), save=False)
#kvn.plot_evolution_mode(x, psi_store, t, save=True, plot_analytical=False, params=(-1,0,0), filename='KvN_delta_FFT')
x_kvn = kvn.plot_initial_evolution_mode(x, psi_store, t, save=True, plot_analytical=False, params=params, filename='KvN_plots', x0=x0)
#kvn.plot_std_evolution_mode(x, psi_store, t, save=True, plot_analytical=False, params=params, filename='KvN_plots', x0=x0)

#################################################################
# Stable time analysis

epsilon = 0.01

# Get the numerical solution 
t_num, x_num = kvn.numerical_solution(t, x0, params)

# Get the KvN stable time
t_stable = kvn.stable_time(t, x_kvn, x_num, epsilon)
print(f'Solution stable for: {t_stable.max()}')