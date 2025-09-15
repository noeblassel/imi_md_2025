import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# --- paramètres physiques ---
M = 1.0
temperature = 2.0

# potentiel
def V(q):
    return np.zeros_like(q)

# force
def F(q):
    return np.zeros_like(q)

# energie cinetique
def W(p):
    return np.zeros_like(p)

def mon_schema(q, p, force, dt, gamma=None): # gamma = pour langevin
     return q, p

def film(q0, p0, force, n_steps, dt, gamma, schema): # animation
    q, p = q0, p0
    t = 0

    fig, ax = plt.subplots()

    xlim = 3.0
    X = np.linspace(-xlim, xlim, 400)

    courbe_potentiel, = ax.plot(X, V(X), color='black')
    atom, = ax.plot([q0], [V(q0)], 'o', ms=12, color='red')

    ax.set_xlim(-xlim, xlim)
    ax.set_ylim(0.0, 5.0)

    energy_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

    def init():
        atom.set_data([], [])
        energy_text.set_text('')
        return atom, energy_text

    def animate(frame):
        nonlocal q, p, force, t, dt
        q, p = schema(q, p, force, dt, gamma)
        t += dt

        atom.set_data([q], [V(q)])

        total_energy = V(q) + W(p)
        energy_text.set_text(f'H = {total_energy:.4f}, t = {t:.2f}')

        return atom, energy_text

    ani = animation.FuncAnimation(
        fig,
        animate,
        frames=n_steps,
        init_func=init,
        interval=20,
        blit=True,
        repeat=False
    )
    plt.show()
    return ani

# --- paramètres de simulation ---
dt = 0.05
n_steps = 500
gamma = 1.0

# --- conditions initiales ---
q0 = 0.0
sigma_p = np.sqrt(temperature * M)
p0 = np.random.randn() * sigma_p

# --- simulation ---
ani = film(q0, p0, F, n_steps, dt, gamma, mon_schema)