import streamlit as st
import csv

def calculate_emission(EMISSION_FACTORS):
    st.title("Calculate CO2 Emission")
    selected_category = st.sidebar.selectbox("Select a category", list(EMISSION_FACTORS.keys()))

    if selected_category:
        st.subheader(f"Input Parameters for {selected_category}")
        inputs = {}
        if selected_category == "Transportation":
            inputs["distance"] = st.slider("Distance Traveled (km)", 0.0, 100.0, 0.0)
            inputs["fuel_efficiency"] = st.slider("Fuel Efficiency (km per liter or kWh)", 0.0, 10.0, 0.0)
            inputs["vehicle_type"] = st.selectbox("Type of Vehicle", list(EMISSION_FACTORS["Transportation"]["vehicle_types"].keys()))
            inputs["fuel_type"] = st.selectbox("Fuel Type", list(EMISSION_FACTORS["Transportation"]["fuel_types"].keys()))
        elif selected_category == "Electricity":
            inputs["consumption"] = st.slider("Electricity Consumption (kWh)", 0.0, 1000.0, 0.0)
            inputs["energy_source"] = st.selectbox("Energy Source", list(EMISSION_FACTORS["Electricity"]["energy_sources"].keys()))
        elif selected_category == "Diet":
            inputs["meals_per_day"] = st.slider("Number of Meals per Day", 0, 10, 0)
            inputs["diet_composition"] = st.selectbox("Composition of Diet", ["Balanced", "High Protein", "Low Carb", "Vegetarian", "Vegan"])
            inputs["food_type"] = st.selectbox("Type of Food Consumed", list(EMISSION_FACTORS["Diet"]["food_types"].keys()))
        elif selected_category == "Industrial Processes":
            if "industry_types" in EMISSION_FACTORS["Industrial Processes"]:
                inputs["quantity_of_materials_used"] = st.slider("Quantity of Materials Used (kg)", 0.0, 100.0, 0.0)
                inputs["industry_type"] = st.selectbox("Type of Industry", list(EMISSION_FACTORS["Industrial Processes"]["industry_types"].keys()))
                inputs["production_process"] = st.selectbox("Production Process", list(EMISSION_FACTORS["Industrial Processes"]["production_processes"].keys()))
            else:
                st.error("Invalid emission factors for industrial processes.")
                return

        # Button for calculating CO2 emissions
        if st.button("Calculate CO2 Emissions", key=f"calculation_{selected_category}"):
            total_emissions = 0
            emissions = EMISSION_FACTORS[selected_category]
            for key, value in inputs.items():
                if key in emissions:
                    if selected_category == "Diet" and key == "diet_composition":
                        total_emissions += emissions["food_types"][inputs["food_type"]] * inputs["meals_per_day"]
                    else:
                        total_emissions += emissions[key] * float(value)
            total_emissions = round(total_emissions, 2)
            st.header("Results")
            st.subheader(f"Carbon Emissions for {selected_category}")
            st.info(f"Total CO2 Emissions: {total_emissions} tonnes CO2 per year")

            # Save data to CSV file
            with open("emission_data.csv", "a", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["Category", "Inputs", "Total CO2 Emissions"])
                if f.tell() == 0:
                    writer.writeheader()
                writer.writerow({"Category": selected_category, "Inputs": inputs, "Total CO2 Emissions": total_emissions})

            # Return the data calculated during CO2 emission calculation
            return {"Category": selected_category, "Inputs": inputs, "Total CO2 Emissions": total_emissions}

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
