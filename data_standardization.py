import pandas as pd

# Load data
df = pd.read_csv("synthetic_customer_data.csv")

# Standardize email and remove non-numeric characters from device_id
df["email"] = df["email"].str.lower()
df["device_id"] = df["device_id"].str.replace(r"\D", "", regex=True)

# Save cleaned data
df.to_csv("cleaned_data.csv", index=False)
print("✅ Data cleaned and saved as cleaned_data.csv")
