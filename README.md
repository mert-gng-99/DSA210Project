-----

# DSA 210 Introduction to Data Science: Project Proposal

**Project Title:** Analyzing the Link Between Economic Growth and CO₂ Emissions: A Study of the Environmental Kuznets Curve

**Student Name:** Mert Güngör

## Table of Contents

1.  [Motivation](https://www.google.com/search?q=%231-motivation-why-this-project-is-important)
2.  [Data Sources](https://www.google.com/search?q=%232-data-sources-where-the-data-comes-from)
3.  [Data Collection Plan](https://www.google.com/search?q=%233-data-collection-plan-how-i-will-get-the-data)
4.  [Methodology](https://www.google.com/search?q=%234-methodology-how-i-analyzed-the-data)
5.  [Analysis and Findings](https://www.google.com/search?q=%235-analysis-and-findings)
6.  [Conclusion](https://www.google.com/search?q=%236-conclusion)

-----

## 1\. Motivation (Why this project is important)

### The Problem

Climate change is a big problem for the world, and it is mainly caused by carbon dioxide (CO₂) emissions [1, 2]. In the past, when a country's economy grew, its CO₂ emissions also grew. This is because economic growth often needs more energy, and this energy usually comes from burning fossil fuels [3].

This project studies the relationship between a country's economic level and its CO₂ emissions. We want to understand if countries can grow their economies without increasing pollution.

### The Main Idea: Environmental Kuznets Curve (EKC)

There is a theory called the Environmental Kuznets Curve (EKC). This theory says that when a country is poor and starts to grow, its pollution increases. But, after it reaches a certain level of wealth, the country starts to use cleaner technology and becomes more efficient. Then, its pollution starts to decrease, even if the economy continues to grow. This relationship looks like an inverted "U" shape [4, 5, 6].

### Research Question

This project tries to answer a simple question:
*"Does the data from 1990 to 2022 show an inverted U-shaped relationship between a country's wealth (GDP per capita) and its pollution (CO₂ emissions per capita)?"*

-----

## 2\. Data Sources (Where the data comes from)

This project follows the course rules by using a public dataset and adding another dataset to it.

### Main Dataset

  * **Dataset Name:** Our World in Data (OWID) - "CO₂ and Greenhouse Gas Emissions" [8, 2]
  * **What it is:** This is a large and trusted dataset with information about CO₂ emissions for many countries over many years [9, 10].
  * **Source:** OWID collects this data from top scientific sources like the Global Carbon Project [8, 11].

### Enriching Dataset

  * **Dataset Name:** The World Bank - "World Development Indicators" [12, 13]
  * **What it is:** This dataset provides the economic information for each country. I used the "GDP per capita, PPP" indicator.
  * **Why this data:** This specific GDP measure is the best for comparing how rich countries are because it adjusts for differences in the cost of living [14]. This makes the comparison fair.

### Dataset Details (Key Columns)

The final combined dataset includes these important columns:

  * `country`: The name of the country/region.
  * `year`: The year of the observation (ranging from 1990 to 2022).
  * `iso_code`: The 3-letter code for the country (used to filter out continents).
  * `co2_per_capita`: Carbon dioxide emissions measured in tonnes per person.
  * `gdp`: Gross Domestic Product per capita, adjusted for inflation and purchasing power.

-----

## 3\. Data Collection Plan (How I got the data)

Both datasets are free and easy to download. The process was:

1.  **Get the CO₂ Data:**

      * I downloaded the "CO₂ and Greenhouse Gas Emissions" dataset as a CSV file from the Our World in Data GitHub page [8].
      * **Download Link:** `https://nyc3.digitaloceanspaces.com/owid-public/data/co2/owid-co2-data.csv`

2.  **Get the Economic Data:**

      * I downloaded the "GDP per capita, PPP" data as a CSV file from the World Bank's official data website [15, 16].
      * **Download Link:** `https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.KD`

3.  **Combine the Data:**

      * I used Python (Pandas library) to merge these two files. I matched the data for each country and each year using the `iso_code` and `year`. This created one single, clean dataset ready for analysis.

-----

## 4\. Methodology (How I analyzed the data)

In this project, I used Python libraries like Pandas, Matplotlib, Seaborn, and Scipy. My analysis followed these steps:

### A. Data Cleaning and Preparation

Before analysis, I prepared the data:

  * I merged the CO₂ and GDP datasets based on country codes and years.
  * I filtered the data to include years from 1990 to 2022.
  * I removed rows with missing values (NaNs) or zero values to prevent errors during calculation.
  * I checked for outliers using box plots.

### B. Exploratory Data Analysis (EDA)

I explored the data to understand the distributions:

  * **Logarithmic Transformation:** Because most countries have low GDP and low emissions, the data was crowded in the charts. To see the relationship better, I used a **Log Scale** for both GDP and CO₂ charts.
  * **Visualizations:** I created histograms to see data distribution and scatter plots to analyze the relationship.

### C. Hypothesis Testing

I tested if there is a statistical relationship between economic growth and pollution.

  * **Null Hypothesis ($H_0$):** There is no significant correlation between GDP per capita and CO₂ emissions.
  * **Alternative Hypothesis ($H_A$):** There is a significant correlation between GDP per capita and CO₂ emissions.
  * **Method:** I used the **Pearson Correlation Coefficient** on the log-transformed data and calculated the **p-value**. I used a significance level (alpha) of 0.05.

-----
<img width="1389" height="489" alt="logdistofco2" src="https://github.com/user-attachments/assets/6a8ca48a-dcd5-4d6e-b0a4-164562d32dcb" />
<img width="857" height="552" alt="gdpandco2mixed" src="https://github.com/user-attachments/assets/54d1e3a2-4334-4694-a0f9-56ba94f2d30f" />


## 5\. Analysis and Findings

### Data Distributions

First, I looked at how GDP and CO₂ emissions are distributed across the world.

**GDP Distribution:**
*The histogram above shows the distribution of GDP per capita using a log scale.*

**CO₂ Distribution:**
*The histogram above shows the distribution of CO₂ emissions per capita using a log scale.*

### Relationship Between GDP and CO₂

This is the most important part of the analysis. I plotted GDP vs. CO₂ emissions for the year 2019 (pre-pandemic data) to see the trend clearly.

  * **Observation:** The scatter plot shows a clear upward trend. The red line represents the regression line (trend line).
  * **Interpretation:** As countries get richer (move to the right), their CO₂ emissions tend to increase (move up).

### Statistical Test Results

I performed a Pearson Correlation test on the log-transformed data for the entire dataset (1990-2022).

  * **Pearson Correlation Coefficient:** `0.90`
  * **P-value:** `0.0` (virtually zero)

**Result:** Since the p-value is less than 0.05, I **REJECT** the Null Hypothesis.

-----

## 6\. Conclusion

My analysis shows a **very strong, positive relationship** (Correlation: 0.90) between a country's wealth (GDP) and its carbon footprint.

1.  **Economic Growth increases Pollution:** Globally, as countries develop economically, they consume more energy and produce more CO₂.
2.  **No Inverted "U" (Yet):** The global data does not clearly show the "inverted U" shape predicted by the Environmental Kuznets Curve. Instead, we see a linear increase. This might mean that most countries are still in the "scale effect" phase, where growth leads to more emissions.
3.  **Statistical Significance:** The relationship is statistically significant, meaning it is not due to random chance.

### Future Work

In the next steps, I could look at individual developed countries separately. It is possible that the "inverted U" shape (emissions going down) only happens in very rich countries, and looking at the global average hides this trend.

-----

### References

[1] IPCC, 2021: Climate Change 2021.
[2] Ritchie, H., Roser, M. (2020) - "CO₂ and Greenhouse Gas Emissions". OurWorldInData.org.
[3] Stern, D. I. (2004). The Rise and Fall of the Environmental Kuznets Curve.
[4] Grossman, G. M., & Krueger, A. B. (1991). Environmental Impacts of a North American Free Trade Agreement.
[5] Kuznets, S. (1955). Economic Growth and Income Inequality.
[6] Panayotou, T. (1993). Empirical Tests and Policy Analysis of Environmental Degradation.
[7] Dasgupta, S., et al. (2002). Confronting the Environmental Kuznets Curve.
[8] OWID CO2 Data GitHub Repository. [https://github.com/owid/co2-data](https://github.com/owid/co2-data)
[9] Global Carbon Project. (2022).
[10] Jones, M. W., et al. (2023). Scientific Data.
[11] Friedlingstein, P., et al. (2022). Earth System Science Data.
[12] The World Bank. (2023). World Development Indicators.
[13] The World Bank Group. GDP per capita, PPP.
[14] Callen, T. (2020). PPP Versus the Market. IMF.
[15] World Bank Open Data. [https://data.worldbank.org/](https://data.worldbank.org/)
[16] World Bank Data Catalog.
