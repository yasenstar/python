graph = {
    "Paris": [
        ("CAPITAL_OF", "France")
    ],
    "France": [
        ("LOCATED_IN", "Europe")
    ]
}

for relation, target in graph.get("Paris", []):
    print("Paris", relation, target)


# RESULT:
# Paris CAPITAL_OF France