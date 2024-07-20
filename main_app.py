# main_app.py

# main_app.py

import streamlit as st
import carbon_co2
import login_app
import csv
import update_emission_factors
import Predict_CO2_Emission
import pandas as pd  


# Function to load data from a CSV file
def load_data_from_csv(file_name):
    data = []
    with open(file_name, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            data.append(row)
    return data

# Function to display the dashboard page
def dashboard_page(EMISSION_FACTORS):
    st.title("Dashboard")
    username = st.session_state.username
    st.write(f"Welcome {username}!")

    # Admin privileges
    if username == "admin":
        st.write("You have admin privileges.")
        option = st.selectbox("Select an option", ["Calculate CO2 Emission", "Update Emission Factors", "Predict CO2 Emission & Visualization Report"])

        if option == "Calculate CO2 Emission":
            st.write("Calculating CO2 emission...")
            carbon_co2.calculate_emission(EMISSION_FACTORS)
        elif option == "Update Emission Factors":
            st.write("Updating emission factors...")
            update_emission_factors.update_emission_factors(EMISSION_FACTORS)
        elif option == "Predict CO2 Emission & Visualization Report":
            st.write("Predicting CO2 emission and displaying visualization report...")
            Predict_CO2_Emission.predict_CO2_emissions(EMISSION_FACTORS)  # Call to predict_page function
    
    # User privileges
    else:
        st.write("You have user privileges.")
        option = st.selectbox("Select an option", ["Calculate CO2 Emission", "Predict CO2 Emission & Visualization Report"])

        if option == "Calculate CO2 Emission":
            st.write("Calculating CO2 emission...")
            carbon_co2.calculate_emission(EMISSION_FACTORS)
        elif option == "Predict CO2 Emission & Visualization Report":
            st.write("Predicting CO2 emission and displaying visualization report...")
            Predict_CO2_Emission.predict_CO2_emissions(EMISSION_FACTORS)  # Call to predict_page function

# Main function
def main():
    if not hasattr(st.session_state, "logged_in"):
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        login_app.login_page()
    else:
        # Define emission factors
        EMISSION_FACTORS = {
            "Transportation": {
                "distance": 0.14,
                "fuel_efficiency": 0.05,
                "vehicle_types": {
                    "Car": 0.12,
                    "Van": 0.15,
                    "Bus": 0.2,
                    "Bicycle": 0.0
                },
                "fuel_types": {
                    "Gasoline": 2.31,
                    "Diesel": 2.66,
                    "Electric": 0.0
                }
            },
            "Electricity": {
                "consumption": 0.82,
                "energy_sources": {
                    "Coal": 1.5,
                    "Natural Gas": 0.8,
                    "Renewables": 0.0
                }
            },
            "Diet": {
                "meals_per_day": 3,
                "food_types": {
                    "Meat": 5.0,
                    "Vegetarian": 2.0,
                    "Vegan": 1.5
                }
            },
            "Industrial Processes": {
                "quantity_of_materials_used": 100,
                "industry_types": {
                    "Manufacturing": 1.5,
                    "Textile": 2.0,
                    "Chemical": 2.5
                },
                "production_processes": {
                    "Casting": 0.5,
                    "Machining": 0.3,
                    "Chemical Processing": 0.
                }
            }
        }
        dashboard_page(EMISSION_FACTORS)

if __name__ == "__main__":
    main()
