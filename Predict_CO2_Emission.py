
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import csv

# Placeholder function to simulate CO2 emission predictions
def predict_emissions(inputs, factors):
    """
    This function predicts CO2 emissions based on input parameters and emission factors.
    It simplistically multiplies input values by a factor of 10% more than the actual to simulate prediction.
    """
    prediction = 0
    for key, value in inputs.items():
        if key in factors:
            base_emission = factors[key] * float(value)
            prediction += base_emission * 1.1  # Predicted is 110% of actual for simulation
    return round(prediction, 2)

# Function to plot actual vs. predicted emissions
def plot_emissions(actual, predicted, category):
    """
    This function plots a line chart comparing actual and predicted CO2 emissions.
    """
    fig, ax = plt.subplots()
    index = ['Actual', 'Predicted']
    emissions = [actual, predicted]
    ax.bar(index, emissions, color=['blue', 'green'])
    ax.set_ylabel('Tonnes of CO2')
    ax.set_title(f'CO2 Emission Comparison for {category}')
    st.pyplot(fig)

# Main function to be called from the Streamlit app
def predict_CO2_emissions(EMISSION_FACTORS):
    """
    Main function to handle CO2 emission prediction and visualization.
    """
    st.title("Predict CO2 Emissions & Visualization")

    # Select a category
    selected_category = st.selectbox("Select a category for prediction", list(EMISSION_FACTORS.keys()))

    if st.button("Load Recent Emissions Data"):
        # Assuming data is stored in 'emission_data.csv' in the format defined in carbon_co2.py
        if os.path.exists("emission_data.csv"):
            df = pd.read_csv("emission_data.csv")
            df = df[df['Category'] == selected_category]  # Filter by selected category
            if not df.empty:
                last_record = df.iloc[-1]
                inputs = eval(last_record['Inputs'])
                actual_emissions = last_record['Total CO2 Emissions']
                predicted_emissions = predict_emissions(inputs, EMISSION_FACTORS[selected_category])

                # Display results
                st.write("### Emission Data")
                st.write(f"**Category:** {selected_category}")
                st.write(f"**Inputs:** {inputs}")
                st.write(f"**Actual Emissions:** {actual_emissions} tonnes CO2")
                st.write(f"**Predicted Emissions:** {predicted_emissions} tonnes CO2")

                # Plot results
                plot_emissions(actual_emissions, predicted_emissions, selected_category)
            else:
                st.error("No emission data found for the selected category. Please calculate emissions first.")
        else:
            st.error("Emission data file not found. Please calculate emissions to generate data.")