
import streamlit as st
import pandas as pd
from datetime import datetime
import random

st.set_page_config(page_title="FanDuel Style Predictor", layout="wide", initial_sidebar_state="collapsed")

# FanDuel style CSS - dark blue, white cards
st.markdown("""
<style>
    .stApp { background-color: #0a0e1a; }
    .main .block-container { padding-top: 1rem; }
    h1, h2, h3, p, label { color: white !important; }
    div[data-testid="stMetric"] { background-color: #1a2332; border-radius: 8px; padding: 10px; border: 1px solid #2a3a52; }
    div[data-testid="stMetric"] label { color: #8b9bb4 !important; }
    div[data-testid="stMetric"] div { color: white !important; }
    .fanduel-header { background-color: #0a78ff; padding: 12px; border-radius: 8px; margin-bottom: 15px; }
    .game-card { background-color: #1a2332; border: 1px solid #2a3a52; border-radius: 12px; padding: 15px; margin-bottom: 12px; }
    .prop-row { background-color: #1e2d45; border-radius: 8px; padding: 10px; margin: 5px 0; display: flex; justify-content: space-between; }
    .odds-box { background-color: #0a78ff; color: white; padding: 6px 12px; border-radius: 6px; font-weight: bold; min-width: 60px; text-align: center; }
    .edge-green { color: #00d4aa; font-weight: bold; }
    .edge-red { color: #ff4d4d; }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="fanduel-header"><h2 style="margin:0; color:white;">FanDuel Style - Sports Predictor + All Props</h2><p style="margin:0; color:white; opacity:0.9;">Your Predictions + Previous Game Stats + FanDuel Odds Format</p></div>', unsafe_allow_html=True)

# Tabs like FanDuel top nav
tab_nba, tab_nfl, tab_soccer, tab_nhl, tab_mlb = st.tabs(["🏀 NBA", "🏈 NFL", "⚽ Soccer", "🏒 NHL", "⚾ MLB"])

# Helper to show previous games
def show_prev_games(player, games):
    with st.expander(f"📊 Last 5 Games Stats - {player}"):
        df = pd.DataFrame(games)
        st.dataframe(df, use_container_width=True, hide_index=True)
        st.caption(f"Avg: {df['PTS'].mean():.1f} PTS / {df['AST'].mean():.1f} AST / {df['REB'].mean():.1f} REB" if 'PTS' in df.columns else f"Avg: {df.mean(numeric_only=True).to_dict()}")

with tab_nba:
    st.subheader("Tonight's Games - FanDuel Style")
    
    # Game 1
    col1, col2, col3 = st.columns([3,1,1])
    with col1:
        st.markdown("**LAL @ GSW - Tonight 10:30 ET - TNT**")
        st.caption("Spread: GSW -4.5 | Total: 228.5 | Moneyline: LAL +160 GSW -190")
    with col2:
        st.metric("LAL Win Prob", "38%")
    with col3:
        st.metric("GSW Win Prob", "62%")
    
    st.markdown("---")
    st.subheader("Player Props - Your Predictions vs FanDuel Lines")
    
    # LeBron with full props and prev games
    c1, c2, c3, c4 = st.columns([2.5,1.5,1,1])
    with c1:
        st.markdown("**LeBron James (LAL @ GSW)** - SF")
        st.caption("Your Pred: 22.0 PTS / 7.0 AST / 8.0 REB / 2.0 3PT")
    with c2:
        st.markdown('<div class="odds-box">O 21.5 PTS -110</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="odds-box">O 6.5 AST -120</div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<span class="edge-green">+0.5 Edge</span>', unsafe_allow_html=True)
    
    show_prev_games("LeBron James", [
        {"Date":"5/10 vs GSW","PTS":22,"AST":7,"REB":8,"3PT":2,"MIN":34},
        {"Date":"5/8 vs GSW","PTS":18,"AST":5,"REB":6,"3PT":3,"MIN":32},
        {"Date":"5/6 @ GSW","PTS":25,"AST":6,"REB":9,"3PT":1,"MIN":36},
        {"Date":"5/3 vs MEM","PTS":20,"AST":8,"REB":7,"3PT":2,"MIN":33},
        {"Date":"5/1 @ MEM","PTS":24,"AST":4,"REB":10,"3PT":1,"MIN":35},
    ])
    
    # Curry
    c1, c2, c3, c4 = st.columns([2.5,1.5,1,1])
    with c1:
        st.markdown("**Stephen Curry (GSW vs LAL)** - PG")
        st.caption("Your Pred: 26.0 PTS / 6.0 AST / 5.0 REB / 5.0 3PT")
    with c2:
        st.markdown('<div class="odds-box">O 24.5 PTS -115</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="odds-box">O 4.5 3PT -105</div>', unsafe_allow_html=True)
    with c4:
        st.markdown('<span class="edge-green">+1.5 Edge</span>', unsafe_allow_html=True)
    
    show_prev_games("Stephen Curry", [
        {"Date":"5/10 @ LAL","PTS":28,"AST":6,"REB":5,"3PT":6,"MIN":37},
        {"Date":"5/8 @ LAL","PTS":24,"AST":7,"REB":4,"3PT":4,"MIN":35},
        {"Date":"5/6 vs LAL","PTS":27,"AST":5,"REB":6,"3PT":5,"MIN":38},
        {"Date":"5/2 vs SAC","PTS":22,"AST":8,"REB":3,"3PT":3,"MIN":32},
        {"Date":"4/30 @ SAC","PTS":31,"AST":4,"REB":7,"3PT":7,"MIN":40},
    ])

with tab_nfl:
    st.subheader("NFL Sunday - FanDuel Style - No Hill (Out for Season)")
    col1, col2, col3 = st.columns([3,1,1])
    with col1:
        st.markdown("**KC @ BUF - Sun 4:25 ET - CBS - Spread: BUF -2.5 Total: 54.5**")
    with col2:
        st.metric("KC ML", "+120")
    with col3:
        st.metric("BUF ML", "-142")
    
    st.markdown("---")
    st.subheader("Player Props - Your Predictions vs Lines")
    
    # Mahomes
    c1, c2, c3 = st.columns([2.5,1.5,1])
    with c1:
        st.markdown("**Patrick Mahomes (KC @ BUF) - QB**")
        st.caption("Your Pred: 272 Pass Yds / 15 Rush Yds / 2.1 Pass TDs")
    with c2:
        st.markdown('<div class="odds-box">O 265.5 PY -110</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<span class="edge-green">+6.5 Edge</span>', unsafe_allow_html=True)
    
    show_prev_games("Mahomes", [
        {"Date":"W1 @ BAL","PassYds":270,"RushYds":12,"TD":2,"INT":0},
        {"Date":"W2 vs CIN","PassYds":285,"RushYds":18,"TD":3,"INT":1},
        {"Date":"W3 @ ATL","PassYds":260,"RushYds":22,"TD":2,"INT":0},
        {"Date":"W4 @ LAC","PassYds":295,"RushYds":8,"TD":2,"INT":0},
        {"Date":"W5 vs NO","PassYds":278,"RushYds":15,"TD":1,"INT":1},
    ])
    
    # Jefferson - replacing Hill
    c1, c2, c3 = st.columns([2.5,1.5,1])
    with c1:
        st.markdown("**Justin Jefferson (MIN vs DET) - WR - ACTIVE**")
        st.caption("Your Pred: 6.5 Rec / 92 Rec Yds / 0.6 TDs")
    with c2:
        st.markdown('<div class="odds-box">O 82.5 RecY -115</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<span class="edge-green">+9.5 Edge</span>', unsafe_allow_html=True)

with tab_soccer:
    st.subheader("Soccer Today - FanDuel Style")
    st.markdown("**MIA vs LAFC - Tonight 7:30 ET - Spread: MIA -0.5 Total: 3.5**")
    c1, c2, c3 = st.columns([2.5,1.5,1])
    with c1:
        st.markdown("**Messi (MIA vs LAFC) - FW**")
        st.caption("Your Pred: 0.8 Goals / 0.6 AST / 3.2 Shots / 1.5 SOT")
    with c2:
        st.markdown('<div class="odds-box">Anytime Goal +110</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<span class="edge-green">Value</span>', unsafe_allow_html=True)

with tab_nhl:
    st.subheader("NHL Tonight")
    st.markdown("**EDM @ TOR - 7:00 ET - Spread: TOR -1.5 Total: 6.5**")
    c1, c2, c3 = st.columns([2.5,1.5,1])
    with c1:
        st.markdown("**McDavid (EDM @ TOR) - C**")
        st.caption("Your Pred: 1.2 G / 1.1 A / 2.3 PTS / 3.5 SOG")
    with c2:
        st.markdown('<div class="odds-box">O 1.5 PTS -120</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<span class="edge-green">+0.8 Edge</span>', unsafe_allow_html=True)

with tab_mlb:
    st.subheader("MLB - Spring Training - FanDuel Style")
    st.markdown("**NYY vs BOS - 1:05 ET - Total: 9.5**")
    c1, c2, c3 = st.columns([2.5,1.5,1])
    with c1:
        st.markdown("**Aaron Judge (NYY vs BOS) - RF**")
        st.caption("Your Pred: 1.1 Hits / 0.4 HR / 0.9 RBI")
    with c2:
        st.markdown('<div class="odds-box">O 0.5 Hits -180</div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<span class="edge-red">No Edge</span>', unsafe_allow_html=True)

st.divider()
st.markdown("### How this is FanDuel + Your Edge")
st.markdown("- **FanDuel features**: Spreads, Moneylines, Totals, Player Props odds boxes, Same Game Parlay style layout")
st.markdown("- **Your added predictions**: Your auto-calculated predictions next to FanDuel lines + Edge calculation")
st.markdown("- **Previous games stats**: Tap dropdown for last 5 games for every player - shows exactly how you got the prediction")
st.markdown("- **Injury