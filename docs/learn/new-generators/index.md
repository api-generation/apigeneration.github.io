# Developing New Generators

As described in the [MTT Overview](/learn/mtt-overview), a core design principle of the **Model Transform Tools (MTT)** is to make adding and customizing Generators flexible, quick, and easy.

---

## Generator Dependencies

Creating a new Generator requires aligning with both high-level semantic specifications and underlying syntax formats. The relationship below illustrates how target standards build upon one another:

![Generator Dependencies](assets/generator-dependencies.png)

*Figure 1: Relationship between low-level syntax formats and high-level schema semantics.*

---

## Architectural Principles

When developing or tailoring a generator, keep these two key structural points in mind:

### 1. Dependencies Between Standards
Higher-level specifications are not built in a vacuum—they rely on standard foundational formats for their syntax:
* **The API & Schema Layers**: Both the **OpenAPI standard** and custom **Reversed standard** rely on the **[JSON Schema Standard](https://json-schema.org/)** to establish object validation, types, and parameters.
* **The Base Serialization Layer**: Underlying everything, both JSON Schema and OpenAPI are serialized as valid **[JSON](https://www.json.org/)** (or YAML), meaning your generator must adhere to strict base-level formatting.

### 2. Double Conformance (Syntax vs. Semantics)
Your generator must validate and satisfy rules on both layers:
* **Format (Syntax)**: Generates valid file formats complying with JSON / JSON Schema rules.
* **Structure (Semantics)**: Conforms to the higher-level specifications (like OpenAPI routes, parameters, and info blocks or Reversed micro-formats) to establish what the data actually represents.

---

!!! tip "Getting Started with Custom Development"
    Ready to write a new loader or map models to another target format? Ensure your custom scripts output standard syntax before applying specific enterprise semantics.
