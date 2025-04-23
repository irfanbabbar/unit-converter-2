import streamlit as st

# App title and description
st.title("📏 Unit Converter")
st.write("Convert between different units of length, weight, temperature, and volume.")

# Define conversion functions
def convert_length(value, from_unit, to_unit):
    # Conversion logic for length
    length_conversions = {
        "meters": 1,
        "kilometers": 1000,
        "centimeters": 0.01,
        "millimeters": 0.001,
        "miles": 1609.34,
        "feet": 0.3048,
        "inches": 0.0254,
    }
    return value * length_conversions[from_unit] / length_conversions[to_unit]

def convert_weight(value, from_unit, to_unit):
    # Conversion logic for weight
    weight_conversions = {
        "kilograms": 1,
        "grams": 0.001,
        "milligrams": 0.000001,
        "pounds": 0.453592,
        "ounces": 0.0283495,
    }
    return value * weight_conversions[from_unit] / weight_conversions[to_unit]

def convert_temperature(value, from_unit, to_unit):
    # Conversion logic for temperature
    if from_unit == "Celsius":
        if to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif to_unit == "Kelvin":
            return value + 273.15
        else:
            return value
    elif from_unit == "Fahrenheit":
        if to_unit == "Celsius":
            return (value - 32) * 5/9
        elif to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        else:
            return value
    elif from_unit == "Kelvin":
        if to_unit == "Celsius":
            return value - 273.15
        elif to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value

def convert_volume(value, from_unit, to_unit):
    # Conversion logic for volume
    volume_conversions = {
        "liters": 1,
        "milliliters": 0.001,
        "gallons": 3.78541,
        "cubic meters": 1000,
    }
    return value * volume_conversions[from_unit] / volume_conversions[to_unit]

# Sidebar for selecting conversion type
conversion_type = st.sidebar.selectbox(
    "Select Conversion Type",
    ["Length", "Weight", "Temperature", "Volume"]
)

# Main conversion logic
if conversion_type == "Length":
    units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "feet", "inches"]
elif conversion_type == "Weight":
    units = ["kilograms", "grams", "milligrams", "pounds", "ounces"]
elif conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
elif conversion_type == "Volume":
    units = ["liters", "milliliters", "gallons", "cubic meters"]

# Input fields
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox("From", units)
with col2:
    to_unit = st.selectbox("To", units)

value = st.number_input("Enter value", min_value=0.0, format="%.2f")

# Perform conversion
if st.button("Convert"):
    if conversion_type == "Length":
        result = convert_length(value, from_unit, to_unit)
    elif conversion_type == "Weight":
        result = convert_weight(value, from_unit, to_unit)
    elif conversion_type == "Temperature":
        result = convert_temperature(value, from_unit, to_unit)
    elif conversion_type == "Volume":
        result = convert_volume(value, from_unit, to_unit)

    st.success(f"**Result:** {value} {from_unit} = {result:.2f} {to_unit}")

# Footer
st.markdown("---")
st.caption("Made with ❤️ using Streamlit")