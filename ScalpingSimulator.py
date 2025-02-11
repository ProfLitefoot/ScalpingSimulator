import random
import time
import streamlit as st
import matplotlib.pyplot as plt

# Initialize market variables
current_price = 2.06
prices = [current_price]
tick_size = 0.02
back_bet = None
lay_bet = None
wom = round(random.uniform(0.3, 0.7), 2)

# Function to simulate market movement
def simulate_market():
    global current_price, prices, wom
    current_price += random.choice([-1, 1]) * tick_size
    current_price = round(current_price, 2)
    prices.append(current_price)
    wom = round(random.uniform(0.3, 0.7), 2)

# Streamlit UI setup
st.title("Pre-Match Scalping Simulator")
st.sidebar.header("Trade Controls")

# Display current price and WoM
st.subheader(f"Current Price: {current_price}")
st.subheader(f"Weight of Money (WoM): {wom:.2f}")

# Buttons for user actions
if st.sidebar.button("Place Back Bet"):
    back_bet = current_price
    st.sidebar.write(f"Back bet placed at {back_bet}")

if back_bet is not None:
    if st.sidebar.button("Place Lay Bet"):
        lay_bet = current_price
        profit = (back_bet - lay_bet) / tick_size
        st.sidebar.write(f"Trade closed! Profit: {profit:.2f} ticks")
        back_bet = None
        lay_bet = None
    
    if st.sidebar.button("Exit Trade"):
        loss = (current_price - back_bet) / tick_size
        st.sidebar.write(f"Trade exited at loss: {loss:.2f} ticks")
        back_bet = None
        lay_bet = None

# Simulate market movement every iteration
simulate_market()

# Plot the price movement
fig, ax = plt.subplots()
ax.plot(prices, label="Price Movement")
ax.legend()
st.pyplot(fig)

# Refresh the page periodically to simulate real-time updates
time.sleep(1)
st.rerun()
