import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification
from sklearn.metrics import accuracy_score, confusion_matrix
import seaborn as sns

# Set random seed for reproducibility
np.random.seed(42)

def generate_synthetic_data(n_samples=150, n_classes=3, n_features=4, class_sep=1.0):
    """Generate synthetic classification data similar to Iris dataset structure"""
    X, y = make_classification(
        n_samples=n_samples,
        n_features=n_features,
        n_classes=n_classes,
        n_clusters_per_class=1,
        class_sep=class_sep,
        random_state=42
    )
    return X, y

def simulate_blockchain_data_additions(initial_samples=30, max_samples=150, step=10):
    """Simulate adding data incrementally through blockchain transactions"""
    # Generate full dataset
    X_full, y_full = generate_synthetic_data(n_samples=max_samples)
    
    # Initial split - starting point
    X_train = X_full[:initial_samples]
    y_train = y_full[:initial_samples]
    
    # Test set (separate from the data that will be added)
    X_test = X_full[max_samples-30:max_samples]
    y_test = y_full[max_samples-30:max_samples]
    
    # Data that will be added incrementally
    X_to_add = X_full[initial_samples:max_samples-30]
    y_to_add = y_full[initial_samples:max_samples-30]
    
    # Track accuracy as we add data
    accuracies = []
    sample_counts = []
    
    # Initialize model
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    # Initial model
    model = KNeighborsClassifier(n_neighbors=5)
    model.fit(X_train_scaled, y_train)
    
    # Initial accuracy
    y_pred = model.predict(X_test_scaled)
    accuracies.append(accuracy_score(y_test, y_pred))
    sample_counts.append(len(X_train))
    
    # Simulate adding data incrementally
    for i in range(0, len(X_to_add), step):
        end_idx = min(i + step, len(X_to_add))
        
        # Add new data points
        X_train = np.vstack([X_train, X_to_add[i:end_idx]])
        y_train = np.append(y_train, y_to_add[i:end_idx])
        
        # Retrain model
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        model = KNeighborsClassifier(n_neighbors=5)
        model.fit(X_train_scaled, y_train)
        
        # Evaluate
        y_pred = model.predict(X_test_scaled)
        accuracies.append(accuracy_score(y_test, y_pred))
        sample_counts.append(len(X_train))
    
    return sample_counts, accuracies, X_train, y_train, X_test, y_test

def simulate_data_drift(X_train, y_train, X_test, y_test, drift_intensity=0.5):
    """Simulate data drift by gradually changing the distribution of incoming data"""
    accuracies = []
    drift_levels = np.arange(0, 1.1, 0.1)
    
    # Base model trained on original data
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)
    
    base_model = KNeighborsClassifier(n_neighbors=5)
    base_model.fit(X_train_scaled, y_train)
    
    # Baseline accuracy
    baseline_acc = accuracy_score(y_test, base_model.predict(X_test_scaled))
    accuracies.append(baseline_acc)
    
    # Generate increasingly drifted data and see how model performs
    for drift in drift_levels[1:]:
        # Generate drifted test data (increasing separation between classes)
        X_drifted_test, y_drifted_test = generate_synthetic_data(
            n_samples=len(X_test),
            class_sep=1.0 + drift * drift_intensity * 3
        )
        
        # Transform using the original scaler
        X_drifted_scaled = scaler.transform(X_drifted_test)
        
        # Evaluate original model on drifted data
        y_pred = base_model.predict(X_drifted_scaled)
        acc = accuracy_score(y_drifted_test, y_pred)
        accuracies.append(acc)
    
    return drift_levels, accuracies

def main():
    # Part 1: Model growth with added data (replicating Fig. 5)
    sample_counts, accuracies, X_train_final, y_train_final, X_test, y_test = simulate_blockchain_data_additions(
        initial_samples=30,
        max_samples=150,
        step=10
    )
    
    plt.figure(figsize=(10, 6))
    plt.plot(sample_counts, accuracies, marker='o', linestyle='-', color='blue')
    plt.xlabel('Number of Training Samples')
    plt.ylabel('Model Accuracy')
    plt.title('Model Accuracy Improvement with Added Blockchain Data Points')
    plt.grid(True, linestyle='--', alpha=0.7)
    
    # Highlight key points
    for i, count in enumerate(sample_counts):
        if count in [30, 60, 90, 120]:
            plt.annotate(f"{accuracies[i]:.2f}", 
                         (count, accuracies[i]), 
                         textcoords="offset points",
                         xytext=(0, 10), 
                         ha='center')
    
    plt.tight_layout()
    plt.savefig('model_growth_chart.png')
    
    # Part 2: Simulate data drift and its impact on model performance
    drift_levels, drift_accuracies = simulate_data_drift(
        X_train_final, y_train_final, X_test, y_test
    )
    
    plt.figure(figsize=(10, 6))
    plt.plot(drift_levels, drift_accuracies, marker='o', linestyle='-', color='red')
    plt.xlabel('Data Drift Level')
    plt.ylabel('Model Accuracy')
    plt.title('Impact of Data Drift on Model Performance')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.savefig('data_drift_impact.png')
    
    # Part 3: Generate confusion matrices to show how predictions change
    # Create a figure with 3 subplots for confusion matrices
    fig, axes = plt.subplots(1, 3, figsize=(16, 5))
    
    # Train models with different amounts of data
    data_points = [30, 60, 120]
    
    for i, n_samples in enumerate(data_points):
        # Generate data
        X_full, y_full = generate_synthetic_data(n_samples=150)
        
        # Split data
        X_train = X_full[:n_samples]
        y_train = y_full[:n_samples]
        X_test = X_full[120:150]
        y_test = y_full[120:150]
        
        # Train model
        scaler = StandardScaler()
        X_train_scaled = scaler.fit_transform(X_train)
        X_test_scaled = scaler.transform(X_test)
        
        model = KNeighborsClassifier(n_neighbors=5)
        model.fit(X_train_scaled, y_train)
        
        # Get predictions
        y_pred = model.predict(X_test_scaled)
        
        # Plot confusion matrix
        cm = confusion_matrix(y_test, y_pred)
        ax = axes[i]
        sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', ax=ax)
        ax.set_title(f'Confusion Matrix with {n_samples} Samples')
        ax.set_xlabel('Predicted Label')
        ax.set_ylabel('True Label')
    
    plt.tight_layout()
    plt.savefig('confusion_matrix_evolution.png')
    
    print("Analysis complete! Charts have been saved.")

if __name__ == "__main__":
    main()