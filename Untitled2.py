#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def combined_plot(M, A, P, E_P, E_C, E_M, e, LR_0, C):
    # Define range for n
    n_values = np.arange(1, 101)  # Calculate for n from 1 to 100
    
    # Market Growth Factor
    market_growth_factors = ((1 + M) / (1 + A)) ** n_values
    
    # Premium Growth Factor
    premium_growth_factors = (1 + P) ** n_values
    
    # Elasticity Factors
    elasticity_premium_factors = 1 + E_P * (1 / (1 + P) ** n_values - 1)
    elasticity_claims_factors = 1 + E_C * ((1 + C) ** n_values - 1)
    elasticity_market_factors = 1 + E_M * ((1 + M) ** n_values - 1)
    elasticity_combined_factors = elasticity_premium_factors * elasticity_claims_factors * elasticity_market_factors
    
    # Breakeven Factor
    constant_term = (1 - e)
    decay_term = LR_0 * ((1 + C) / (1 + P)) ** n_values
    breakeven_factors = constant_term - decay_term
    
    # Compute the terms of the cumulative sum
    term = market_growth_factors * premium_growth_factors * elasticity_combined_factors * breakeven_factors
    
    # Calculate the cumulative sum
    cumulative_sum = np.cumsum(term)
    
    # Plotting
    plt.figure(figsize=(14, 8))

    # Plot each factor with improved lines
    plt.plot(n_values, market_growth_factors, label='Market Growth Factor', color='yellow', linewidth=2)
    plt.plot(n_values, premium_growth_factors, label='Premium Growth Factor', color='cyan', linewidth=2)
    plt.plot(n_values, elasticity_combined_factors, label='Elasticity Combined Factor', color='green', linewidth=2)
    plt.plot(n_values, breakeven_factors, label='Breakeven Factor', color='pink', linewidth=2)

    # Plot the final cumulative sum with a dashed line
    plt.plot(n_values, cumulative_sum, label='Final Cumulative Sum of Profit Factor', linestyle='--', linewidth=2, color='black')

    # Improve legend placement
    plt.legend(loc='upper left', bbox_to_anchor=(1, 1))

    plt.xlabel('Time Period (n)')
    plt.ylabel('Factor Values / Cumulative Sum')
    plt.title('Combined Visualization of Factors and Final Cumulative Sum of Profit Factor')
    plt.grid(True)
    plt.show()

# Create interactive widgets
interactive_combined_plot = interactive(
    combined_plot,
    M=widgets.FloatSlider(min=0, max=0.1, step=0.01, value=0.03),
    A=widgets.FloatSlider(min=0, max=0.1, step=0.01, value=0.02),
    P=widgets.FloatSlider(min=0, max=0.1, step=0.01, value=0.01),
    E_P=widgets.FloatSlider(min=-1, max=1, step=0.1, value=1.00),
    E_C=widgets.FloatSlider(min=0, max=1, step=0.1, value=0.50),
    E_M=widgets.FloatSlider(min=0, max=1, step=0.1, value=0.10),
    e=widgets.FloatSlider(min=0, max=1, step=0.01, value=0.47),
    LR_0=widgets.FloatSlider(min=0, max=1, step=0.1, value=0.35),
    C=widgets.FloatSlider(min=0, max=0.1, step=0.01, value=0.02)
)

# Display the interactive plot
interactive_combined_plot


# In[ ]:




