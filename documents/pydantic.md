# Pydantic Documentation

# Introduction

Pydantic is a Python library for data validation and parsing using Python type annotations. It allows developers to define data structures as Python classes and automatically validates incoming data to ensure it matches the expected types.

Pydantic is widely used in Python applications and serves as the data validation layer for frameworks such as FastAPI.

---

# Key Features

- Data validation using Python type hints
- Automatic type conversion
- JSON Schema generation
- Easy-to-create data models
- Detailed validation error messages
- High performance
- IDE-friendly type checking
- Integration with FastAPI and other frameworks

---

# BaseModel

`BaseModel` is the foundation of every Pydantic model.

To create a data model, a Python class inherits from `BaseModel`. Every attribute declared inside the class becomes a validated field.

When data is passed to a model, Pydantic automatically checks whether the values match the expected data types.

### Benefits of BaseModel

- Automatic validation
- Automatic parsing
- Serialization to dictionaries and JSON
- Easy integration with APIs
- Type safety

### Example

A User model may contain:

- id
- name
- email
- age

When a User object is created, Pydantic validates every field before creating the object.

---

# Models

A model is a Python class that defines the structure of data.

Models represent real-world objects such as:

- User
- Product
- Employee
- Student
- Order
- Customer

Each model contains fields that describe the object's properties.

### Example User Model

A User model might contain:

- User ID
- Name
- Email
- Date of Birth

### Benefits of Models

- Organize application data
- Improve readability
- Reuse data structures
- Automatic validation
- Easy serialization

---

# Fields

Fields are the attributes defined inside a Pydantic model.

Each field has:

- Name
- Data type
- Optional default value
- Validation rules

### Common Field Types

- Integer (`int`)
- String (`str`)
- Float (`float`)
- Boolean (`bool`)
- List (`list`)
- Dictionary (`dict`)
- Date (`datetime`)

### Field Options

Fields can include additional information such as:

- Default values
- Descriptions
- Minimum values
- Maximum values
- Required or optional status

### Example Fields

A Product model could contain:

| Field | Type | Description |
|--------|------|-------------|
| id | Integer | Product ID |
| name | String | Product name |
| price | Float | Product price |
| available | Boolean | Availability status |

---

# Validation

Validation is the process of checking whether incoming data satisfies the rules defined in a model.

Whenever a model is created, Pydantic automatically validates all fields.

If the data is valid, the model instance is created.

If the data is invalid, Pydantic raises a validation error describing exactly what is wrong.

### Validation Checks

Pydantic validates:

- Data types
- Required fields
- Missing values
- Numeric constraints
- String constraints
- Nested objects
- Lists and dictionaries

### Validation Process

```
Input Data
     |
     v
Pydantic Model
     |
     v
Validation
     |
+------------+
|            |
Valid     Invalid
|            |
v            v
Model     Validation Error
Created
```

### Benefits of Validation

- Prevents invalid data
- Improves application reliability
- Reduces runtime errors
- Produces clear error messages
- Ensures data consistency

---

# Type Hints

Pydantic uses Python type annotations to determine how each field should be validated.

Common type hints include:

- `int`
- `str`
- `float`
- `bool`
- `list`
- `dict`
- `datetime`

These type hints allow Pydantic to automatically parse and validate incoming data.

---

# JSON Schema

Pydantic models can automatically generate JSON Schema.

JSON Schema describes:

- Field names
- Data types
- Required fields
- Validation rules

This feature is commonly used by FastAPI to generate OpenAPI documentation.

---

# Serialization

Serialization converts a Pydantic model into formats such as:

- Dictionary
- JSON

Serialization is useful when sending responses from APIs or storing data.

---

# Validation Errors

If validation fails, Pydantic returns detailed error information.

Examples of validation errors include:

- Missing required field
- Invalid integer
- Invalid string
- Invalid date format
- Value out of allowed range

These error messages help developers quickly identify and fix input problems.

---

# Advantages of Pydantic

- Easy to learn
- Automatic validation
- Type-safe models
- High performance
- JSON Schema generation
- Excellent FastAPI integration
- Detailed error reporting
- Clean and readable code

---

# Common Use Cases

Pydantic is commonly used for:

- API request validation
- API response validation
- Configuration management
- Data parsing
- JSON serialization
- Machine learning applications
- Backend development

---

# Summary

Pydantic is a powerful Python library for defining and validating structured data. By using `BaseModel`, developers can create reusable models with strongly typed fields. Pydantic automatically validates input data, reports clear validation errors, and supports serialization and JSON Schema generation. These features make it an essential tool for building reliable Python applications, especially when working with FastAPI and modern APIs.