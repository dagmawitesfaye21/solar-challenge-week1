# app/main.py
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Function to load data
@st.cache
def load_data():
    benin_df = pd.read_csv('../data/benin_clean.csv')  # Adjust the path as needed
    sierraleone_df = pd.read_csv('../data/sierraleone_clean.csv')  # Adjust the path as needed
    togo_df = pd.read_csv('../data/togo_clean.csv')  # Adjust the path as needed
    return benin_df, sierraleone_df, togo_df

# Main function to run the app
def main():
    st.title("Solar Data Insights Dashboard")
    
    # Load data
    benin_df, sierraleone_df, togo_df = load_data()
    
    # Country selection
    country_options = ['Benin', 'Sierra Leone', 'Togo']
    selected_country = st.selectbox("Select a Country", country_options)

    # Displaying selected country data
    if selected_country == 'Benin':
        df = benin_df
    elif selected_country == 'Sierra Leone':
        df = sierraleone_df
    else:
        df = togo_df

    st.write(f"Data for {selected_country}")
    st.dataframe(df)

    # Display column names for debugging
    st.write("Available columns:", df.columns)

    # Boxplot of GHI
    st.subheader('GHI Boxplot')
    plt.figure(figsize=(10, 5))
    sns.boxplot(data=df, y='GHI')
    plt.title(f'GHI Distribution in {selected_country}')
    st.pyplot(plt)

    # Check if 'Region' column exists before using it
    if 'Region' in df.columns:
        # Top regions table
        st.subheader('Top Regions by GHI')
        top_regions = df[['Region', 'GHI']].sort_values(by='GHI', ascending=False).head(10)
        st.table(top_regions)
    else:
        st.warning("Region column not found in the dataset.")

if __name__ == "__main__":
    main()