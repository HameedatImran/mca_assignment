# The Gradient Descent Deep-Dive & Open Source Workflow

## Objective

You will independently research, code, and optimize the Gradient Descent algorithm from scratch using Python and NumPy. You will then package your code and submit it to a shared class repository by opening a professional GitHub Pull Request (PR) named strictly after your full name.

---

# Phase 1: Git & GitHub Setup (The Workflow)

Before writing any code, you must set up your local development space using standard industry Git workflows.

## 1. Fork the Repository

Navigate to the class GitHub repository URL provided below and click the **Fork** button in the top right corner to create a copy under your personal account.

## 2. Clone Your Fork

Open your terminal or Git Bash and clone your fork locally:

```bash
git clone https://github.com/qeinstein/mca_assignments.git
```

## 3. Create a Feature Branch

Never work directly on the main branch. Create a clean branch named after yourself:

```bash
git checkout -b gradient-descent-yourname
```

## 4. Work in a file named after yourself

Don't work in the root directory, work in the folder you created with your own name

---

# Phase 2: Core Research Questions

Before you code, answer the following questions inside a Markdown file named `RESEARCH.md` in your own folder.

## 1. What is an Epoch?

In plain English, what does one complete epoch mean during model training?

## 2. The Learning Rate Dilemma

Explain what happens visually to the error metric when the learning rate (alpha) is:

### Too High (> 1.0)

Describe how the loss behaves and why.

### Too Small (< 0.00001)

Describe how the loss behaves and why.

## 3. Local vs. Global Minima

Linear regression with Mean Squared Error (MSE) is a convex optimization problem.

Research and explain:

* What does "convex" mean?
* What does the error surface look like?
* Why does convexity guarantee that Gradient Descent can find the absolute best weights instead of getting trapped in a local minimum?

---

# Phase 3: The Coding Challenge

Create a file named `gradient_descent.py`.

Write a clean, well-documented Python script using NumPy and Matplotlib.

---

## Task 1: Generate Noisy Linear Data

Generate a synthetic dataset with 100 data points where:

[
y = 4x + 3 + \text{Gaussian Noise}
]

Use the following starter code:

```python
import numpy as np

np.random.seed(42)

X = 2 * np.random.rand(100, 1)

# Create a linear ground truth target with added random noise
noise = np.random.randn(100, 1)
y = 4 * X + 3 + noise
```

---

## Task 2: Build Gradient Descent From Scratch

Implement a function:

```python
fit_line(X, y, lr, epochs)
```

Requirements:

### Parameter Initialization

Initialize:

```python
w = 0.0
b = 0.0
```

### Loss Tracking

Track the Mean Squared Error (MSE) loss at every epoch.

Store all loss values in a list for plotting later.

### Manual Gradient Updates

Do **not** use Scikit-Learn.

Compute gradients manually and update:

```python
w = w - lr * dw
b = b - lr * db
```

where:

```python
dw = gradient of loss with respect to weight
db = gradient of loss with respect to bias
```

---

## Task 3: Experiment & Plot the Loss Journey

Run your algorithm three separate times using the same dataset but different learning rates.

### Run A

```python
alpha = 0.001
```

Expected behavior: very slow learning.

### Run B

```python
alpha = 0.1
```

Expected behavior: healthy convergence.

### Run C

```python
alpha = 0.9
```

Expected behavior: aggressive learning that may oscillate or diverge.

---

## Visualization Requirement

Using Matplotlib:

* Plot Epoch vs MSE Loss.
* Show all three learning-rate runs on the same graph.
* Use different colors and labels.
* Add:

  * Title
  * X-axis label
  * Y-axis label
  * Legend
  * Grid

Save the chart as:

```text
loss_convergence.png
```

---

# Submission Deadline & Grading Policy

## Deadline

This assignment is compulsory for all MCA students.

All submissions must be completed and the Pull Request opened on or before Friday, 19/06/2026, 11:59 PM WAT.

Late submissions will not be considered unless prior approval has been granted by the MCA leadership.

## Contribution to Final Scores

This assignment contributes 30% of the MCA final evaluation score.

Assessment will be based on:

- Quality and completeness of responses in RESEARCH.md
- Correct implementation of Gradient Descent from scratch
- Proper loss tracking and visualization
- Code quality, readability, and documentation
- Appropriate use of Git and GitHub workflows
- Successful generation of loss_convergence.png
- Professional Pull Request submission

## Mandatory Requirement

Completion of this assignment is mandatory for all MCA students.

Failure to submit a valid Pull Request by the stated deadline will result in a score of zero (0) for this assessment, representing 30% of the final MCA evaluation score.

A submission will only be considered valid if it satisfies all stated requirements and is submitted through a Pull Request with the student's full name as the Pull Request title.

---

# Phase 4: Submit Your Pull Request

## Critical Rule for PR Naming

When creating your Pull Request on GitHub:

**The PR title must be your Full Name.**

### Correct Example

```text
John Doe
```

### Incorrect Examples

```text
Assignment 5
```

```text
Gradient Descent Update
```

```text
Machine Learning Homework
```

Pull Requests that do not use the student's full name as the title will not be graded.

---

## Step 1: Stage and Commit (Remember to create a .gitignore)

Once your code runs successfully and the chart has been generated:

```bash
git add .
git commit -m "feat: complete gradient descent challenge and research"
```

---

## Step 2: Push to GitHub

Push your branch to your fork:

```bash
git push origin gradient-descent-yourname
```

---

## Step 3: Open the Pull Request

1. Navigate to the original class repository.
2. GitHub should display a yellow banner indicating that your branch has been pushed.
3. Click **Compare & Pull Request**.

---

## Step 4: Set PR Title and Description

### Title

Enter your exact full name.

Example:

```text
John Doe
```

### Description

Your PR description should include:

* A summary of your implementation.
* An explanation of the metrics you tracked.
* What the convergence plot revealed about different learning rates.
* Confirmation that the code executes successfully without syntax or runtime errors.

Submit the Pull Request for review.

---

# Deliverables Checklist

Before submission, verify that your repository contains:

* [ ] `gradient_descent.py`
* [ ] `RESEARCH.md`
* [ ] `loss_convergence.png`
* [ ] Feature branch pushed to GitHub
* [ ] Pull Request opened
* [ ] Pull Request title set to your full name
* [ ] Code runs successfully without crashes

Good luck and happy optimizing!
