def validate_resource_data(data):
    required_fields = ["name", "description"]
    for field in required_fields:
        if field not in data:
            raise ValueError(f"Missing required field: {field}")