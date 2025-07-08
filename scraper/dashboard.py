import streamlit as st
import pandas as pd
import altair as alt
import os

# Load data
df = pd.read_csv("data/skill_trends.csv")

st.set_page_config(page_title="AI Job Skills Dashboard", layout="centered")
st.title("📊 AI Job Skills Dashboard")
st.subheader("Top Skills Extracted from Naukri Job Postings")

# 🔍 Search filter
search_term = st.text_input("🔍 Filter skills (optional):").lower()

# 📅 Optional date range filter if 'Date' column exists
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    min_date, max_date = df["Date"].min(), df["Date"].max()
    date_range = st.slider("📅 Select Date Range", min_value=min_date, max_value=max_date, value=(min_date, max_date))
    df = df[(df["Date"] >= date_range[0]) & (df["Date"] <= date_range[1])]

# 🔎 Apply skill filter
if search_term:
    filtered_df = df[df["Skill"].str.lower().str.contains(search_term)]
else:
    filtered_df = df

# 📊 Bar chart of top 20 skills
top_skills = filtered_df.groupby("Skill")["Count"].sum().reset_index()
top_skills = top_skills.sort_values("Count", ascending=False).head(20)

bar_chart = alt.Chart(top_skills).mark_bar().encode(
    x=alt.X("Skill", sort="-y"),
    y="Count",
    tooltip=["Skill", "Count"]
).properties(
    width=700,
    height=400,
    title="Top 20 Most Demanded Skills"
)

st.altair_chart(bar_chart, use_container_width=True)

# 📈 Line chart for trends over time (if date exists)
if "Date" in df.columns and search_term:
    trend_df = filtered_df.groupby(["Date", "Skill"])["Count"].sum().reset_index()
    line_chart = alt.Chart(trend_df).mark_line(point=True).encode(
        x="Date:T",
        y="Count:Q",
        color="Skill:N",
        tooltip=["Date", "Skill", "Count"]
    ).properties(
        width=700,
        height=400,
        title="Skill Trend Over Time"
    )
    st.altair_chart(line_chart, use_container_width=True)

# 📋 Full table
with st.expander("📋 View full data table"):
    st.dataframe(filtered_df.reset_index(drop=True))

st.markdown("---")
st.caption("Built by Sakshya Sinha 🔥 using Streamlit + Selenium")
