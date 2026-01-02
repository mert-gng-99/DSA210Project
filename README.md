# DSA 210 Introduction to Data Science: Project Report

**Project Title:** The Price of Wealth: A Deep Dive into Economic Growth and Carbon Emissions (1990-2020)

**Student Name:** Mert Güngör

---

## Table of Contents
1.  [Introduction and Motivation](#1-introduction-and-motivation)
2.  [The Data We Used](#2-the-data-we-used)
3.  [Step-by-Step Methodology](#3-step-by-step-methodology)
4.  [Part 1: The Global Picture (Correlation)](#4-part-1-the-global-picture-correlation)
5.  [Part 2: Adding Time (Temporality Analysis)](#5-part-2-adding-time-temporality-analysis)
6.  [Part 3: Testing the Theory (EKC Hypothesis)](#6-part-3-testing-the-theory-ekc-hypothesis)
7.  [Part 4: Machine Learning Analysis](#7-part-4-machine-learning-analysis)
8.  [Final Conclusion](#8-final-conclusion)
9.  [Limitations and What's Next](#9-limitations-and-whats-next)

---

## 1. Introduction and Motivation

### Why is this topic important?
Global warming is one of the biggest dangers to our planet. The main cause of global warming is a gas called **Carbon Dioxide ($CO_2$)**. We produce this gas when we drive cars, use electricity, or run factories.

For a long time, people believed that **money equals pollution**. If a country wants to be rich (have a high GDP), it must build more factories and burn more oil. This project asks a very important question:
> *"Is it possible for a country to get richer but also cleaner?"*

### The Main Theory: The Environmental Kuznets Curve (EKC)
Scientists have a theory about this. It is like a story with three parts:
1.  **The Beginning (Poor Phase):** A country is poor. It starts to build basics like roads and electricity. Pollution goes **UP** very fast.
2.  **The Middle (Turning Point):** The country becomes rich. People start to care about clean air. They have money for better technology (like solar power).
3.  **The End (Rich Phase):** The country gets even richer, but pollution starts to go **DOWN**.

This project tests if this "inverted U-shape" story is true using real world data.

---

## 2. The Data We Used

To answer this question, I needed two types of information for every country in the world. I combined two very trusted sources.

### Source A: The Pollution Data
*   **Where from?** "Our World in Data" (OWID).
*   **What is it?** It measures $CO_2$ emissions.
*   **Unit:** "Tonnes per person". This is important because big countries like China naturally have more pollution. Measuring "per person" makes it fair to compare China with a small country like Belgium.

### Source B: The Money Data
*   **Where from?** The World Bank.
*   **What is it?** GDP (Gross Domestic Product) per capita.
*   **Unit:** US Dollars (adjusted for inflation/PPP). This tells us the average income of a person in that country.

**The Final Table:**
After joining these sources, I had a big table with columns like:
*   `Country`: Name (e.g., Turkey, USA)
*   `Year`: 1990 to 2020
*   `GDP`: How rich they are.
*   `CO2`: How much they pollute.

---

## 3. Step-by-Step Methodology

I used the Python programming language to do this work. Here is exactly what I did:

### Step 1: Cleaning the Data
Real data is often messy.
*   I removed lines where data was missing (for example, if we knew the GDP but not the CO2).
*   I removed very small countries or islands that had errors in the data.
*   I focused on the years **1990 to 2020** because this is the most important time for modern industry.

### Step 2: "Log Scale" Transformation
**Problem:** The difference between poor countries and rich countries is huge. Some make \$1,000, some make \$60,000. If you put them on a normal chart, all the poor countries get squashed into the corner.
**Solution:** I used a "Logarithmic Scale". This spreads out the data so we can see the differences between poor and developing nations much better.

### Step 3: Different Types of Analysis
*   **Static Analysis:** Looking at just one year (2019) to see a snapshot.
*   **Time Analysis:** Looking at how things change year by year (like a movie).
*   **Math Test:** Using a formula called "Polynomial Regression" to scientifically test the curve.
*   **Machine Learning:** Using advanced computer algorithms to predict pollution.

---

## 4. Part 1: The Global Picture (Correlation)

First, I looked at the whole world at once for the year 2019.

### The Findings
I visualized the relationship between GDP and Carbon Emissions.

*(Figure 1: Global Scatter Plot - 2019)*
<img width="800" alt="gdpandco2mixed" src="https://github.com/user-attachments/assets/54d1e3a2-4334-4694-a0f9-56ba94f2d30f" />

*   **What we see:** The dots go up from left to right. This is a straight line, not a curve.
*   **The Statistic:** The correlation score is **0.90**. (1.0 is a perfect match).
*   **Interpretation:** This is bad news. In 2019, generally speaking, **more money still meant more pollution**. The global trend has not turned down yet.

---

## 5. Part 2: Adding Time (Temporality Analysis)

The previous chart was just a photo. Now let's look at the "movie" from 1990 to 2020. This helps us see the direction countries are moving.

### A. Tracking Specific Countries
I picked roughly 6 important countries to represent the world:
*   **Developing:** China, India, Brazil, Turkey.
*   **Developed:** USA, Germany.

*(Figure 2: Time Series Analysis)*
<img width="1189" height="590" alt="co2emissionpercapitaovertime" src="https://github.com/user-attachments/assets/e38f50c1-3a78-41e8-96ee-3e0b567db53d" />

**Observation:**
*   Look at **China (Orange)** and **India**: Their lines are shooting up! They are getting richer, but polluting much more.
*   Look at the **USA (Blue)** and **Germany**: Their lines are slowly going **DOWN**. This is the key finding! They are rich, but they are reducing emissions.

### B. The World Over Decades
I also made "snapshots" for the years 1990, 2000, 2010, and 2020 to see if the global cloud of dots moved.

*(Figure 3: Decadal Snapshots)*
<img width="1389" height="985" alt="evoulution of gdp vs co2relationship" src="https://github.com/user-attachments/assets/9485278e-541b-4325-94ac-ea0a8f942ec1" />

**Observation:** The pattern stays mostly the same (positive line), but the whole world is slowly moving to the top-right (richer and dirtier).

---

## 6. Part 3: Testing the Theory (EKC Hypothesis)

Finally, I used mathematics to test the "Environmental Kuznets Curve" theory specifically for a rich country: the **USA**.

**The Logic:**
I fitted a curve formula ($y = ax^2 + bx + c$) to the USA data.
*   If the curve bends **UP**, pollution is out of control.
*   If the curve bends **DOWN** (Inverted U), the theory is correct.

*(Figure 4: EKC Test for USA)*

<img width="848" height="548" alt="ekc hypothesis testing usa" src="https://github.com/user-attachments/assets/ae0ea49f-13da-4c42-9898-d23eaa94a466" />

**Statistical Result:**
*   The math shows a **negative curve** (Coefficient is -1.35e-09).
*   The "P-value" is 0.000 (which means the result is definitely real, not luck).

**Verdict:** The theory is **TRUE** for the USA. They have passed the peak and are now in the "cleaner" phase.

---

## 7. Part 4: Machine Learning Analysis

In this final part, I used advanced Machine Learning (ML) methods to understand the data even better.

### A. Regression (Prediction)
I asked the question: *"Can we predict how much CO2 a country produces if we only know its GDP and Population?"*
*   **Method:** Random Forest Regressor (A machine learning model that uses many decision trees).
*   **Result (R² Score):** 0.86. This means the model is **86% accurate**!


<img width="846" height="470" alt="regressionresult" src="https://github.com/user-attachments/assets/ec0561ae-ae33-44d0-8ddf-3526d4bf9284" />

**Graph Interpretation:**
*   In the graph above, the **Red Dashed Line** represents a "perfect guess".
*   The **Green Dots** are the model's predictions.
*   **Observation:** Most green dots are very close to the red line. This shows that Wealth (GDP) and Population are very strong indicators of pollution. The model works well.

### B. Classification (Yes/No Estimate)
I asked the question: *"Can we classify if a country is a 'High Polluter' or 'Low Polluter'?"*
*   **Method:** Random Forest Classifier.
*   **Result (Accuracy):** 92%. The model guesses correctly 92 times out of 100.

<img width="513" height="470" alt="confusionmatrix (randomforestclassification)" src="https://github.com/user-attachments/assets/b1545e08-e58d-4554-96a1-79f44b29ea1e" />

**Graph Interpretation (Confusion Matrix):**
*   **Dark Blue Squares** show the correct guesses.
    *   **599** times it correctly said "Low Polluter".
    *   **592** times it correctly said "High Polluter".
*   **Light Blue Squares** show the mistakes (only 49 and 55 errors).
*   **Meaning:** The computer is very good at separating clean countries from dirty countries using economic data.

### C. Unsupervised Learning (Clustering)
I set a goal: *"Don't use any labels. Just look at the data and find natural groups of countries."*
*   **Method:** K-Means Clustering.


<img width="857" height="552" alt="kmeansclustering" src="https://github.com/user-attachments/assets/08993b80-7715-4607-b728-65d999c048bf" />

**Graph Interpretation:**
The colors show the 3 different groups the model found:
1.  **Purple Dots (Low GDP, Low CO2):** These are poor countries. They don't have much money, but they also don't pollute much.
2.  **Green Dots (Middle):** These are developing nations (like Turkey, Brazil). They are getting richer and starting to pollute more.
3.  **Yellow Dots (High GDP, High CO2):** These are rich countries (like USA, Europe). They are wealthy but have high emissions.

### D. PCA Analysis (Visualizing the Groups)
Data is complex (3D). I used PCA to flatten it to 2D so we can see it easily.

<img width="833" height="547" alt="pcaanalysis" src="https://github.com/user-attachments/assets/d1c7f5f2-10c2-43aa-827c-41a43cfca33a" />

**Graph Interpretation:**
*   Even when we flatten the data, we can still see the **3 separate colors (groups)** clearly.
*   This proves that the groups are real and distinct, not just random.

### E. Time Series (Predicting the Future)
Finally, I asked: *"What will happen to the USA in the next 5 years?"*
*   **Method:** ARIMA (AutoRegressive Integrated Moving Average).


<img width="842" height="470" alt="timeseriesforecasting" src="https://github.com/user-attachments/assets/94f0d00b-8203-4a20-b857-fc44b81b5ec1" />

**Graph Interpretation:**
*   **Blue Line:** This is real history (1990-2020). You can see the pollution going down recently.
*   **Red Dashed Line:** This is the model's prediction for 2021-2025.
*   **Conclusion:** The model predicts that the USA's emissions will **continue to drop**. The trend is good!

### F. Causal Inference (Cause & Effect)
Correlation is not causation. Just because rich countries pollute, does it mean money causes pollution?

*   **Method:** Inverse Propensity Weighting (IPW). This is a statistical method to remove the effect of other factors (like population size) to see the pure effect of wealth.
*   **Result (ATE):** 7.52.
*   **Interpretation:** Being a "High Income" country causes an average increase of 7.52 tonnes of CO2 per person, independent of population size. This proves the link is causal, not just a coincidence.

![Causal Inference](causal_inference.png)

### G. Fairness & Bias Check (Ethics)
I checked if my Machine Learning model is "fair". Does it work equally well for rich and poor countries?

*   **Method:** Error Analysis by Group.
*   **Finding:** The model had slightly higher errors for very poor nations because their data is sometimes missing or noisy.
*   **Conclusion:** While the model is accurate globally, future improvements should focus on getting better data for developing nations to ensure the model is fair to everyone.

![Fairness Check](fairness_check.png)

---

## 8. Final Conclusion

This project reveals a complex story about our world:

1.  **The Bad News:** For most of the world (especially developing nations), economic growth still causes massive pollution. The global link is very strong ($0.90$ correlation).
2.  **The Good News:** It is possible to change! My analysis of the USA and Germany proves that **you can be rich and green**. Once a country reaches a high level of development, it can decouple money from carbon.
3.  **The Hope:** Developing countries (like Turkey, China, India) are currently in the rising phase. We hope they can reach the "turning point" faster than Europe and the USA did, by using new technologies.

---

## 9. Limitations and What's Next

*   **Missing Pieces:** I only looked at $CO_2$. I did not look at plastic waste, deforestation, or water pollution.
*   **It's Not Just Money:** I focused on GDP. But laws, government policies, and population size also affect pollution.
*   **Future Ideas:** Next time, I would like to group countries by continent. For example, does Europe follow a different path than Asia?

---

### References
*   It is based on data from **Our World in Data** (2022) and **The World Bank** (2023).
*   Concepts are based on the **Environmental Kuznets Curve (EKC)** theory from economics literature (Grossman & Krueger, 1991).

### Tools Used
*   **Python:** For all calculations.
*   **Libraries:** Pandas (for data), Matplotlib & Seaborn (for charts), Statsmodels (for the math test).
*   **AI Assistance:** ChatGPT was used to help debug Python code and correct English grammar. The analysis design is original.
