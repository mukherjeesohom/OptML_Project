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


