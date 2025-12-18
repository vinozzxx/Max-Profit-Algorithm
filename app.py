

import streamlit as st
import pandas as pd

# Building configuration
BUILDINGS = {
    "T": {"name": "Theatre", "time": 5, "earn": 1500, "color": "#8B5CF6", "icon": "🎭"},
    "P": {"name": "Pub", "time": 4, "earn": 1000, "color": "#F59E0B", "icon": "🍸"},
    "C": {"name": "Commercial Park", "time": 10, "earn": 2000, "color": "#10B981", "icon": "🏢"},
}

def max_profit(n):
    """Calculate maximum profit and building counts"""
    dp = [0] * (n + 1)
    choice = [None] * (n + 1)

    for t in range(n - 1, -1, -1):
        best_profit = -1
        best_choice = None

        for b, info in BUILDINGS.items():
            build_time = info["time"]
            earn_rate = info["earn"]

            finish = t + build_time
            if finish > n:
                continue

            earn_now = (n - finish) * earn_rate
            total_profit = earn_now + dp[finish]

            if total_profit > best_profit:
                best_profit = total_profit
                best_choice = b

        dp[t] = best_profit
        choice[t] = best_choice

    # Reconstruct building counts
    t = 0
    counts = {"T": 0, "P": 0, "C": 0}
    schedule = []
    
    while t < n and choice[t] is not None:
        b = choice[t]
        counts[b] += 1
        schedule.append({
            "building": b,
            "start": t,
            "end": t + BUILDINGS[b]["time"]
        })
        t += BUILDINGS[b]["time"]

    return dp[0], counts, schedule

# Custom CSS for clean single page
st.markdown("""
<style>
    /* Main container */
    .main {
        padding: 20px;
        max-width: 1200px;
        margin: 0 auto;
    }
    
    /* Header styling */
    .main-header {
        text-align: center;
        margin-bottom: 30px;
        padding: 20px;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        border-radius: 15px;
        color: white;
    }
    
    /* Section cards */
    .section-card {
        background: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.08);
        margin-bottom: 20px;
        border-left: 5px solid;
    }
    
    /* Building info cards */
    .building-info {
        display: flex;
        align-items: center;
        padding: 15px;
        background: #f8fafc;
        border-radius: 10px;
        margin: 10px 0;
        border-left: 4px solid;
    }
    
    /* KPI cards */
    .kpi-card {
        text-align: center;
        padding: 15px;
        border-radius: 10px;
        color: white;
        margin: 5px;
    }
    
    /* Timeline items */
    .timeline-item {
        display: inline-block;
        padding: 8px 15px;
        margin: 5px;
        border-radius: 8px;
        color: white;
        font-weight: 500;
    }
    
    /* Hide sidebar */
    [data-testid="stSidebar"] {
        display: none;
    }
    
    /* Make main area full width */
    .block-container {
        padding-top: 20px;
        padding-left: 30px;
        padding-right: 30px;
        max-width: 100%;
    }
</style>
""", unsafe_allow_html=True)

# Page config
st.set_page_config(
    page_title="Max Profit Calculator",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Main header
st.markdown("""
<div class="main-header">
    <h1>🏗️ Max Profit Calculator</h1>
    <p>Optimize your construction strategy for maximum profitability</p>
</div>
""", unsafe_allow_html=True)

# Create two columns for main content
col1, col2 = st.columns([1, 1])

with col1:
    # Control Panel
    st.markdown("""
    <div class="section-card" style="border-left-color: #6366F1;">
        <h3> Control Panel</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Time input
    n = st.number_input(
        "**Total Time Units (n)**",
        min_value=1,
        max_value=100,
        value=20,
        step=1,
        help="Enter the total time units available for construction"
    )
    
    st.markdown("""
    <div style="margin-top: 20px;">
        <small style="color: #64748B;">The algorithm will calculate the optimal building sequence to maximize profit within the given time.</small>
    </div>
    """, unsafe_allow_html=True)

with col2:
    # Building Information
    st.markdown("""
    <div class="section-card" style="border-left-color: #10B981;">
        <h3> Building Portfolio</h3>
    </div>
    """, unsafe_allow_html=True)
    
    for key, info in BUILDINGS.items():
        efficiency = info['earn'] / info['time']
        
        st.markdown(f"""
        <div class="building-info" style="border-left-color: {info['color']};">
            <div style="font-size: 24px; margin-right: 15px;">{info['icon']}</div>
            <div style="flex-grow: 1;">
                <div style="font-weight: 600; font-size: 16px;">{info['name']}</div>
                <div style="color: #64748B; font-size: 14px;">
                    Build Time: {info['time']} units | Earn Rate: ${info['earn']}/unit
                </div>
            </div>
            <div style="text-align: right;">
                <div style="font-size: 14px; color: #64748B;">Efficiency</div>
                <div style="font-weight: 600; color: {info['color']};">${efficiency:.0f}/unit</div>
            </div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Calculate and display results
if n:
    earnings, counts, schedule = max_profit(n)
    time_used = sum(counts[k] * BUILDINGS[k]['time'] for k in counts)
    
    # KPI Metrics
    st.markdown("##  Results")
    
    # Create KPI cards in a row
    kpi_col1, kpi_col2, kpi_col3, kpi_col4 = st.columns(4)
    
    with kpi_col1:
        st.markdown(f"""
        <div class="kpi-card" style="background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);">
            <div style="font-size: 14px; opacity: 0.9;">Total Earnings</div>
            <div style="font-size: 28px; font-weight: bold; margin: 10px 0;">${earnings:,}</div>
            <div style="font-size: 12px; opacity: 0.8;">Maximum Profit</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col2:
        st.markdown(f"""
        <div class="kpi-card" style="background: {BUILDINGS['T']['color']};">
            <div style="font-size: 14px; opacity: 0.9;">Theatres (T)</div>
            <div style="font-size: 28px; font-weight: bold; margin: 10px 0;">{counts['T']}</div>
            <div style="font-size: 12px; opacity: 0.8;">5 units each</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col3:
        st.markdown(f"""
        <div class="kpi-card" style="background: {BUILDINGS['P']['color']};">
            <div style="font-size: 14px; opacity: 0.9;">Pubs (P)</div>
            <div style="font-size: 28px; font-weight: bold; margin: 10px 0;">{counts['P']}</div>
            <div style="font-size: 12px; opacity: 0.8;">4 units each</div>
        </div>
        """, unsafe_allow_html=True)
    
    with kpi_col4:
        st.markdown(f"""
        <div class="kpi-card" style="background: {BUILDINGS['C']['color']};">
            <div style="font-size: 14px; opacity: 0.9;">Parks (C)</div>
            <div style="font-size: 28px; font-weight: bold; margin: 10px 0;">{counts['C']}</div>
            <div style="font-size: 12px; opacity: 0.8;">10 units each</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Detailed Information in two columns
    detail_col1, detail_col2 = st.columns([2, 1])
    
    with detail_col1:
        # Construction Schedule
        st.markdown("""
        <div class="section-card" style="border-left-color: #F59E0B;">
            <h3> Construction Schedule</h3>
        </div>
        """, unsafe_allow_html=True)
        
        if schedule:
            # Show timeline visualization
            timeline_html = '<div style="margin: 20px 0;">'
            for i, project in enumerate(schedule):
                info = BUILDINGS[project["building"]]
                timeline_html += f"""
                <div class="timeline-item" style="background: {info['color']}; margin: 5px 0;">
                    {info['icon']} {info['name']} #{i+1} 
                    (T{project['start']}-T{project['end']})
                </div>
                """
            timeline_html += '</div>'
            st.markdown(timeline_html, unsafe_allow_html=True)
            
            # Show schedule table
            schedule_data = []
            for i, project in enumerate(schedule):
                info = BUILDINGS[project["building"]]
                schedule_data.append({
                    "Project": f"{info['icon']} {info['name']} #{i+1}",
                    "Start": f"T{project['start']}",
                    "Finish": f"T{project['end']}",
                    "Duration": f"{info['time']} units",
                    "Revenue": f"${(n - project['end']) * info['earn']:,}"
                })
            
            df_schedule = pd.DataFrame(schedule_data)
            st.dataframe(df_schedule, use_container_width=True, hide_index=True)
        else:
            st.info("No buildings can be constructed in the given time period.")
    
    with detail_col2:
        # Statistics
        st.markdown("""
        <div class="section-card" style="border-left-color: #6366F1;">
            <h3> Statistics</h3>
        </div>
        """, unsafe_allow_html=True)
        
        total_buildings = sum(counts.values())
        time_remaining = n - time_used
        
        st.markdown(f"""
        <div style="background: #f8fafc; padding: 20px; border-radius: 10px; margin: 15px 0;">
            <div style="margin: 12px 0;">
                <strong>Total Buildings:</strong> {total_buildings}
            </div>
            <div style="margin: 12px 0;">
                <strong>Time Used:</strong> {time_used}/{n} units
            </div>
            <div style="margin: 12px 0;">
                <strong>Time Remaining:</strong> {time_remaining} units
            </div>
            <div style="margin: 12px 0;">
                <strong>Utilization:</strong> {(time_used/n)*100:.1f}%
            </div>
            <div style="margin: 12px 0;">
                <strong>Efficiency:</strong> ${earnings/time_used:.0f}/unit
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        # Progress bar for time utilization
        st.progress(time_used / n if n > 0 else 0)
        st.caption(f"Time Utilization: {time_used}/{n} units")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Output Format (as per problem requirement)
    st.markdown("""
    <div class="section-card" style="border-left-color: #10B981;">
        <h3> Output Format</h3>
    </div>
    """, unsafe_allow_html=True)
    
    output_text = f"**Earnings:** ${earnings:,}\n\n"
    output_text += f"**Solution:** T: {counts['T']}  P: {counts['P']}  C: {counts['C']}"
    
    st.markdown(output_text)
    
    # Display test cases information
    st.markdown("---")
    st.markdown("###  Test Cases Reference")
    
    test_col1, test_col2, test_col3 = st.columns(3)
    
    with test_col1:
        st.markdown("""
        **Test Case 1**
        - Time Unit: 7
        - Earnings: $3,000
        - Solution: T:1 P:0 C:0
        """)
    
    with test_col2:
        st.markdown("""
        **Test Case 2**
        - Time Unit: 8
        - Earnings: $4,500
        - Solution: T:0 P:1 C:0
        """)
    
    with test_col3:
        st.markdown("""
        **Test Case 3**
        - Time Unit: 13
        - Earnings: $16,500
        - Solution: T:2 P:0 C:0
        """)

# Footer
st.markdown("---")
st.markdown("""
<div style="text-align: center; color: #64748B; font-size: 0.9rem; padding: 1rem 0;">
    <p>Max Profit Problem | Dynamic Programming Solution</p>
</div>
""", unsafe_allow_html=True)
