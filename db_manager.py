import sqlite3
import os
import time

BASE_DIR = os.path.dirname(os.path.abspath(__file__)) if '__file__' in locals() else os.getcwd()
DB_PATH = os.path.join(BASE_DIR, "clickstream_telemetry.db")

class AnalyticsDB:
    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH, check_same_thread=False)
        self.initialize_schema()

    def initialize_schema(self):
        with self.conn:
            # 1. Base Security Alerts Schema
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS security_alerts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    timestamp REAL,
                    user_id TEXT,
                    ip_address TEXT,
                    threat_type TEXT,
                    severity_score REAL,
                    allocated_node TEXT
                )
            """)
            
            # --- DYNAMIC FAULT TOLERANCE MATRIX (FAANG STANDARD) ---
            # Agar table pehle se bana hai aur allocated_node column nahi mila, toh automatic alter script inject karo
            try:
                self.conn.execute("ALTER TABLE security_alerts ADD COLUMN allocated_node TEXT")
                print("🛡️ [DB SCHEEMA] Patched security_alerts vector metrics dynamically.")
            except sqlite3.OperationalError:
                pass # Column pehle se hi exist karta hai

            # 2. Base Cluster Metrics Schema
            self.conn.execute("""
                CREATE TABLE IF NOT EXISTS cluster_metrics (
                    timestamp REAL PRIMARY KEY,
                    rps INTEGER,
                    active_bots INTEGER,
                    avg_latency_ms REAL,
                    stream_entropy REAL,
                    rolling_std_dev REAL,
                    cpu_util REAL,
                    ram_mb REAL,
                    packet_loss REAL
                )
            """)

    def log_alert(self, user_id: str, ip: str, threat: str, severity: float, node: str):
        with self.conn:
            self.conn.execute(
                "INSERT INTO security_alerts (timestamp, user_id, ip_address, threat_type, severity_score, allocated_node) VALUES (?, ?, ?, ?, ?, ?)",
                (time.time(), user_id, ip, threat, severity, node)
            )

    def update_metrics(self, rps: int, bots: int, latency: float, entropy: float, std_dev: float, cpu: float, ram: float, loss: float):
        with self.conn:
            self.conn.execute(
                "INSERT OR REPLACE INTO cluster_metrics (timestamp, rps, active_bots, avg_latency_ms, stream_entropy, rolling_std_dev, cpu_util, ram_mb, packet_loss) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
                (time.time(), rps, bots, latency, entropy, std_dev, cpu, ram, loss)
            )

    def fetch_latest_metrics(self, limit: int = 30):
        cursor = self.conn.cursor()
        cursor.execute("SELECT timestamp, rps, active_bots, avg_latency_ms, stream_entropy, rolling_std_dev, cpu_util, ram_mb, packet_loss FROM cluster_metrics ORDER BY timestamp DESC LIMIT ?", (limit,))
        return cursor.fetchall()

    def fetch_alerts(self, limit: int = 12):
        cursor = self.conn.cursor()
        cursor.execute("SELECT datetime(timestamp, 'unixepoch', 'localtime'), user_id, ip_address, threat_type, severity_score, allocated_node FROM security_alerts ORDER BY id DESC LIMIT ?", (limit,))
        return cursor.fetchall()