'''
In this final program, you will re-write your `process_file.py` 
to keep track of the number of files and total number of lines 
that have been processed.

For each file you read, you only need to output the 
summary information eg. "X packages written to file.json".

Screenshot available as process_files.png
'''
import streamlit as st
import json
from packaging import parse_packaging, calc_total_units, get_unit

# Initialize session state variables if they don't exist
if 'summaries' not in st.session_state:
    st.session_state.summaries = []
if 'total_lines' not in st.session_state:
    st.session_state.total_lines = 0
if 'total_files' not in st.session_state:
    st.session_state.total_files = 0

st.title("Process Package Files")

# url
uploaded_file = st.file_uploader("Upload package file", type=["txt"])

if uploaded_file:
    # Get the file name and create a JSON file name
    filename = uploaded_file.name
    json_filename = filename.replace(".txt", ".json")

    # Read the file content directly
    file_contents = uploaded_file.read().decode("utf-8")
    lines = file_contents.splitlines()  # Split the file into lines

    packages = []

    for line in lines:
        line = line.strip()
        if line:  # Skip empty lines
            # Parse package information
            parsed_pkg = parse_packaging(line)
            total_units = calc_total_units(parsed_pkg)
            unit = get_unit(parsed_pkg)

            # Append parsed package info
            packages.append(parsed_pkg)

    # Write the parsed packages to a JSON file
    with open(f"./data/{json_filename}", "w") as json_file:
        json.dump(packages, json_file, indent=4)

    # Update session state
    count = len(packages)
    st.session_state.summaries.append(f"{count} packages written to {json_filename}")
    st.session_state.total_files += 1
    st.session_state.total_lines += count

    # Display summaries of processed files
    for summary in st.session_state.summaries:
        st.info(summary, icon="💾")

    # Show final summary of all processed files
    st.success(f"{st.session_state.total_files} files processed, {st.session_state.total_lines} total lines processed")