def get_traffic_level(value):
    if value < 30:
        return "LOW"
    elif value < 70:
        return "MEDIUM"
    return "HIGH"