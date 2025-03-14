# Investment Report Generator

## Overview
The **Investment Report Generator** is a Python-based financial planning tool that helps users analyze their income, expenses, liabilities, and risk appetite to generate a **personalized investment report**. The project calculates the recommended **Systematic Investment Plan (SIP)** amount and suggests suitable investment options. A **detailed PDF report** is generated, including investment suggestions and a visualized SIP growth forecast.

## Features
- **User Input Handling:** Collects financial data such as income, expenses, liabilities, and financial goals.
- **Risk-based Investment Suggestions:** Suggests investment options based on the user's age and risk appetite.
- **SIP Calculation:** Estimates the required **SIP amount** to achieve a financial goal in a specified time.
- **Automated PDF Report Generation:** Provides a professional **Investment Report** with suggested funds and a **growth projection graph**.
- **Graph Visualization:** Generates and embeds a SIP growth chart for better financial insight.

### Technologies Used:
- **Python**: Core logic and computation.
- **Matplotlib & NumPy:** For generating and displaying investment growth graphs.
- **Pandas:** To manage financial data.
- **FPDF:** For generating a professional **Investment Report PDF**.

## How It Works
1. **User Input:** Collects age, income, expenses, liabilities, and financial goals.
2. **Risk Analysis:** Determines risk appetite and suitable investment category (Equity, Small Cap, Large Cap, etc.).
3. **SIP Calculation:** Recommends a **monthly SIP investment amount** based on financial goals and expected returns.
4. **Report Generation:** A PDF report is created with a breakdown of investment recommendations and a **SIP growth projection chart**.

## Installation & Usage
1. Install required libraries:
   ```bash
   pip install matplotlib numpy pandas fpdf
   ```
2. Run the script:
   ```bash
   python investment_report.py
   ```
3. Enter the required financial details.
4. The program will suggest investments and generate an **Investment Report PDF**.

## Output
- A **personalized PDF report** named `investment_report.pdf` is generated with:
  - User's financial details summary
  - **Recommended SIP amount & duration**
  - **Suggested investments** based on risk appetite
  - A **growth projection graph** for better financial insights

This project is ideal for individual investors, financial brokers, and data science enthusiasts interested in financial analytics and personalized investment strategies.

