



import os
import mne
import json
import numpy as np
import pandas as pd

# Folder containing your EEG files
folder_path = r"C:\Users\priya\OneDrive\Desktop\eeg"

# List to store results for all files
all_results = []

# Iterate over all files in the folder
for filename in os.listdir(folder_path):
    if filename.endswith(".set"):
        file_path = os.path.join(folder_path, filename)
        print("Processing file:", file_path)

        # Load .set file using MNE
        raw = mne.io.read_raw_eeglab(file_path, preload=True)

        # Extract relevant information
        # subject_id = "Subject_001"  # You can replace this with the actual subject ID
        # label = "Healthy"  # You can replace this with the actual label

        # ... (rest of your calculations)
        delta = np.mean(raw.copy().filter(1, 4).get_data(), axis=-1).mean()
        theta = np.mean(raw.copy().filter(4, 8).get_data(), axis=-1).mean()
        alpha = np.mean(raw.copy().filter(8, 13).get_data(), axis=-1).mean()
        beta = np.mean(raw.copy().filter(13, 30).get_data(), axis=-1).mean()
        gamma = np.mean(raw.copy().filter(30, 40).get_data(), axis=-1).mean()
        erp1 = np.mean(raw.copy().pick_channels(['Fz']).filter(0.1, 1).get_data(), axis=-1).mean()
        erp2 = np.mean(raw.copy().pick_channels(['Pz']).filter(0.1, 1).get_data(), axis=-1).mean()
        asymmetry = np.mean(raw.copy().pick_channels(['F3', 'F4']).filter(13, 30).get_data()[0] - raw.copy().pick_channels(['F3', 'F4']).filter(13, 30).get_data()[1])

        result_dict = {
            'Delta': delta,
            'Theta': theta,
            'Alpha': alpha,
            'Beta': beta,
            'Gamma': gamma,
            'ERP1': erp1,
            'ERP2': erp2,
            'Asymmetry': asymmetry
        }

        # Append the result dictionary to the list
        all_results.append(result_dict)

# Convert the list of dictionaries to a pandas DataFrame
result_df = pd.DataFrame(all_results)

# Save the DataFrame to an Excel file
excel_file_path = r"C:\Users\priya\OneDrive\Desktop\major\output_combined.xlsx"
result_df.to_excel(excel_file_path, index=False)

# Print a message indicating the completion of the process
print("Data for all files saved to Excel file:", excel_file_path)
