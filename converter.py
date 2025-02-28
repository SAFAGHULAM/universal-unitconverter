import streamlit as st
from forex_python.converter import CurrencyRates
import requests
import pandas as pd

st.title("Universal Unit Converter🌎")
st.write("A universal unit converter for various units like Length, Width, Temperature, Currency, Speed, Time and more!")

result = None 

conversion_type = st.selectbox("Select the type of conversion", ["Length", "Weight", "Temperature", "Currency", "Speed", "Time", "Area", "Volume", "Energy", "Pressure", "Data Storage"])

def store_history(value, from_unit, to_unit, result, conversion_type):
    """Stores each conversion in session history."""
    st.session_state["history"].append({
        "Type": conversion_type,
        "From": f"{value} {from_unit}",
        "To": f"{result} {to_unit}"
    })

def length_conversion(value, from_unit, to_unit):
    conversion_factors={
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])


if conversion_type == "Length":
    units = ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = length_conversion(value, from_unit, to_unit)


def weight_conversion(value, from_unit, to_unit):
    conversion_factors={
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1000000,
        "pounds": 2.20462,
        "ounces": 35.274
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

if conversion_type == "Weight":
    units = ["kilograms", "grams", "milligrams", "pounds", "ounces"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = weight_conversion(value, from_unit, to_unit)
        
def temperature_conversion(value, from_unit, to_unit):
    if from_unit == "Celsius":
       return value * 9/5 +32 if to_unit == "Fahrenheit" else value + 273.15
    elif from_unit == "Fahrenheit":
       return (value - 32) * 5/9 if to_unit == "Celsius" else (value - 32) * 5/9 + 273.15
    elif from_unit == "Kelvin":
        return value - 273.15 if to_unit == "Celsius" else (value - 273.15) * 9/5 + 32
    return value
    
if conversion_type == "Temperature":
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = temperature_conversion(value, from_unit, to_unit)

API_KEY = "2f71e7a15a-91fc2d2cd7-sse9db"
        
def currency_conversion(value, from_unit, to_unit):
    url = f"https://api.fastforex.io/fetch-one?from={from_unit}&to={to_unit}&api_key={API_KEY}"
    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and "result" in data:
        rate = data["result"].get(to_unit)
        return value * rate if rate else None
    return None
    
if conversion_type == "Currency":
    currency_units = ["USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD"]
    from_unit = st.selectbox("From", currency_units)
    to_unit = st.selectbox("To", currency_units)
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = currency_conversion(value, from_unit, to_unit)
        
def speed_conversion(value, from_unit, to_unit):
    conversion_factors={
        "m/s": 1,
        "km/h": 3.6,
        "mph": 2.23694,
        "fps": 3.28084,
        "knots": 1.94384
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

if conversion_type == "Speed":
    units = ["m/s", "km/h", "mph", "fps", "knots"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = speed_conversion(value, from_unit, to_unit)
        
def time_conversion(value, from_unit, to_unit):
    conversion_factors={
        "seconds": 1,
        "minutes": 1/60,
        "hours": 1/3600,
        "days": 1/86400,
        "weeks": 1/604800,
        "months": 1/2628000,
        "years": 1/31540000
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

if conversion_type == "Time":
    units = ["seconds", "minutes", "hours", "days", "weeks", "months", "years"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = time_conversion(value, from_unit, to_unit)
        
def area_conversion(value, from_unit, to_unit):
    conversion_factors={
        "square meters": 1,
        "square kilometers": 0.000001,
        "square centimeters": 10000,
        "square millimeters": 1000000,
        "square feet": 10.7639,
        "square yards": 1.19599,
        "acres": 0.000247105,
        "hectares": 0.0001
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

if conversion_type == "Area":
    units = ["square meters", "square kilometers", "square centimeters", "square millimeters", "square feet", "square yards", "acres", "hectares"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = area_conversion(value, from_unit, to_unit)

def volume_conversion(value, from_unit, to_unit):
    conversion_factors={
        "cubic meters": 1,
        "cubic kilometers": 0.000000000001,
        "liters": 1000,
        "milliliters": 1000000,
        "cubic feet": 35.3147,
        "cubic inches": 61023.7,
        "gallons": 264.172,
        "quarts": 1056.69
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

if conversion_type == "Volume":
    units = ["cubic meters", "cubic kilometers", "liters", "milliliters", "cubic feet", "cubic inches", "gallons", "quarts"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = volume_conversion(value, from_unit, to_unit)
        
def energy_conversion(value, from_unit, to_unit):
    conversion_factors={
        "joules": 1,
        "kilojoules": 0.001,
        "calories": 0.239006,
        "kilocalories": 0.000239006,
        "watt-hours": 0.000277778,
        "kilowatt-hours": 0.000000277778,
        "electronvolts": 6241506480000000000
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])

if conversion_type == "Energy":
    units = ["joules", "kilojoules", "calories", "kilocalories", "watt-hours", "kilowatt-hours", "electronvolts"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = energy_conversion(value, from_unit, to_unit)
        
def pressure_conversion(value, from_unit, to_unit):
    conversion_factors={
        "pascals": 1,
        "kilopascals": 0.001,
        "megapascals": 0.000001,
        "bars": 0.00001,
        "atmospheres": 0.00000986923,
        "mmHg": 0.00750062,
        "psi": 0.000145038
    }
    return value * (conversion_factors[to_unit] / conversion_factors[from_unit])
    
if conversion_type == "Pressure":
    units = ["pascals", "kilopascals", "megapascals", "bars", "atmospheres", "mmHg", "psi"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = pressure_conversion(value, from_unit, to_unit)
        
def data_storage_conversion(value, from_unit, to_unit):
    conversion_factor={
        "bits": 1,
        "bytes": 0.125,
        "kilobits": 0.001,
        "kilobytes": 0.000125,
        "megabits": 0.000001,
        "megabytes": 0.000000125,
        "gigabits": 0.000000001,
        "gigabytes": 0.000000000125,
        "terabits": 0.000000000001,
        "terabytes": 0.000000000000125
    }
    return value * (conversion_factor[to_unit] / conversion_factor[from_unit])

if conversion_type == "Data Storage":
    units = ["bits", "bytes", "kilobits", "kilobytes", "megabits", "megabytes", "gigabits", "gigabytes", "terabits", "terabytes"]
    from_unit = st.selectbox("From", units)
    to_unit = st.selectbox("To", units)
    value = st.number_input("Enter value", min_value=0.0)
    if st.button("Convert"):
        result = data_storage_conversion(value, from_unit, to_unit)

# Ensure the session state for history exists
if "history" not in st.session_state:
    st.session_state["history"] = []

if result is not None:
    st.success(f"Converted Value = {result}")

    # Store conversion history in session state
    st.session_state["history"].append({
        "Value": value,
        "From": from_unit,
        "To": to_unit,
        "Result": result,
        "Type": conversion_type
    })

# Display Conversion History
st.subheader("📜 Conversion History")
if st.session_state["history"]:
    st.table(st.session_state["history"])
else:
    st.write("No conversions yet.")