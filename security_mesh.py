import re
import time

class IngressSecurityMesh:
    # Pre-compiled regex patterns for scanning payload anomalies (FAANG standard)
    SQL_INJECTION_PATTERN = re.compile(r"UNION\s+SELECT|SELECT\s+.*\s+FROM|DROP\s+TABLE|--|;", re.IGNORECASE)
    XSS_PATTERN = re.compile(r"<script>|javascript:|onerror=", re.IGNORECASE)
    
    def __init__(self):
        self.ip_blacklist = {"192.168.44.110", "10.0.12.220"} # High-risk flagged botnets
        self.rate_limit_directory = {} # Memory cache for sliding window rate limits

    def inspect_ingress_packet(self, ip_address: str, target_url: str, payload_sample: str) -> dict:
        """
        Deep packet assessment engine before sending to downstream vector processors.
        """
        current_time = time.time()
        
        # 1. Edge Firewall Check
        if ip_address in self.ip_blacklist:
            return {"safe": False, "threat_type": "BLACKLISTED_BOTNET_NODE", "severity": 1.0}
            
        # 2. XSS / SQLi Payload Injection Inspection
        if self.SQL_INJECTION_PATTERN.search(target_url) or self.SQL_INJECTION_PATTERN.search(payload_sample):
            return {"safe": False, "threat_type": "SQL_INJECTION_ATTEMPT", "severity": 0.95}
            
        if self.XSS_PATTERN.search(payload_sample):
            return {"safe": False, "threat_type": "CROSS_SITE_SCRIPTING_XSS", "severity": 0.88}

        # 3. Microsecond-level Stateful Rate Limiting
        if ip_address not in self.rate_limit_directory:
            self.rate_limit_directory[ip_address] = []
            
        # Evict timestamps older than 1 second window
        self.rate_limit_directory[ip_address] = [t for t in self.rate_limit_directory[ip_address] if current_time - t < 1.0]
        self.rate_limit_directory[ip_address].append(current_time)
        
        if len(self.rate_limit_directory[ip_address]) > 45: # Over 45 requests per second is inhuman
            return {"safe": False, "threat_type": "DDoS_BRUTEFORCE_BURST", "severity": 0.98}

        return {"safe": True, "threat_type": "CLEAN_TRANSACTION", "severity": 0.0}