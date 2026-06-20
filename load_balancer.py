import itertools

class DistributedLoadBalancer:
    def __init__(self):
        # Initializing 3 mock microservice cluster nodes (FAANG Sharding Standard)
        self.cluster_nodes = [
            {"node_id": "CLUSTER-US-EAST-01", "status": "HEALTHY", "load_coefficient": 0.0},
            {"node_id": "CLUSTER-EU-WEST-02", "status": "HEALTHY", "load_coefficient": 0.0},
            {"node_id": "CLUSTER-AP-SOUTH-03", "status": "HEALTHY", "load_coefficient": 0.0}
        ]
        self.node_cycler = itertools.cycle(self.cluster_nodes)

    def route_request(self, click_weight: int) -> dict:
        """
        Dynamically cycles and simulates node capacity updates on each incoming data packet burst.
        """
        target_node = next(self.node_cycler)
        
        # Simulating operational load index scaling mathematically
        target_node["load_coefficient"] = round((click_weight / 90.0) * 100, 2)
        if target_node["load_coefficient"] > 85.0:
            target_node["status"] = "HIGH_LOAD"
        else:
            target_node["status"] = "HEALTHY"
            
        return {
            "allocated_node": target_node["node_id"],
            "node_status": target_node["status"],
            "capacity_used_pct": target_node["load_coefficient"]
        }