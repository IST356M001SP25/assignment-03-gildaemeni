'''
Next, write a streamlit to read ONE file of packaging information. 
You should output the parsed package and total package size for each package in the file.

Screenshot available as process_file.png
'''
import streamlit as st
import json
from packaging import parse_packaging, calc_total_units, get_unit

st.title("Process File of Packages")

uploaded_file = st.file_uploader("Upload a package file", type=["txt"])

if uploaded_file:
    filename = uploaded_file.name
    json_filename = filename.replace(".txt", ".json")
    text = uploaded_file.read().decode("utf-8")
    lines = text.split("\n")

    packages = []
    
    for line in lines:
        line = line.strip()
        if line:
            parsed_pkg = parse_packaging(line)
            total = calc_total_units(parsed_pkg)
            unit = get_unit(parsed_pkg)

            packages.append(parsed_pkg)
            st.info(f"{line} ➡️ Total 📦 Size: {total} {unit}")

    with open(f"./data/{json_filename}", "w") as f:
        json.dump(packages, f, indent=4)

    st.success(f"💾 {len(packages)} packages written to {json_filename}")