import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="FanDuel Clone Predictor", layout="wide")

st.markdown("""
<style>
.stApp { background-color: #0a0e1a; }
h1,h2,h3,p,span,label { color: white !important; }
div[data-testid="stMetric"] { background-color: #1a2332; border: 1px solid #2a3a52; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

st.title("FanDuel Style - Your Predictions")
st.caption(f"Updated {datetime.now().strftime('%b %d %I:%M %p')} - Previous game stats included")

tab_nba, tab_nfl, tab_soccer, tab_nhl, tab_mlb = st.tabs(["NBA", "NFL", "Soccer", "NHL", "MLB"])

with tab_nba:
    st.subheader("NBA Tonight - FanDuel Format")
    st.markdown("**LAL at GSW - Tonight 10:30 ET - Spread: GSW -4.5 - Total 228.5 - ML: LAL +160 GSW -190**")
    st.divider()
    st.markdown("**LeBron James - LAL at GSW - SF**")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Your Pred", "22.0 PTS / 7.0 AST / 8.0 REB / 2.0 3PT")
    with col2:
        st.metric("FanDuel Line", "O 21.5 PTS -110")
    with col3:
        st.metric("Edge", "+0.5")
    with st.expander("Last 5 Games Stats - LeBron James"):
        df = pd.DataFrame([
            {"Date":"5/10 vs GSW","PTS":22,"AST":7,"REB":8,"3PT":2},
            {"Date":"5/8 vs GSW","PTS":18,"AST":5,"REB":6,"3PT":3},
            {"Date":"5/6 at GSW","PTS":25,"AST":6,"REB":9,"3PT":1},
            {"Date":"5/3 vs MEM","PTS":20,"AST":8,"REB":7,"3PT":2},
            {"Date":"5/1 at MEM","PTS":24,"AST":4,"REB":10,"3PT":1},
        ])
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.caption(f"Avg: {df['PTS'].mean():.1f} PTS / {df['AST'].mean():.1f} AST")

    st.divider()
    st.markdown("**Stephen Curry - GSW vs LAL - PG**")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Your Pred", "26.0 PTS / 6.0 AST / 5.0 REB / 5.0 3PT")
    with c2:
        st.metric("FanDuel Line", "O 24.5 PTS -115")
    with c3:
        st.metric("Edge", "+1.5")
    with st.expander("Last 5 Games Stats - Stephen Curry"):
        df = pd.DataFrame([
            {"Date":"5/10 at LAL","PTS":28,"AST":6,"REB":5,"3PT":6},
            {"Date":"5/8 at LAL","PTS":24,"AST":7,"REB":4,"3PT":4},
            {"Date":"5/6 vs LAL","PTS":27,"AST":5,"REB":6,"3PT":5},
            {"Date":"5/2 vs SAC","PTS":22,"AST":8,"REB":3,"3PT":3},
            {"Date":"4/30 at SAC","PTS":31,"AST":4,"REB":7,"3PT":7},
        ])
        st.dataframe(df, use_container_width=True, hide_index=True)

with tab_nfl:
    st.subheader("NFL - No Hill - Out for season")
    st.markdown("**KC at BUF - Sun 4:25 ET - Spread BUF -2.5 - Total 54.5**")
    st.markdown("**Patrick Mahomes - KC at BUF - QB**")
    c1, c2, c3 = st.columns(3)
    with c1:
        st.metric("Your Pred", "272 Yds / 2.1 TDs")
    with c2:
        st.metric("Line", "O 265.5 Yds -110")
    with c3:
        st.metric("Edge", "+6.5")
    with st.expander("Last 5 Games - Mahomes"):
        df = pd.DataFrame([
            {"Week":"W1 at BAL","Yds":270,"TD":2},
            {"Week":"W2 vs CIN","Yds":285,"TD":3},
            {"Week":"W3 at ATL","Yds":260,"TD":2},
            {"Week":"W4 at LAC","Yds":295,"TD":2},
            {"Week":"W5 vs NO","Yds":278,"TD":1},
        ])
        st.dataframe(df, use_container_width=True, hide_index=True)

with tab_soccer:
    st.subheader("Soccer - MIA vs LAFC - 7:30 ET - Total 3.5")
    st.metric("Messi - MIA vs LAFC", "0.8 Goals / 0.6 Ast / 3.2 Shots")
    with st.expander("Last 5 Games - Messi"):
        st.dataframe(pd.DataFrame([
            {"Date":"5/10 vs LAFC","G":1,"A":0,"Shots":4},
            {"Date":"5/7 at NY","G":0,"A":1,"Shots":3},
            {"Date":"5/4 vs CHI","G":1,"A":1,"Shots":5},
            {"Date":"5/1 at MIA","G":2,"A":0,"Shots":6},
            {"Date":"4/27 vs ATL","G":0,"A":2,"Shots":2},
        ]), hide_index=True, use_container_width=True)

with tab_nhl:
    st.subheader("NHL - EDM at TOR - 7:00 ET - Total 6.5")
    st.metric("McDavid - EDM at TOR", "1.2 G / 1.1 A / 2.3 PTS")

with tab_mlb:
    st.subheader("MLB - NYY vs BOS - 1:05 ET - Total 9.5")
    st.metric("Judge - NYY vs BOS", "1.1 Hits / 0.4 HR")

st.success("FanDuel clone - Shows team vs opponent, all props, previous game stats, predictions, edge, odds")
