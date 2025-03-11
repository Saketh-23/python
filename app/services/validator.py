def validate_schemas(api_schema, db_schema):
    """Validate API schema against the database schema."""
    print("Validating API and database schema consistency...")

    missing_tables = [
        endpoint["table"]
        for endpoint in api_schema.get("endpoints", [])
        if endpoint["table"] not in db_schema.get("tables", {})
    ]

    if missing_tables:
        print(f"Warning: API schema references missing tables: {missing_tables}")
    
    return {"validation_passed": len(missing_tables) == 0, "missing_tables": missing_tables}
