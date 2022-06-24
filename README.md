# OptML_Project: Study on Loss Landscape Geometry for Improving Generalization in Adaptive Optimization Methods
In this project we analyse the loss landscape geometry of adaptive optimization methods, using a measure of loss landscape curvature called sharpness. It is well known that flat minima are associated with better generalization. Improved methods that aid convergence of adaptive methods, namely ADAM, to flat minima are proposed, for improving their generalization.



## Definitions:

### 1. Generalization:
Generalization refers to a model's ability to adapt properly to new, previously unseen data, drawn from the same distribution as the one used to create the model.

### 2. Optimization:
Optimization is the process where we train the model iteratively that results in a maximum and minimum function evaluation.

### 3. Sharpness/ Flatness: 
The sharpness of loss function can be defined as the difference between the maximum training loss and the generalization loss at the same point at the x-axis.

![image](https://user-images.githubusercontent.com/21705597/175521022-a43d5c96-c474-4105-91ed-370f7a60cd0d.png)


### 4. Sharpness Aware Minimisation (SAM): 
Sharpness-Aware Minimization, or SAM, is a procedure that improves model generalization by simultaneously minimizing loss value and loss sharpness. 



## Overview of the proposed method:

![image](https://user-images.githubusercontent.com/21705597/175528840-818c3523-e675-433a-8478-38389e449b73.png)

In this project we are trying to compare the sharpness of the minima for a model training with optimization that does not include SAM and one that includes SAM.

### Neural Networks:
1. ResNet 18
2. VGG 16

### Optimizer:
1. SGD
2. ADAM

### Dataset:
Cifar-10 (https://www.cs.toronto.edu/~kriz/cifar.html)

### Requirements:
1. Pytorch: https://pytorch.org/get-started/locally/
2. Torchvision
3. matplotlib
4. Cuda (if available)

## Code Structure:
1. **Baseline Code:** Training and optimization without SAM- shared at the link:
2. **SAM Code:** Training and optimization with SAM- shared at the link:

