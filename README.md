# DSA 210 Introduction to Data Science: Project Proposal

**Project Title:** Analyzing the Link Between Economic Growth and CO₂ Emissions: A Study of the Environmental Kuznets Curve
1. [Motivation](#motivation)
2. [Research Question](#research-question)
3. [Data Sources](#data-sources)
4. [Data Collection Plan](#data-collection-plan)

## 1. Motivation (Why this project is important)

### The Problem
Climate change is a big problem for the world, and it is mainly caused by carbon dioxide (CO₂) emissions.[1, 2] In the past, when a country's economy grew, its CO₂ emissions also grew. This is because economic growth often needs more energy, and this energy usually comes from burning fossil fuels.[3]

This project will study the relationship between a country's economic level and its CO₂ emissions. We want to understand if countries can grow their economies without increasing pollution.

### The Main Idea: Environmental Kuznets Curve (EKC)
There is a theory called the Environmental Kuznets Curve (EKC). This theory says that when a country is poor and starts to grow, its pollution increases. But, after it reaches a certain level of wealth, the country starts to use cleaner technology and becomes more efficient. Then, its pollution starts to decrease, even if the economy continues to grow. This relationship looks like an inverted "U" shape.[4, 5, 6]

### Research Question
This project will try to answer a simple question:
"Does the data from 1990 to 2022 show an inverted U-shaped relationship between a country's wealth (GDP per capita) and its pollution (CO₂ emissions per capita)?"

### Why It Matters
If the EKC theory is true for CO₂ emissions, it means that economic development can help solve environmental problems in the long run.[7] This is very important for creating good policies that support both economic growth and a cleaner environment. This project will use data to see if this idea is correct.

## 2. Data Source (Where the data comes from)

This project will follow the course rules by using a public dataset and adding another dataset to it.

### Main Dataset
*   **Dataset Name:** Our World in Data (OWID) - "CO₂ and Greenhouse Gas Emissions" [8, 2]
*   **What it is:** This is a large and trusted dataset with information about CO₂ emissions for many countries over many years.[9, 10] It includes total emissions and emissions per person.
*   **Source:** OWID collects this data from top scientific sources like the Global Carbon Project.[8, 11]

### Enriching Dataset
*   **Dataset Name:** The World Bank - "World Development Indicators" [12, 13]
*   **What it is:** This dataset will provide the economic information for each country. We will use the "GDP per capita, PPP" indicator.
*   **Why this data:** This specific GDP measure is the best for comparing how rich countries are because it adjusts for differences in the cost of living.[14] This makes the comparison fair.

## 3. Data Collection Plan (How I will get the data)

Both datasets are free and easy to download. The plan is:

1.  **Get the CO₂ Data:**
    *   I will download the "CO₂ and Greenhouse Gas Emissions" dataset as a CSV file from the Our World in Data GitHub page.[8]
    *   **Download Link:** `https://nyc3.digitaloceanspaces.com/owid-public/data/co2/owid-co2-data.csv`

2.  **Get the Economic Data:**
    *   I will download the "GDP per capita, PPP" data as a CSV file from the World Bank's official data website.[15, 16]
    *   **Download Link:** `https://data.worldbank.org/indicator/NY.GDP.PCAP.PP.KD`

3.  **Combine the Data:**
    *   I will use Python and the Pandas library to combine these two files. I will match the data for each country and each year. This will create one single, clean dataset that is ready for analysis.
