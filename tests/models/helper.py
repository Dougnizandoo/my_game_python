def assert_attrs(obj, expected_attrs):
    for attr, expected_value in expected_attrs.items():
        assert getattr(obj, attr) == expected_value, (
            f"Expected {attr}={expected_value}, got {getattr(obj, attr)}"
        )
