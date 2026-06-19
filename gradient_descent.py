import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

X = 2 * np.random.rand(100, 1)

noise = np.random.randn(100, 1)
y = 4 * X + 3 + noise


def fit_line(X, y, lr, epochs):
    w = 0.0
    b = 0.0

    m = len(X)

    losses = []

    for epoch in range(epochs):

        y_pred = w * X + b

        loss = np.mean((y - y_pred) ** 2)
        losses.append(loss)

        dw = (-2/m) * np.sum(X * (y - y_pred))
        db = (-2/m) * np.sum(y - y_pred)

        w = w - lr * dw
        b = b - lr * db

    return w, b, losses


epochs = 200

_, _, losses_1 = fit_line(X, y, 0.001, epochs)
_, _, losses_2 = fit_line(X, y, 0.1, epochs)
_, _, losses_3 = fit_line(X, y, 0.9, epochs)

plt.figure(figsize=(10, 6))

plt.plot(losses_1, label="lr = 0.001")
plt.plot(losses_2, label="lr = 0.1")
plt.plot(losses_3, label="lr = 0.9")

plt.title("Gradient Descent Convergence")
plt.xlabel("Epoch")
plt.ylabel("MSE Loss")
plt.legend()
plt.grid(True)

plt.savefig("loss_convergence.png")

plt.show()