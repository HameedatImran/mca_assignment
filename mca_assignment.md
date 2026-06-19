Question 1
What is an Epoch?
An epoch is one complete pass through the entire training dataset during model training. During one epoch, the algorithm processes all training examples once and updates the model parameters based on the calculated gradients.

Question 2
Learning Rate Too High (>1.0)

A too high learning rate causes the model to take overly large steps while updating weights. This leads to overshooting the optimal minimum, erratic fluctuations, and training instability. Instead of decreasing smoothly, loss function will oscillate wildly or completely diverge.

Learning Rate Too Small (<0.00001)

When the learning rate is extremely small, gradient descent takes tiny steps toward the minimum. The loss decreases very slowly, requiring many epochs to make meaningful progress. Training becomes inefficient and may appear almost flat on a loss curve.


What does "convex" mean?
A convex function is a mathematical function whose graph curves upward, forming a "cup" shape. A line segment connecting any two points on the graph never falls below the function's curve.

What does the error surface look like?
For linear regression with Mean Squared Error, the error surface is bowl-shaped.

Why does convexity guarantee that Gradient Descent can find the absolute best weights instead of getting trapped in a local minimum?

Because the error surface contains only one global minimum because of the bowl shape error surface and no local minima, gradient descent is guaranteed to converge to the best possible solution if an appropriate learning rate is used without going below the bowl.

