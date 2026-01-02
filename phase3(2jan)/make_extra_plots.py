import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# 1. Load and Prepare Data (Same as notebook)
gdp_df = pd.read_csv('API_NY.GDP.PCAP.PP.KD_DS2_en_csv_v2_130128.csv', skiprows=4)
co2_df = pd.read_csv('owid-co2-data (1).csv')

gdp_clean = gdp_df.drop(columns=['Indicator Name', 'Indicator Code', 'Unnamed: 69'], errors='ignore')
gdp_long = gdp_clean.melt(id_vars=['Country Name', 'Country Code'], 
                          var_name='year', 
                          value_name='gdp_per_capita')
gdp_long['year'] = pd.to_numeric(gdp_long['year'], errors='coerce')
gdp_long = gdp_long.dropna(subset=['year', 'gdp_per_capita'])
gdp_long['year'] = gdp_long['year'].astype(int)

co2_clean = co2_df[['iso_code', 'country', 'year', 'co2_per_capita', 'population']]
co2_clean = co2_clean.dropna(subset=['co2_per_capita', 'iso_code'])

data = pd.merge(gdp_long, co2_clean, left_on=['Country Code', 'year'], right_on=['iso_code', 'year'])
data = data.dropna()

# --- WEEK 11: CAUSAL INFERENCE (Inverse Propensity Weighting) ---
# T = Treatment (High Income, e.g. > Median GDP)
# Y = Outcome (CO2 Emissions)
# X = Confounder (Population)

median_gdp = data['gdp_per_capita'].median()
data['treatment'] = (data['gdp_per_capita'] > median_gdp).astype(int)

# 1. Estimate Propensity Score (Probability of being High Income given Population)
# We use log population because population scale varies hugely
data['log_pop'] = np.log(data['population'])
propensity_model = LogisticRegression()
propensity_model.fit(data[['log_pop']], data['treatment'])
data['ps'] = propensity_model.predict_proba(data[['log_pop']])[:, 1]

# 2. Calculate Weights (IPW)
# Weight = 1/PS for Treated, 1/(1-PS) for Control
data['weight'] = np.where(data['treatment'] == 1, 
                          1 / data['ps'], 
                          1 / (1 - data['ps']))

# 3. Calculate Average Treatment Effect (ATE) using weighted means
weighted_mean_treated = np.average(data[data['treatment']==1]['co2_per_capita'], 
                                   weights=data[data['treatment']==1]['weight'])
weighted_mean_control = np.average(data[data['treatment']==0]['co2_per_capita'], 
                                   weights=data[data['treatment']==0]['weight'])

ate = weighted_mean_treated - weighted_mean_control
print(f"Estimated ATE: {ate:.2f}")

# Visualization for Causal Inference: Propensity Score Distribution
plt.figure(figsize=(10, 6))
sns.kdeplot(data[data['treatment'] == 0]['ps'], fill=True, label='Control (Low Income)', color='blue', alpha=0.3)
sns.kdeplot(data[data['treatment'] == 1]['ps'], fill=True, label='Treated (High Income)', color='orange', alpha=0.3)
plt.title('Propensity Score Overlap (Checking if groups are comparable)')
plt.xlabel('Propensity Score (Probability of being High Income)')
plt.ylabel('Density')
plt.legend()
plt.savefig('causal_inference.png')
plt.close()


# --- WEEK 14: FAIRNESS & BIAS CHECK ---
# Check if model error varies by group (Rich vs Poor)

# Reuse the Regression setup
X = data[['gdp_per_capita', 'population', 'year']]
y = data['co2_per_capita']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_model = RandomForestRegressor(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Calculate Errors on Test Set
test_data = X_test.copy()
test_data['actual_co2'] = y_test
test_data['predicted_co2'] = rf_model.predict(X_test)
test_data['error'] = abs(test_data['actual_co2'] - test_data['predicted_co2'])

# Define Groups (Rich vs Poor based on Median of TEST set)
threshold = test_data['gdp_per_capita'].median()
test_data['group'] = np.where(test_data['gdp_per_capita'] > threshold, 'High Income', 'Low Income')

# Calculate Mean Absolute Error by Group
group_errors = test_data.groupby('group')['error'].mean()

# Visualization
plt.figure(figsize=(8, 6))
sns.barplot(x=group_errors.index, y=group_errors.values, palette=['orange', 'blue'])
plt.title('Model Fairness: Average Error by Income Group')
plt.ylabel('Mean Absolute Error (Lower is Better)')
plt.xlabel('Income Group')
plt.savefig('fairness_check.png')
plt.close()
