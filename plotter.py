import numpy as np
import matplotlib.pyplot as plt

with open('SAM_ADAM_RESNET.npy', 'rb') as f:
    train_losses = np.load(f)
    train_accuracy = np.load(f)
    val_losses = np.load(f)
    val_accuracy = np.load(f)


def plot(train_accuracy, val_accuracy):
    plt.plot(train_accuracy, 'r', label='Train')
    plt.plot(val_accuracy, 'b', label='Test')
    plt.xlabel("Epoch")
    plt.ylabel("Accuracy")
    plt.legend(loc='best')
    plt.show()

plot(train_accuracy, val_accuracy)