# Information Models

> *"A picture paints a thousand words."*  
> — Fred R. Barnard

In **Model Transform Tools (MTT)**, an information model serves as the central, output-agnostic source of truth for your business domain. Rather than hand-crafting thousands of lines of API specifications, schema definitions, and static documentation, MTT parses visual domain models and automatically converts them into deterministic technical contracts.

---

## Why Use Information Models?

<div class="grid cards" markdown>

-   **Define Once, Generate Many**

    ---

    Maintain a single domain representation. Generate **OpenAPI**, **GraphQL**, **Protobuf**, **JSON Schema**, and **Markdown** documentation simultaneously from one source model.

-   **Visual Domain Governance**

    ---

    Allow business analysts, enterprise architects, and software engineers to collaborate directly on intuitive diagrams before writing implementation code.

-   **Enforced Architectural Rigor**

    ---

    Centralize enterprise standards, naming conventions, and validation rules in the transform engine to guarantee consistency across all generated artifacts.

-   **Technology Independence**

    ---

    Decouple domain specifications from specific server frameworks or programming languages, giving delivery teams total implementation freedom.

</div>

---

## Core Modeling Elements

MTT parses standard UML constructs exported as XML or XMI files from modeling tools like **Sparx Enterprise Architect (EA)**. The transform engine maps four primary building blocks into its canonical internal format:

### 1. Classes & Domain Entities
Classes represent core business entities (e.g., `Borrower`, `Book`, `Property`, `Account`). Each class provides the structural definition for generated REST endpoints, GraphQL object types, or database schemas.

### 2. Attributes & Data Types
Attributes define the properties of a class. MTT resolves attribute types against primitive data catalogs (such as `Core Types` for `Integer`, `Float`, `String`, `UUID`, and `URI`) to ensure consistent data serialization across all target specifications.

### 3. Entity Relationships
MTT preserves complex structural semantics across entity associations:

* **Composition & Aggregation:** Represents parent-child ownership hierarchies (e.g., a `Library` containing `Loans`).
* **Specialization (Inheritance):** Defines class hierarchies and subtype polymorphism (e.g., `AdultBorrower` inheriting base properties from `Borrower`).
* **Association Classes:** Attaches attributes and metadata directly to an association link (e.g., recording start and end dates on a `PropertyOwnership` relationship).
* **Reflexive Associations:** Maps entities that reference instances of their own type (e.g., parent/child category trees or organizational reporting lines).

### 4. Stereotypes & Tagged Values
UML stereotypes and extended tags allow modelers to annotate classes or attributes with technical metadata—such as flagging read-only properties, marking unique identifiers, or defining security classifications.

---

## Transformation Pipeline Mechanics

The transformation process moves through four distinct stages:

=== "1. Visual Modeling"

    ### Domain Design
    Architects design visual UML class diagrams inside standard modeling environments (e.g., Sparx Enterprise Architect).

=== "2. Model Export"

    ### File Generation
    The visual model is exported into an XML/XMI document (e.g., `library.xml`) that captures entity definitions, attributes, and associations.

=== "3. Canonical Parsing"

    ### MTT Internal Model
    MTT ingests the XML export and maps it into an intermediate, output-agnostic canonical representation. This layer normalizes types, resolves cross-project catalog dependencies, and validates structural integrity.

=== "4. Artifact Generation"

    ### Target Outputs
    Active generators consume the canonical metadata layer to produce concrete target files (OpenAPI specifications, GraphQL schemas, Protobuf contracts, and Markdown documentation portals).

---

## Best Practices for Information Modeling

!!! tip "Modeling Guidelines"
    * **Use Standard Primitive Catalogs:** Always import and reference foundational type packages like `Core Types` for standard scalar fields (`String`, `Integer`, `UUID`) rather than creating ad-hoc primitive definitions.
    * **Export from Root Package:** When exporting XMI/XML files, export from the root package node to ensure all child entities, stereotypes, and relationships are included in the output file.
    * **Modularize Shared Sub-Domains:** Separate reusable components (such as `Personal Details` or `Core Types`) into dedicated models so other projects can import them cleanly as catalog dependencies.

---

!!! tip "Next Steps"
    * Review repository file structures in [Project Structure](../projects/).
    * Explore pre-configured sample models in [Example Projects](../example-projects/).
    * Learn how to execute generators in [Running the Tool](../running-mtt/).
