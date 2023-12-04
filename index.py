import numpy as np
import pandas as pd

# Set a random seed for reproducibility
np.random.seed(42)

# Define the number of samples
num_samples = 100

# Create a DataFrame to store the dummy dataset
columns = ['SubjectID', 'Label', 'Delta', 'Theta', 'Alpha', 'Beta', 'Gamma', 'ERP1', 'ERP2', 'Coherence', 'Amplitude', 'Asymmetry']
dummy_data = pd.DataFrame(columns=columns)

# Generate synthetic data
for i in range(num_samples):
    subject_id = f'Subject_{i + 1}'
    label = np.random.choice([0, 1])  # 0: Healthy, 1: Alzheimer's

    # EEG frequency bands
    delta = np.random.normal(4, 1)
    theta = np.random.normal(6, 1)
    alpha = np.random.normal(10, 1)
    beta = np.random.normal(15, 1)
    gamma = np.random.normal(30, 1)

    # Event-Related Potentials (ERPs)
    erp1 = np.random.normal(5, 1)
    erp2 = np.random.normal(8, 1)

    # Coherence
    coherence = np.random.normal(0.5, 0.1)

    # Amplitude
    amplitude = np.random.normal(20, 5)

    # Asymmetry
    asymmetry = np.random.normal(0, 1)

    # Create a temporary DataFrame for the current sample
    temp_df = pd.DataFrame({
        'SubjectID': subject_id,
        'Label': label,
        'Delta': delta,
        'Theta': theta,
        'Alpha': alpha,
        'Beta': beta,
        'Gamma': gamma,
        'ERP1': erp1,
        'ERP2': erp2,
        'Coherence': coherence,
        'Amplitude': amplitude,
        'Asymmetry': asymmetry
    }, index=[0])

    # Concatenate the temporary DataFrame to the main DataFrame
    dummy_data = pd.concat([dummy_data, temp_df], ignore_index=True)

# Save the dummy dataset to a CSV file
dummy_data.to_csv('dummy_eeg_dataset.csv', index=False)

# Display the first few rows of the generated dataset
print(dummy_data.head())
