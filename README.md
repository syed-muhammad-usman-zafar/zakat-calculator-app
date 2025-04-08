# Zakat Calculator App

A Streamlit-based web application for calculating Zakat (Islamic obligatory charity) based on various assets and liabilities.


## Description

This Zakat Calculator app helps Muslims determine their Zakat obligation by calculating the total wealth, comparing it against the Nisab threshold, and computing the amount of Zakat due (2.5% of eligible wealth). The app supports multiple currencies and provides a visual representation of wealth distribution.

## Features

- Calculate Zakat based on various assets and liabilities
- Compare wealth against the Nisab threshold (minimum amount for Zakat eligibility)
- Support for multiple currencies (PKR, GBP, AED, USD)
- Real-time currency conversion using forex-python
- Visual representation of wealth distribution with interactive pie charts
- Simple and intuitive user interface

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/yourusername/zakat-calculator.git
   cd zakat-calculator
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Requirements

- Python 3.7+
- Streamlit
- forex-python
- plotly

Create a `requirements.txt` file with:
```
streamlit
forex-python
plotly
```

## Usage

1. Run the Streamlit app:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL displayed in your terminal (typically http://localhost:8501)

3. Fill in the form with your financial information:
   - Select your currency
   - Enter your cash on hand and in bank accounts
   - Enter the value of gold and silver
   - Enter the value of investments
   - Enter the value of business merchandise
   - Enter the value of income-generating property
   - Enter money owed to you
   - Enter your debts and liabilities
   - Enter current gold and silver prices per gram in PKR

4. Click the "Calculate Zakat" button to see your Zakat obligation

5. View the wealth distribution chart to understand your asset allocation

## How Zakat is Calculated

1. All assets are converted to the same currency (PKR)
2. Net wealth is calculated by subtracting liabilities from total assets
3. Nisab threshold is determined as the minimum of:
   - Value of 87.48 grams of gold
   - Value of 612.36 grams of silver
4. If net wealth exceeds the Nisab threshold, Zakat is calculated as 2.5% of net wealth

## Deployment

This app can be deployed on Streamlit Sharing, Heroku, or any other platform that supports Python web applications.

### Streamlit Sharing Deployment

1. Push your code to a GitHub repository
2. Go to [Streamlit Sharing](https://share.streamlit.io/)
3. Sign in with GitHub
4. Deploy the app by selecting your repository

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Author

Created by Usman Zafar


## Disclaimer

This calculator is provided for educational and informational purposes only. For definitive Zakat calculations, please consult with a qualified Islamic scholar or financial advisor.
