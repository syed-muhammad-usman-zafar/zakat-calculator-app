import streamlit as st
from forex_python.converter import CurrencyRates
import plotly.express as px

st.markdown(
    """
    <div style='text-align: left;'>
        <span style='font-weight: normal;'>Created by Usman Zafar</span>
    </div>
    """, 
    unsafe_allow_html=True
)

# Function to calculate Zakat
def calculate_zakat(cash, gold, silver, investments, business_merchandise, property, receivables, debts, gold_price, silver_price, exchange_rate):
    # Convert all inputs to base currency (e.g., USD)
    total_wealth = (cash + gold + silver + investments + business_merchandise + property + receivables) * exchange_rate
    net_wealth = total_wealth - (debts * exchange_rate)
    
    # Calculate Nisab in base currency
    nisab_gold = 87.48 * gold_price
    nisab_silver = 612.36 * silver_price
    nisab = min(nisab_gold, nisab_silver)
    
    if net_wealth > nisab:
        zakat = 0.025 * net_wealth
    else:
        zakat = 0
    
    return zakat, net_wealth, nisab

# Streamlit app layout
st.title("Zakat Calculator App")


currency_options = ['PKR', 'GBP', 'AED','USD']
currency = st.selectbox("Select your currency", currency_options)

# Get the latest exchange rates
c = CurrencyRates()
exchange_rate = c.get_rate(currency, 'PKR')

cash = st.number_input("Cash on hand and in bank", min_value=0.0)
gold = st.number_input("Value of gold", min_value=0.0)
silver = st.number_input("Value of silver", min_value=0.0)
investments = st.number_input("Value of investments", min_value=0.0)
business_merchandise = st.number_input("Value of business merchandise", min_value=0.0)
property = st.number_input("Value of income-generating property", min_value=0.0)
receivables = st.number_input("Money owed to you", min_value=0.0)
debts = st.number_input("Debts and liabilities", min_value=0.0)
gold_price = st.number_input("Current gold price per gram in PKR", min_value=0.0)
silver_price = st.number_input("Current silver price per gram in PKR", min_value=0.0)

if st.button("Calculate Zakat"):
    zakat, net_wealth, nisab = calculate_zakat(cash, gold, silver, investments, business_merchandise, property, receivables, debts, gold_price, silver_price, exchange_rate)
    
    st.write(f"Total Net Wealth in PKR: {net_wealth:.2f}")
    st.write(f"Nisab Threshold in PKR: {nisab:.2f}")
    if zakat > 0:
        st.write(f"Zakat Due in PKR: {zakat:.2f}")
    else:
        st.write("You are not liable to pay Zakat as your net wealth is below the Nisab threshold.")
    
    # Plotting the wealth distribution
    wealth_distribution = {
        'Category': ['Cash', 'Gold', 'Silver', 'Investments', 'Business Merchandise', 'Property', 'Receivables', 'Debts'],
        'Amount': [cash * exchange_rate, gold * exchange_rate, silver * exchange_rate, investments * exchange_rate, business_merchandise * exchange_rate, property * exchange_rate, receivables * exchange_rate, debts * exchange_rate]
    }
    
    fig = px.pie(wealth_distribution, values='Amount', names='Category', title='Wealth Distribution')
    st.plotly_chart(fig)
