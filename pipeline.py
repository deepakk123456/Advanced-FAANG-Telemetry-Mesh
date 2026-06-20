import time
import random
import numpy as np
from sklearn.ensemble import IsolationForest
from db_manager import AnalyticsDB
from security_mesh import IngressSecurityMesh
from analytics import RealTimeStreamAnalytics
from load_balancer import DistributedLoadBalancer
from health_monitor import ClusterHealthMonitor

db = AnalyticsDB()
firewall = IngressSecurityMesh()
balancer = DistributedLoadBalancer()

# Isolation Forest setup
normal_distribution = np.random.normal(loc=[3, 150, 1.2], scale=[1, 25, 0.3], size=(250, 3))
adversarial_distribution = np.random.uniform(low=[40, 1, 8.0], high=[85, 4, 15.0], size=(25, 3))
training_matrix = np.vstack([normal_distribution, adversarial_distribution])

ml_classifier = IsolationForest(contamination=0.08, random_state=1337)
ml_classifier.fit(training_matrix)
print("⚙️ [CORE COMPUTE NODE] Distributed Matrix boundaries mapped across Virtual Shards.")

def start_faang_ingestion_loop():
    print("🚀 [INGRESS PROTOCOL] Microservice Stream Routing Mesh is ONLINE.")
    rps_sliding_window = []
    
    while True:
        simulated_packets = random.randint(40, 100) # Higher load for massive scale
        active_bots = 0
        total_processing_latency = 0.0
        threat_signatures_epoch = []
        
        for _ in range(simulated_packets):
            attack_roll = random.random()
            
            if attack_roll < 0.06: # Botnet behavior
                clicks, duration, bounce = random.randint(45, 90), random.uniform(0.5, 3.0), random.uniform(8.0, 14.0)
                user_id, ip = f"NODE-BOT-{random.randint(100, 999)}", f"192.168.44.{random.randint(10, 254)}"
                payload, target_uri = "Automated scraping header override", "/api/v1/telemetry/sync"
            elif attack_roll < 0.10: # Exploits
                clicks, duration, bounce = random.randint(1, 4), random.randint(10, 50), random.uniform(0.5, 2.0)
                user_id, ip = f"EXPL-HACK-{random.randint(4000, 5000)}", f"45.79.{random.randint(10, 200)}.{random.randint(1, 254)}"
                payload = random.choice(["SELECT * FROM users; DROP TABLE database; --", "<script>window.location=evil</script>"])
                target_uri = random.choice(["/admin/config?id=DROP", "/checkout?token=<script>"])
            else: # Standard Humans
                clicks, duration, bounce = random.randint(1, 6), random.randint(60, 450), random.uniform(0.2, 2.5)
                user_id, ip = f"USER-COR-{random.randint(1000, 9999)}", f"172.56.{random.randint(1, 99)}.{random.randint(1, 254)}"
                payload, target_uri = "Standard analytical payload payload JSON", "/home/feed"

            execution_start = time.time()
            
            # 1. Routing Traffic Through Distributed Load Balancer
            routing_metadata = balancer.route_request(clicks)
            assigned_cluster = routing_metadata["allocated_node"]
            
            # 2. Ingress Firewall Inspection
            security_evaluation = firewall.inspect_ingress_packet(ip, target_uri, payload)
            
            # 3. ML Processing Core
            features_array = np.array([[clicks, duration, bounce]])
            ml_prediction = ml_classifier.predict(features_array)[0]
            
            latency_delta = (time.time() - execution_start) * 1000
            total_processing_latency += latency_delta
            
            if not security_evaluation["safe"] or ml_prediction == -1:
                active_bots += 1
                threat_tag = security_evaluation["threat_type"] if not security_evaluation["safe"] else "UNSUPERVISED_ML_ISOLATION_ANOMALY"
                severity = security_evaluation["severity"] if security_evaluation["severity"] > 0 else abs(float(ml_classifier.decision_function(features_array)[0]))
                
                threat_signatures_epoch.append(threat_tag)
                db.log_alert(user_id, ip, threat_tag, round(severity, 3), assigned_cluster)

        # Statistical Calculations & Rolling Window
        rps_sliding_window.append(simulated_packets)
        if len(rps_sliding_window) > 25:
            rps_sliding_window.pop(0)
            
        statistical_metrics = RealTimeStreamAnalytics.calculate_rolling_variance(rps_sliding_window)
        calculated_entropy = RealTimeStreamAnalytics.calculate_entropy(threat_signatures_epoch)
        avg_epoch_latency = total_processing_latency / simulated_packets if simulated_packets else 0.0
        
        # 4. Extract Real-Time Hardware Resource Telemetry
        system_vitals = ClusterHealthMonitor.inspect_system_vitals()
        
        # Stream into Database Store Room
        db.update_metrics(
            rps=simulated_packets,
            bots=active_bots,
            latency=avg_epoch_latency,
            entropy=calculated_entropy,
            std_dev=statistical_metrics["std_dev"],
            cpu=system_vitals["cpu_util_pct"],
            ram=system_vitals["ram_allocated_mb"],
            loss=system_vitals["packet_drop_rate"]
        )
        time.sleep(1.0)

if __name__ == "__main__":
    start_faang_ingestion_loop()