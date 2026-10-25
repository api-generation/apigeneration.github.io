# Information Models

> *"A picture paints a thousand words."*  
> — Fred R. Barnard[cite: 9]

In **Model Transform Tools (MTT)**, an information model serves as the central, output-agnostic source of truth for your business domain[cite: 8, 9]. Rather than hand-crafting thousands of lines of API specifications, schema definitions, and static documentation, MTT parses visual domain models and automatically converts them into deterministic technical contracts[cite: 8, 9].

---

## Why Use Information Models?

<div class="grid cards" markdown>

-   **Define Once, Generate Many**

    ---

    Maintain a single domain representation. Generate **OpenAPI**, **GraphQL**, **Protobuf**, **JSON Schema**, and **Markdown** documentation simultaneously from one source model[cite: 8].

-   **Visual Domain Governance**

    ---

    Allow business analysts, enterprise architects, and software engineers to collaborate directly on intuitive diagrams before writing implementation code[cite: 8].

-   **Enforced Architectural Rigor**

    ---

    Centralize enterprise standards, naming conventions, and validation rules in the transform engine to guarantee consistency across all generated artifacts[cite: 8].

-   **Technology Independence**

    ---

    Decouple domain specifications from specific server frameworks or programming languages, giving delivery teams total implementation freedom[cite: 8].

</div>

---

## Core Modeling Elements

MTT parses standard UML constructs exported as XML or XMI files from modeling tools like **Sparx Enterprise Architect (EA)**[cite: 8]. The transform engine maps four primary building blocks into its canonical internal format:

### 1. Classes & Domain Entities
Classes represent core business entities (e.g., `Borrower`, `Book`, `Property`, `Account`)[cite: 8]. Each class provides the structural definition for generated REST endpoints, GraphQL object types, or database schemas[cite: 8].

### 2. Attributes & Data Types
Attributes define the properties of a class. MTT resolves attribute types against primitive data catalogs (such as `Core Types` for `Integer`, `Float`, `String`, `UUID`, and `URI`) to ensure consistent data serialization across all target specifications[cite: 8].

### 3. Entity Relationships
MTT preserves complex structural semantics across entity associations:

* **Composition & Aggregation:** Represents parent-child ownership hierarchies (e.g., a `Library` containing `Loans`)[cite: 8].
* **Specialization (Inheritance):** Defines class hierarchies and subtype polymorphism (e.g., `AdultBorrower` inheriting base properties from `Borrower`)[cite: 8].
* **Association Classes:** Attaches attributes and metadata directly to an association link (e.g., recording start and end dates on a `PropertyOwnership` relationship)[cite: 8].
* **Reflexive Associations:** Maps entities that reference instances of their own type (e.g., parent/child category trees or organizational reporting lines)[cite: 8].

### 4. Stereotypes & Tagged Values
UML stereotypes and extended tags allow modelers to annotate classes or attributes with technical metadata—such as flagging read-only properties, marking unique identifiers, or defining security classifications[cite: 8].

---

## Transformation Pipeline Mechanics

The transformation process moves through four distinct stages:

=== "1. Visual Modeling"

    ### Domain Design
    Architects design visual UML class diagrams inside standard modeling environments (e.g., Sparx Enterprise Architect)[cite: 8].

=== "2. Model Export"

    ### File Generation
    The visual model is exported into an XML/XMI document (e.g., `library.xml`) that captures entity definitions, attributes, and associations[cite: 8].

=== "3. Canonical Parsing"

    ### MTT Internal Model
    MTT ingests the XML export and maps it into an intermediate, output-agnostic canonical representation[cite: 8]. This layer normalizes types, resolves cross-project catalog dependencies, and validates structural integrity[cite: 8].

=== "4. Artifact Generation"

    ### Target Outputs
    Active generators consume the canonical metadata layer to produce concrete target files (OpenAPI specifications, GraphQL schemas, Protobuf contracts, and Markdown documentation portals)[cite: 8].

---

## Best Practices for Information Modeling

!!! tip "Modeling Guidelines"
    * **Use Standard Primitive Catalogs:** Always import and reference foundational type packages like `Core Types` for standard scalar fields (`String`, `Integer`, `UUID`) rather than creating ad-hoc primitive definitions[cite: 8].
    * **Export from Root Package:** When exporting XMI/XML files, export from the root package node to ensure all child entities, stereotypes, and relationships are included in the output file[cite: 8].
    * **Modularize Shared Sub-Domains:** Separate reusable components (such as `Personal Details` or `Core Types`) into dedicated models so other projects can import them cleanly as catalog dependencies[cite: 8].

---

!!! tip "Next Steps"
    * Review repository file structures in [Project Structure](../projects/)[cite: 8].
    * Explore pre-configured sample models in [Example Projects](../example-projects/)[cite: 8].
    * Learn how to execute generators in [Running the Tool](../running-mtt/)[cite: 8, 10].
