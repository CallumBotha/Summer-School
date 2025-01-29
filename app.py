import streamlit as st
import pandas as pd

# Title of the app
st.title("Who is Callum? - Profile Page")

# Collect basic information
name = "Callum Botha"
field = "Bayesian Tolerance Intervals"
institution = "Nelson Mandela University"
linkedin = "https://www.linkedin.com/in/callum-botha/"

# Upload and display a profile image
st.header("Profile Picture")
uploaded_image = st.file_uploader("Upload your profile picture", type=["png", "jpg", "jpeg"])

if uploaded_image:
    st.image(uploaded_image, caption=f"{name}'s Profile Picture", use_column_width=False, width=200)

# Display basic profile information
st.header("Researcher Overview")
st.write(f"**Name:** {name}")
st.write(f"**Linkedin:** {linkedin}")
st.write(f"**Field of Research:** {field}")
st.write(f"**Institution:** {institution}")

# Add a section for publications
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")

if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)

    # Add filtering for year or keyword
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")

# Add a section for visualizing publication trends
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")

# Add a contact section
st.header("Contact Information")
email = "callum.botha@gmail.com"
st.write(f"You can reach {name} at {email}, or alternatively at {linkedin}")
