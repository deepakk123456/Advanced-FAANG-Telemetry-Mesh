import numpy as np

class RealTimeStreamAnalytics:
    @staticmethod
    def calculate_rolling_variance(rps_history: list) -> dict:
        """
        Computes advanced distribution characteristics of current pipeline throughput.
        """
        if not rps_history or len(rps_history) < 2:
            return {"variance": 0.0, "std_dev": 0.0, "z_score_stability": "STABLE"}
            
        data = np.array(rps_history)
        variance = float(np.var(data))
        std_dev = float(np.std(data))
        
        # Calculate volatility scale
        if std_dev > 15.0:
            stability = "CRITICAL_VOLATILITY_BURST"
        elif std_dev > 5.0:
            stability = "MODERATE_FLUCTUATION"
        else:
            stability = "STEADY_STATE"
            
        return {
            "variance": round(variance, 4),
            "std_dev": round(std_dev, 4),
            "z_score_stability": stability
        }

    @staticmethod
    def calculate_entropy(threat_types: list) -> float:
        """
        Shannon Entropy Equation to determine the unpredictability distribution of inbound threat variants.
        Formula: H(X) = -sum(P(x) * log2(P(x)))
        """
        if not threat_types:
            return 0.0
            
        _, counts = np.unique(threat_types, return_counts=True)
        probabilities = counts / len(threat_types)
        entropy = -np.sum(probabilities * np.log2(probabilities))
        return float(round(entropy, 4))