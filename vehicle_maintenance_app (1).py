
import streamlit as st

def get_maintenance_recommendations(mileage, years):
    recommendations = []

    if mileage >= 8000 or years >= 0.5:
        recommendations.append("- Engine oil & filter change")
        recommendations.append("- Check tire pressure & tread")
        recommendations.append("- Inspect fluid levels")
        recommendations.append("- Inspect lights, wipers, and battery")

    if mileage >= 20000 or years >= 1:
        recommendations.append("- Rotate tires")
        recommendations.append("- Inspect brake pads and rotors")
        recommendations.append("- Replace cabin air filter")
        recommendations.append("- Inspect suspension and steering")

    if mileage >= 40000 or years >= 2:
        recommendations.append("- Replace engine air filter")
        recommendations.append("- Inspect spark plugs")
        recommendations.append("- Brake fluid flush")
        recommendations.append("- Inspect belts and hoses")

    if mileage >= 80000 or years >= 4:
        recommendations.append("- Replace spark plugs")
        recommendations.append("- Transmission fluid service")
        recommendations.append("- Inspect cooling system")

    if mileage >= 160000 or years >= 6:
        recommendations.append("- Replace timing belt")
        recommendations.append("- Replace coolant")
        recommendations.append("- Replace transmission fluid")
        recommendations.append("- Comprehensive inspection")

    return recommendations

st.title("Vehicle Maintenance Recommendation Tool")

mileage = st.number_input("Enter vehicle mileage (in km):", min_value=0)
years = st.number_input("Enter vehicle age (in years):", min_value=0.0, step=0.1)

if st.button("Get Recommendations"):
    results = get_maintenance_recommendations(mileage, years)
    st.subheader("Recommended Maintenance:")
    for item in results:
        st.write(item)
