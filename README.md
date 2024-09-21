# Automated Plant Species Identification System

## Scenario:
A botanical research center is working on a system to automatically classify different species of flowers based on their physical characteristics. The center collects data on various flower species and needs a robust model to classify new samples based on measurements like petal length, petal width, sepal length, and sepal width.

## Problem:
Botanists need to quickly and accurately identify species of the **Iris** plant (setosa, versicolor, and virginica) to streamline their research and recordkeeping processes. Identifying species manually is time-consuming, and there is potential for human error.

## Solution: RandomForestClassifier
The research center can use the **RandomForestClassifier**, a powerful ensemble learning algorithm that builds multiple decision trees and merges them to get more accurate and stable predictions. This classifier can be trained on the **Iris dataset**, which contains flower measurements and corresponding species, allowing it to predict the species of new flowers based on their features.

## Steps:
### 1. Data Collection
Use the Iris dataset, which consists of 150 samples of Iris flowers, each labeled as one of three species (setosa, versicolor, or virginica). Each sample includes four features:
- Sepal length
- Sepal width
- Petal length
- Petal width

### 2. Model Training
Train the **RandomForestClassifier** on this dataset, where the features (sepal and petal dimensions) are the independent variables and the species of the flower is the dependent variable.

### 3. Prediction
For new flower samples, input the sepal and petal dimensions into the model, which will predict the species based on the learned patterns from the training data.

### 4. Performance Evaluation
Use metrics such as **accuracy**, **precision**, **recall**, and **F1-score** to evaluate the model’s performance. Since the dataset is well-balanced with three classes, **RandomForestClassifier** is well-suited for providing high accuracy and stability by reducing overfitting that can occur with a single decision tree.

---

## Algorithm Details: RandomForestClassifier

### How RandomForestClassifier Works
Random Forest is an **ensemble learning method** for classification. It works by creating a forest of decision trees at training time and outputting the mode of the classes (for classification) of the individual trees.

The **RandomForestClassifier** in this project:
- Trains multiple decision trees on different random subsets of the data.
- Each tree makes a prediction for the class (Iris species), and the final prediction is made based on the majority vote of all trees.
- Reduces the risk of overfitting that can occur with a single decision tree, improving accuracy and generalization.

### Why Use RandomForestClassifier?
- **High accuracy**: By combining the predictions of multiple decision trees, RandomForest often provides more accurate results than a single model.
- **Robust to overfitting**: RandomForest reduces the risk of overfitting because it averages the predictions of many trees.
- **Feature importance**: RandomForest can rank the importance of each feature (sepal and petal measurements), giving insights into which characteristics are most significant in species classification.

---

## Git Commands

To clone, contribute, and push updates to the repository, use the following Git commands:

1. **Clone the repository:**
    ```bash
    git clone https://github.com/kru2710shna/Flower_Identifier.git
    ```

2. **Navigate into the project directory:**
    ```bash
    cd Flower_Identifier
    ```

3. **Create a new branch:**
    ```bash
    git checkout -b your-branch-name
    ```

4. **Make changes to the code or documentation.**

5. **Stage your changes:**
    ```bash
    git add .
    ```

6. **Commit your changes:**
    ```bash
    git commit -m "Add your commit message here"
    ```

7. **Push your changes to the repository:**
    ```bash
    git push origin your-branch-name
    ```

8. **Create a pull request:**
    After pushing your changes, visit the GitHub repository and open a pull request to merge your changes into the main branch.

---

## Repository Link
[Flower Species Identification using RandomForestClassifier](https://github.com/kru2710shna/Flower_Identifier)
