import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

def simulate_random_noise_response(V, F, k, noise_mean, noise_std):
    tau = V / (F + V * k)
    num = [1]
    den = [tau, 1]
    system = signal.TransferFunction(num, den)
    t = np.linspace(0, 100, 1000)
    np.random.seed(0)
    u = np.random.normal(noise_mean, noise_std, len(t))
    t, response, _ = signal.lsim(system, U=u, T=t)
    plt.plot(t, response, label='System Response')
    plt.plot(t, u, label='Random Noise Input', linestyle='--')
    plt.title('CSTR Random Noise Response (Concentration)')
    plt.xlabel('Time [s]')
    plt.ylabel('Concentration')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    simulate_random_noise_response(1.0, 0.5, 0.1, 0, 1)
