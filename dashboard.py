import streamlit as st
import pandas as pd
import numpy as np
from db_manager import AnalyticsDB
import time

st.set_page_config(page_title="MAANG Ingress Operational Node", layout="wide", page_icon="☣️")

# Custom injection of high-density cyberpunk professional css styling overrides
st.markdown("""
    <style>
    .reportview-container { background: #05070B; }
    div[data-testid="stMetricValue"] { font-family: 'Courier New', monospace; color: #00FFCC; font-weight: bold; font-size: 32px; }
    div[data-testid="stMetricLabel"] { font-size: 13px; font-weight: 600; text-transform: uppercase; letter-spacing: 1px; color: #8D94A5; }
    h1, h2, h3, h4 { font-family: 'Consolas', monospace; color: #FFFFFF; letter-spacing: -0.5px; }
    .stAlert { background-color: #111625; border: 1px solid #FF3366; color: #FFFFFF; }
    </style>
""", unsafe_allow_html=True)

db = AnalyticsDB()

st.title("☣️ FAANG ADVANCED MULTI-SHARD DATASTREAM PLATFORM")
st.markdown("`SYSTEM STATUS: DISTRIBUTED ORCHESTRATION MESH ACTIVE` | `CLUSTER BALANCING: ROUND-ROBIN CONCURRENT` | `INTELLIGENCE SOURCE: HIGH-DIMENSIONAL ISOLATION FOREST`")
st.markdown("---")

ui_placeholder = st.empty()

while True:
    metrics_array = db.fetch_latest_metrics(limit=30)
    live_threats = db.fetch_alerts(limit=12)
    
    if metrics_array:
        # Columns: timestamp, rps, active_bots, avg_latency_ms, stream_entropy, rolling_std_dev, cpu_util, ram_mb, packet_loss
        df = pd.DataFrame(metrics_array, columns=["Timestamp", "Throughput_RPS", "Intercepted_Threats", "Latency_MS", "Shannon_Entropy", "Rolling_Sigma", "CPU_Util", "RAM_MB", "Packet_Loss"])
        df = df.sort_values(by="Timestamp")
        
        latest_rps = df["Throughput_RPS"].iloc[-1]
        latest_threats = df["Intercepted_Threats"].iloc[-1]
        latest_lat = round(df["Latency_MS"].iloc[-1], 3)
        latest_entropy = round(df["Shannon_Entropy"].iloc[-1], 3)
        latest_sigma = round(df["Rolling_Sigma"].iloc[-1], 3)
        latest_cpu = round(df["CPU_Util"].iloc[-1], 1)
        latest_ram = round(df["RAM_MB"].iloc[-1], 1)
        latest_loss = round(df["Packet_Loss"].iloc[-1] * 100, 4)
    else:
        latest_rps, latest_threats, latest_lat, latest_entropy, latest_sigma, latest_cpu, latest_ram, latest_loss = 0, 0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
        df = pd.DataFrame(columns=["Timestamp", "Throughput_RPS", "Intercepted_Threats", "Latency_MS", "Shannon_Entropy", "Rolling_Sigma", "CPU_Util", "RAM_MB", "Packet_Loss"])

    with ui_placeholder.container():
        # ROW 1: System Operational Core Benchmarks
        st.markdown("### 🎛️ Distributed Core Engine Telemetry Matrix")
        m1, m2, m3, m4 = st.columns(4)
        m1.metric(label="🛰️ Core Data Ingestion Rate", value=f"{latest_rps} RPS")
        m2.metric(label="🛡️ Unsupervised ML Intercepts", value=f"{latest_threats} Blocks", delta="Zero-Trust Enforced", delta_color="inverse")
        m3.metric(label="⏱️ End-to-End Latency Overhead", value=f"{latest_lat} ms")
        m4.metric(label="🧮 Structural Shannon Entropy H(X)", value=f"{latest_entropy}")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        # ROW 2: Cluster Bare-Metal Telemetry Health Indicators
        st.markdown("### 🧬 Cluster Virtual Node Hardware Analytics")
        h1, h2, h3, h4 = st.columns(4)
        h1.metric(label="💻 Thread Pool CPU Allotment", value=f"{latest_cpu} %")
        h2.metric(label="💾 Sandbox Memory Resident Footprint", value=f"{latest_ram} MB")
        h3.metric(label="📡 Packet Shard Ingress Drop Rate", value=f"{latest_loss} %")
        h4.metric(label="📊 Statistical Variance Velocity (σ)", value=f"{latest_sigma}")
        
        st.markdown("---")
        
        # ROW 3: High-Fidelity Data Spline Visual Node Arrays
        chart_col1, chart_col2 = st.columns(2)
        with chart_col1:
            st.markdown("#### 📈 Microservice Core Throughput Waveform (RPS Dynamic Trace)")
            st.line_chart(data=df, x="Timestamp", y="Throughput_RPS", color="#00FFCC")
            
            st.markdown("#### 🧠 Real-Time Computational Hardware Overhead (CPU vs Memory Matrix)")
            st.area_chart(data=df, x="Timestamp", y=["CPU_Util", "Packet_Loss"])
            
        with chart_col2:
            st.markdown("#### 🚨 Multi-Shard Threat Detection Volume Graph")
            st.area_chart(data=df, x="Timestamp", y="Intercepted_Threats", color="#FF3366")
            
            st.markdown("#### 🧮 Mathematical Chaos Standard Deviation Spline")
            st.bar_chart(data=df, x="Timestamp", y="Rolling_Sigma", color="#9933FF")
            
        st.markdown("---")
        
        # ROW 4: Distributed System Dynamic Threat Ledger
        st.markdown("#### 🛑 Centralized Threat Intelligence & Microservice Router Ledger")
        if live_threats:
            threat_df = pd.DataFrame(live_threats, columns=["Ingress Network Time", "Anomalous Token ID", "IPv4 Origin Vector", "Classified Payload Risk Pattern", "Mathematical Threat Proximity Weights", "Target Route Server Allocation"])
            st.dataframe(threat_df, use_container_width=True)
        else:
            st.info("System Shards operating at nominal parameters. Load balancer distribution equalized.")
            
    time.time()
    time.sleep(1.0) # Clock tick synchronization anchor