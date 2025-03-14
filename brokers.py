import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from fpdf import FPDF

class Client:
    def __init__(self, name, age, income, expenses, liabilities, investments, dependents, risk_appetite, goals):
        self.name = name
        self.age = age
        self.income = income
        self.expenses = expenses
        self.liabilities = liabilities
        self.investments = investments
        self.dependents = dependents
        self.risk_appetite = risk_appetite
        self.goals = goals
        self.sip_amount = None
        self.sip_years = None

class Broker:
    def __init__(self, client):
        self.client = client
        self.investment_options = {
            "Small Cap Funds": {
                "Bandhan Mutual Fund": 34.35,
                "Nippon India Small Cap Fund": 34.36,
                "SBI Small Cap Fund": 26.23
            },
            "Mid Cap Funds": {
                "Motilal Oswal Fund": 28.24,
                "HDFC Mid-Cap Fund": 23.68,
                "Quant Mid Cap": 20.58
            },
            "Large Cap Funds": {
                "ICICI Bluechip Fund": 16.44,
                "UTI Nifty Next 50 Index Fund": 14.14
            },
            "Fixed Deposits": {"FD Interest Rate": 7.5}
        }

    def suggest_investments(self):
        if self.client.age < 25:
            return ["Small Cap Funds", "Mid Cap Funds"]
        elif 26 <= self.client.age <= 40:
            return ["Mid Cap Funds", "Large Cap Funds", "Fixed Deposits"]
        else:
            return ["Large Cap Funds", "Fixed Deposits"]

    def calculate_sip(self, goal_amount, rate, years):
        months = years * 12
        r = (rate / 100) / 12
        sip = goal_amount / (((1 + r) ** months - 1) / r / (1 + r))
        return max(500, sip)

    def recommend_sip(self):
        max_sip = 500
        max_years = 0
        for goal, years in self.client.goals.items():
            rate = 12
            sip = self.calculate_sip(1000000, rate, years)
            if sip > max_sip:
                max_sip = sip
                max_years = years
        self.client.sip_amount = max_sip
        self.client.sip_years = max_years

    def generate_sip_growth_chart(self, sip_amount, rate, years):
        months = years * 12
        r = (rate / 100) / 12
        sip_values = []
        total_invested = 0
        total_value = 0

        for month in range(1, months + 1):
            total_invested += sip_amount
            total_value = total_value * (1 + r) + sip_amount
            sip_values.append(total_value)

        plt.figure(figsize=(10, 5))
        plt.plot(range(1, months + 1), sip_values, label="SIP Growth", color="blue")
        plt.xlabel("Months")
        plt.ylabel("Total Value (Rs)")
        plt.title("SIP Growth Over Time")
        plt.legend()

        plt.xticks(np.arange(0, months + 1, step=12), rotation=45)
        plt.grid(True)
        plt.savefig("sip_growth.png")
        plt.close()

    def generate_report(self):
        self.recommend_sip()
        self.generate_sip_growth_chart(self.client.sip_amount, 12, self.client.sip_years)

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", "B", 16)
        pdf.cell(200, 10, txt="INVESTMENT REPORT", ln=True, align='C')
        pdf.ln(10)

        pdf.set_font("Arial", size=12)
        pdf.multi_cell(0, 10, txt=f"Client **{self.client.name}**, Age **{self.client.age}**, Income **Rs {self.client.income}**, "
                                  f"Expenses **Rs {self.client.expenses}**, Liabilities **Rs {self.client.liabilities}**, "
                                  f"Risk Appetite: **{self.client.risk_appetite}**.")

        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt="Recommended SIP:", ln=True)
        pdf.set_font("Arial", size=12)
        pdf.cell(200, 10, txt=f"Rs {self.client.sip_amount:.2f} per month for {self.client.sip_years} years", ln=True)
        
        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt="Suggested Investment Plans:", ln=True)
        pdf.set_font("Arial", size=12)

        suggested_categories = self.suggest_investments()
        for category in suggested_categories:
            funds = self.investment_options[category]
            fund_list = ', '.join([f"{name} ({rate}%)" for name, rate in funds.items()])
            pdf.cell(200, 10, txt=f"{category}: {fund_list}", ln=True)

        pdf.ln(10)
        pdf.set_font("Arial", "B", 12)
        pdf.cell(200, 10, txt="SIP Growth Chart:", ln=True)
        pdf.image("sip_growth.png", x=10, y=pdf.get_y(), w=180)

        pdf.output(r"E:\Linkedin Journey\DATA SCIENCE\Brokers Advice\investment_report.pdf")

# User Input
name = input("Enter your name: ")
age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))
expenses = float(input("Enter your monthly expenses: "))
liabilities = float(input("Enter your liabilities (loans, EMIs, etc.): "))
investments = float(input("Enter your current investments: "))
dependents = input("Do you have dependents? (yes/no): ").strip().lower() == "yes"
risk_appetite = input("Enter your risk appetite (Conservative, Moderate, Aggressive): ")

goals = {}
while True:
    goal = input("Enter a financial goal (or type 'done' to finish): ")
    if goal.lower() == "done":
        break
    years = int(input(f"In how many years do you want to achieve {goal}? "))
    goals[goal] = years

client = Client(name, age, income, expenses, liabilities, investments, dependents, risk_appetite, goals)
broker = Broker(client)
print("\nSuggested Investments:", broker.suggest_investments())

broker.generate_report()
