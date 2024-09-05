### Description
This repo contains the reproducible results part of the individual project. To reproduce the results, you need two Python files: the driver file 'KvN.py' and the module containing the tools 'KvN_tools.py'. Additionally, NumPy, SciPy, TQDM, and Matplotlib are required.

### Parameters
The user is encouraged to play around with the parameters to experiment with different nonlinear systems. The available parameters are as follows:

|Parameter | Description |
|----------|-------------|
|n_qubits | Number of qubits that the grid discretisation will represent |
|grid_extent | Extent of the grid |
|n_steps | Number of time steps simulated for |
|delta | Size of time step |
|psi0 | Initial condition; can take the form of a delta or Gaussian |
|params | The parameters of the quadratic nonlinearity |
|H | The Hamiltonian, with a choice of an FFT or finite difference-based derivative |
