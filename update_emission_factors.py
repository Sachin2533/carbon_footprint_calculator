import streamlit as st

def update_emission_factors(EMISSION_FACTORS):
        st.title("Update Emission Factors")
        selected_category = st.selectbox("Select a category to update", list(EMISSION_FACTORS.keys()))

        if selected_category:
            st.write(f"Updating {selected_category} Emission Factors")

            if selected_category == "Transportation":
                update_transportation_emission_factors(EMISSION_FACTORS[selected_category])
            elif selected_category == "Electricity":
                update_electricity_emission_factors(EMISSION_FACTORS[selected_category])
            elif selected_category == "Diet":
                update_diet_emission_factors(EMISSION_FACTORS[selected_category])
            elif selected_category == "Industrial Processes":
                update_industrial_processes_emission_factors(EMISSION_FACTORS[selected_category])

def update_transportation_emission_factors(transportation_factors):
        st.subheader("Update Transportation Emission Factors")

        for key, value in transportation_factors.items():
            if isinstance(value, dict):
                st.write(f"Update {key} Emission Factors")
                for sub_key, sub_value in value.items():
                    new_value = st.number_input(f"Enter new value for {sub_key}", value=sub_value)
                    transportation_factors[key][sub_key] = new_value

        if st.button("Update transportation emission factors"):
            # Perform update here (you can store the transportation_factors dictionary wherever you're storing the emission factors)
            st.write("Emission factors updated successfully!")

def update_electricity_emission_factors(electricity_factors):
        st.subheader("Update Electricity Emission Factors")

        for key, value in electricity_factors.items():
            if isinstance(value, dict):
                st.write(f"Update {key} Emission Factors")
                for sub_key, sub_value in value.items():
                    new_value = st.number_input(f"Enter new value for {sub_key}", value=sub_value)
                    electricity_factors[key][sub_key] = new_value

        if st.button("Update electricity emission factors"):
            # Perform update here (you can store the electricity_factors dictionary wherever you're storing the emission factors)
            st.write("Emission factors updated successfully!")

def update_diet_emission_factors(diet_factors):
        st.subheader("Update Diet Emission Factors")

        for key, value in diet_factors.items():
            if isinstance(value, dict):
                st.write(f"Update {key} Emission Factors")
                for sub_key, sub_value in value.items():
                    new_value = st.number_input(f"Enter new value for {sub_key}", value=sub_value)
                    diet_factors[key][sub_key] = new_value

        if st.button("Update diet emission factors"):
            # Perform update here (you can store the diet_factors dictionary wherever you're storing the emission factors)
            st.write("Emission factors updated successfully!")

def update_industrial_processes_emission_factors(industrial_processes_factors):
        st.subheader("Update Industrial Processes Emission Factors")

        for key, value in industrial_processes_factors.items():
            if isinstance(value, dict):
                st.write(f"Update {key} Emission Factors")
                for sub_key, sub_value in value.items():
                    new_value = st.number_input(f"Enter new value for {sub_key}", value=sub_value)
                    industrial_processes_factors[key][sub_key] = new_value

        if st.button("Update industrial processes emission factors"):
            # Perform update here (you can store the industrial_processes_factors dictionary wherever you're storing the emission factors)
            st.write("Emission factors updated successfully!")

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

    # Run the app
if __name__ == "__main__":
    update_emission_factors(EMISSION_FACTORS)