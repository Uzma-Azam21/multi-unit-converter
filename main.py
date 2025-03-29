import streamlit as st

# Set page configuration
st.set_page_config(page_title="Multi Unit Converter", page_icon="🔄", layout="centered")

# Dynamic Colors & Descriptions for Selected Conversion Type
conversion_details = {
    "Length 📏": {"color": "#ff6f61", "description": "Convert between different length units like meters, inches, and miles."},
    "Weight ⚖️": {"color": "#ffb400", "description": "Convert weights like kilograms, pounds, and ounces."},
    "Temperature 🌡️": {"color": "#20c997", "description": "Convert temperatures between Celsius, Fahrenheit, and Kelvin."},
    "Volume 🧴": {"color": "#6f42c1", "description": "Convert volume measurements like liters, gallons, and cups."},
    "Time ⏰": {"color": "#17a2b8", "description": "Convert time units like seconds, minutes, and hours."}
}

# Main Title
st.markdown("<h1 style='text-align:center; color:#4a90e2; font-size:2.2rem;'>🔄 <b>Multi Unit Converter</b></h1>", unsafe_allow_html=True)

# Subtitle
st.markdown("<div style='text-align:center; font-size:1.2rem; font-weight:bold;'>Easily convert between different units with accuracy!</div>", unsafe_allow_html=True)

# Sidebar for Conversion Selection
with st.sidebar:
    st.markdown("<b>📢 Select Conversion Type</b>", unsafe_allow_html=True)
    selected_type = st.radio("Choose Conversion Type", list(conversion_details.keys()), index=0)

# Apply Dynamic Heading Color & Description
selected_color = conversion_details[selected_type]["color"]
description = conversion_details[selected_type]["description"]

st.markdown(f"<h2 style='text-align:center; color:{selected_color}; font-size:1.8rem;'>{selected_type}</h2>", unsafe_allow_html=True)
st.markdown(f"<p style='text-align:center; color:#333; font-size:1rem; font-weight:bold;'>{description}</p>", unsafe_allow_html=True)

# Conversion Factors Dictionary
conversion_factors = {
    "Length": {
        "meter": 1, "kilometer": 1000, "centimeter": 0.01, "millimeter": 0.001,
        "inch": 0.0254, "foot": 0.3048, "yard": 0.9144, "mile": 1609.34
    },
    "Weight": {
        "gram": 1, "kilogram": 1000, "milligram": 0.001,
        "ounce": 28.3495, "pound": 453.592, "ton": 1000000
    },
    "Volume": {
        "liter": 1, "milliliter": 0.001, "gallon": 3.78541,
        "quart": 0.946353, "pint": 0.473176, "cup": 0.24, "fluid_ounce": 0.0295735
    },
    "Time": {
        "second": 1, "minute": 60, "hour": 3600,
        "day": 86400, "week": 604800, "month": 2.628e+6, "year": 3.154e+7
    }
}

# Function for General Unit Conversion (Except Temperature)
def convert_units(value, from_unit, to_unit, category):
    if from_unit == to_unit:
        return value, f"{value} {from_unit} is the same as {value} {to_unit}."

    factor_from = conversion_factors[category][from_unit]
    factor_to = conversion_factors[category][to_unit]
    
    result = (value * factor_from) / factor_to
    formula = f"{value} × ({factor_from} ÷ {factor_to}) = {result:.2f} {to_unit}"

    return result, f"<b>Formula Used:</b> {formula}"

# Function for Temperature Conversion
def convert_temperature(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value, f"{value} {from_unit} is the same as {value} {to_unit}."

    formulas = {
        ("celsius", "fahrenheit"): f"({value} × 9/5) + 32",
        ("celsius", "kelvin"): f"{value} + 273.15",
        ("fahrenheit", "celsius"): f"({value} - 32) × 5/9",
        ("fahrenheit", "kelvin"): f"(({value} - 32) × 5/9) + 273.15",
        ("kelvin", "celsius"): f"{value} - 273.15",
        ("kelvin", "fahrenheit"): f"(({value} - 273.15) × 9/5) + 32"
    }

    conversions = {
        "celsius": {"fahrenheit": (value * 9/5) + 32, "kelvin": value + 273.15},
        "fahrenheit": {"celsius": (value - 32) * 5/9, "kelvin": ((value - 32) * 5/9) + 273.15},
        "kelvin": {"celsius": value - 273.15, "fahrenheit": ((value - 273.15) * 9/5) + 32}
    }

    result = conversions[from_unit][to_unit]
    return result, f"<b>Formula Used:</b> {formulas[(from_unit, to_unit)]} = {result:.2f} {to_unit}"

# User Input Section
st.markdown("""
<style>
    /* Reduce default Streamlit spacing */
    div[data-testid="column"] {
        gap: 0.2rem !important;
    }
    div.stNumberInput, div.stSelectbox {
        margin-top: -0.8rem !important;
    }
    /* Fine-tune label spacing */
    .stMarkdown {
        margin-bottom: -0.5rem !important;
    }
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("<b style='font-size:0.95rem'>📥 Enter Value</b>", unsafe_allow_html=True)
    value = st.number_input(" ", format="%.2f", key="value_input", label_visibility="collapsed")

with col2:
    units = {
        "Length": ['meter', 'kilometer', 'centimeter', 'millimeter', 'inch', 'foot', 'yard', 'mile'],
        "Weight": ['gram', 'kilogram', 'milligram', 'ounce', 'pound', 'ton'],
        "Temperature": ['celsius', 'fahrenheit', 'kelvin'],
        "Volume": ['liter', 'milliliter', 'gallon', 'quart', 'pint', 'cup', 'fluid_ounce'],
        "Time": ['second', 'minute', 'hour', 'day', 'week', 'month', 'year']
    }
    
    st.markdown("<b style='font-size:0.95rem; margin-bottom:0'>🔹 From Unit</b>", unsafe_allow_html=True)
    from_unit = st.selectbox(" ", units[selected_type.split(" ")[0]], key="from_unit", label_visibility="collapsed")

    st.markdown("<div style='margin-top:-15px;'></div>", unsafe_allow_html=True)

    st.markdown("<b style='font-size:0.95rem; margin-top:0'>🔹 To Unit</b>", unsafe_allow_html=True)
    to_unit = st.selectbox(" ", units[selected_type.split(" ")[0]], key="to_unit", label_visibility="collapsed")
# Convert Button
st.markdown(
    "<style>.stButton>button {background-color: #007BFF !important; color: white !important; font-weight: bold;}</style>", 
    unsafe_allow_html=True
)
if st.button("🚀 Convert", use_container_width=True):
    category = selected_type.split(" ")[0]  
    
    if category == "Temperature":
        result, formula = convert_temperature(value, from_unit, to_unit)
    else:
        result, formula = convert_units(value, from_unit, to_unit, category)

    st.markdown(f"<div style='background-color:#e3f2fd; padding:15px; border-radius:5px; text-align:center; font-size:1.2rem;'><b>Result:</b> {result:.2f} {to_unit}</div>", unsafe_allow_html=True)
    st.markdown(f"<div style='background-color:#d1ecf1; padding:15px; border-radius:5px; text-align:center; font-size:1.1rem;'>{formula}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<div style='text-align:center; font-size:1rem; font-weight:bold; margin-top:100px;'>© <span style='color:#ff6f61;'>Multi Unit Converter by Uzma Azam</span>. All Rights Reserved.</div>", unsafe_allow_html=True)






