'''
Write a streamlit to input one string of package data. 
It should use the `packaging.py` module to parse the string 
and output the package info as it appears. 
Calculate the total package size and display that.

see one_package.png for a screenshot
'''
import streamlit as st
from packaging import parse_packaging, calc_total_units, get_unit

st.title("Process One Package")

package_data = st.text_input("Enter package data:")

if package_data:
    # Process the input
    parsed_package = parse_packaging(package_data)
    total_units = calc_total_units(parsed_package)
    unit = get_unit(parsed_package)

    # Display raw parsed data
    st.text(str(parsed_package))  

    for index, item in enumerate(parsed_package):
        key, value = item.popitem() 
        st.info(f"{key} ➡️ {value}")

    # Display total size
    st.success(f"Total 📦 Size: {total_units} {unit}")
