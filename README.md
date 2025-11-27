# DSA 210 Introduction to Data Science: Project Proposal

**Project Title:** Analyzing the Link Between Economic Growth and CO₂ Emissions: A Study of the Environmental Kuznets Curve

**Student Name:** Mert Güngör

## Table of Contents
1. [Motivation](#1-motivation-why-this-project-is-important)
2. [Data Sources](#2-data-sources-where-the-data-comes-from)
3. [Data Collection Plan](#3-data-collection-plan-how-i-will-get-the-data)
4. [Methodology](#4-methodology-how-i-will-analyze-the-data)

---

## 1. Motivation (Why this project is important)

### The Problem
Climate change is a big problem for the world, and it is mainly caused by carbon dioxide (CO₂) emissions [1, 2]. In the past, when a country's economy grew, its CO₂ emissions also grew. This is because economic growth often needs more energy, and this energy usually comes from burning fossil fuels [3].

This project will study the relationship between a country's economic level and its CO₂ emissions. We want to understand if countries can grow their economies without increasing pollution.

### The Main Idea: Environmental Kuznets Curve (EKC)
There is a theory called the Environmental Kuznets Curve (EKC). This theory says that when a country is poor and starts to grow, its pollution increases. But, after it reaches a certain level of wealth, the country starts to use cleaner technology and becomes more efficient. Then, its pollution starts to decrease, even if the economy continues to grow. This relationship looks like an inverted "U" shape [4, 5, 6].

### Research Question
This project will try to answer a simple question:
*"Does the data from 1990 to 2022 show an inverted U-shaped relationship between a country's wealth (GDP per capita) and its pollution (CO₂ emissions per capita)?"*

### Why It Matters
If the EKC theory is true for CO₂ emissions, it means that economic development can help solve environmental problems in the long run [7]. This is very important for creating good policies that support both economic growth and a cleaner environment. This project will use data to see if this idea is correct.

---

## 2. Data Sources (Where the data comes from)

This project will follow the course rules by using a public dataset and adding another dataset to it.

### Main Dataset
* **Dataset Name:** Our World in Data (OWID) - "CO₂ and Greenhouse Gas Emissions" [8, 2]
* **What it is:** This is a large and trusted dataset with information about CO₂ emissions for many countries over many years [9, 10].
* **Source:** OWID collects this data from top scientific sources like the Global Carbon Project [8, 11].

### Enriching Dataset
* **Dataset Name:** The World Bank - "World Development Indicators" [12, 13]
* **What it is:** This dataset will provide the economic information for each country. I will use the "GDP per capita, PPP" indicator.
* **Why this data:** This specific GDP measure is the best for comparing how rich countries are because it adjusts for differences in the cost of living [14]. This makes the comparison fair.

### Dataset Details (Key Columns)
The final combined dataset will include these important columns:
* `country`: The name of the country/region.
* `year`: The year of the observation (ranging from 1990 to 2022).
* `iso_code`: The 3-letter code for the country (used to filter out continents).
* `co2_per_capita`: Carbon dioxide emissions measured in tonnes per person.
* `gdp`: Gross Domestic Product per capita, adjusted for inflation and purchasing power.

---

## 3. Data Collection Plan (How I will get the data)

Both datasets are free and easy to download. The plan is:

1.  **Get the CO₂ Data:**
    * I will download the "CO₂ and Greenhouse Gas Emissions" dataset as a CSV file from the Our World in Data GitHub page [8].
    * **Download Link:** `https://nyc3.digitaloceanspaces.com/owid-public/data/co2/owid-co2-data.csv`

2.  **Get the Economic Data:**
    * I will download the "GDP per capita, PPP" data as a CSV file from the World Bank's official data website [15, 16].
    * **Download Link:** `https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.KD`

3.  **Combine the Data:**
    * I will use Python and the Pandas library to combine these two files. I will match the data for each country and each year using the `iso_code` and `year`. This will create one single, clean dataset that is ready for analysis.

---

## 4. Methodology (How I will analyze the data)

In this project, I will use Python libraries like Pandas, Matplotlib, and Scipy. My analysis will have these steps:

### A. Data Cleaning and Preparation
Before analysis, I will prepare the data:
* I will merge the CO₂ and GDP datasets based on country codes and years.
* I will filter the data to include years from 1990 to 2022.
* I will handle missing values (NaNs) by removing rows that do not have both GDP and CO₂ data.
* I will check for outliers (extreme values) using **box plots** to ensure the data is correct.

### B. Exploratory Data Analysis (EDA)
I will explore the data to understand the general trends:
* **Summary Statistics:** I will calculate the mean, median, and standard deviation for GDP and CO₂ emissions.
* **Visualizations:**
    * I will use **histograms** to see the distribution of CO₂ emissions and GDP.
    * I will use **scatter plots** to visualize the relationship between GDP per capita (x-axis) and CO₂ emissions (y-axis). This is the most important step to check for the "U" shape of the Kuznets Curve.

### C. Hypothesis Testing
I will test if there is a statistical relationship between economic growth and pollution.
* **Null Hypothesis ($H_0$):** There is no significant correlation between GDP per capita and CO₂ emissions per capita.
* **Alternative Hypothesis ($H_A$):** There is a significant correlation between GDP per capita and CO₂ emissions per capita.
* **Method:** I will use the **Pearson Correlation Coefficient** and calculate the **p-value** to test this hypothesis. I will use a significance level (alpha) of 0.05.

---

### References
[1] IPCC, 2021: Climate Change 2021: The Physical Science Basis. Contribution of Working Group I to the Sixth Assessment Report of the Intergovernmental Panel on Climate Change.
[2] Ritchie, H., Roser, M. (2020) - "CO₂ and Greenhouse Gas Emissions". Published online at OurWorldInData.org.
[3] Stern, D. I. (2004). The Rise and Fall of the Environmental Kuznets Curve. World Development, 32(8), 1419–1439.
[4] Grossman, G. M., & Krueger, A. B. (1991). Environmental Impacts of a North American Free Trade Agreement. National Bureau of Economic Research.
[5] Kuznets, S. (1955). Economic Growth and Income Inequality. The American Economic Review, 45(1), 1–28.
[6] Panayotou, T. (1993). Empirical Tests and Policy Analysis of Environmental Degradation at Different Stages of Economic Development. Working Paper.
[7] Dasgupta, S., Laplante, B., Wang, H., & Wheeler, D. (2002). Confronting the Environmental Kuznets Curve. The Journal of Economic Perspectives, 16(1), 147–168.
[8] OWID CO2 Data GitHub Repository. https://github.com/owid/co2-data
[9] Global Carbon Project. (2022). Supplemental data of Global Carbon Budget 2022 (Version 1.0) [Data set].
[10] Jones, M. W., et al. (2023). National contributions to climate change due to historical emissions of carbon dioxide, methane, and nitrous oxide since 1850. Scientific Data, 10(1).
[11] Friedlingstein, P., et al. (2022). Global Carbon Budget 2022. Earth System Science Data, 14(11), 4811–4900.
[12] The World Bank. (2023). World Development Indicators. https://databank.worldbank.org/source/world-development-indicators
[13] The World Bank Group. (n.d.). GDP per capita, PPP (constant 2017 international $).
[14] Callen, T. (2020). PPP Versus the Market: Which Weight Matters? International Monetary Fund.
[15] World Bank Open Data. https://data.worldbank.org/
[16] World Bank Data Catalog. https://datacatalog.worldbank.org/search/dataset/0037712
