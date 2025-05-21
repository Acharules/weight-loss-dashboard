import streamlit as st
import pandas as pd
from datetime import datetime, timedelta

st.set_page_config(page_title="Daily Weight Loss Dashboard", layout="wide")

st.title("💪 Daily Weight Loss Success Tracker")

# Initialize or load the checklist
if "checklist" not in st.session_state:
    weeks = 4
    days_per_week = 7
    plan = []
    for week in range(1, weeks + 1):
        for day in range(1, days_per_week + 1):
            date = datetime.today() + timedelta(days=(week - 1) * 7 + (day - 1))
            plan.append({
                "Date": date.strftime("%Y-%m-%d"),
                "Day": f"Week {week} - Day {day}",
                "✅ 1,000 Skips Done": False,
                "✅ Max 1 Biscuit at Tea": False,
                "✅ No Food After 8pm": False,
                "✅ Smaller Portion at One Meal": False,
                "🧠 Notes / How I Felt": ""
            })
    st.session_state.checklist = plan

# Display checklist
for i, entry in enumerate(st.session_state.checklist):
    with st.expander(f"{entry['Day']} ({entry['Date']})"):
        col1, col2 = st.columns(2)
        entry["✅ 1,000 Skips Done"] = col1.checkbox("✅ 1,000 Skips Done", value=entry["✅ 1,000 Skips Done"], key=f"skip_{i}")
        entry["✅ Max 1 Biscuit at Tea"] = col2.checkbox("✅ Max 1 Biscuit at Tea", value=entry["✅ Max 1 Biscuit at Tea"], key=f"biscuit_{i}")
        entry["✅ No Food After 8pm"] = col1.checkbox("✅ No Food After 8pm", value=entry["✅ No Food After 8pm"], key=f"nofood_{i}")
        entry["✅ Smaller Portion at One Meal"] = col2.checkbox("✅ Smaller Portion at One Meal", value=entry["✅ Smaller Portion at One Meal"], key=f"portion_{i}")
        entry["🧠 Notes / How I Felt"] = st.text_area("🧠 Notes / How I Felt", value=entry["🧠 Notes / How I Felt"], key=f"notes_{i}")

# Show completion stats
completed = sum(
    1 for entry in st.session_state.checklist
    if all([
        entry["✅ 1,000 Skips Done"],
        entry["✅ Max 1 Biscuit at Tea"],
        entry["✅ No Food After 8pm"],
        entry["✅ Smaller Portion at One Meal"]
    ])
)
st.success(f"✅ {completed} fully completed days out of {len(st.session_state.checklist)}!")
