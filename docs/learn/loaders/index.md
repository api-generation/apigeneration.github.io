# Model Loaders

Model Loaders serve as the entry point for the **Model Transform Tools (MTT)** transformation pipeline. They ingest raw domain export files created in graphical modeling platforms—such as UML class diagrams exported in XML or XMI format—and translate them into the intermediate **MTT Internal Canonical Model**.

---

## Role & Key Functions

By decoupling raw modeling file formats from downstream generators, Loaders ensure that MTT remains completely vendor-agnostic. As long as a Loader exists for a given export format, MTT can parse its structure and produce identical, deterministic specification outputs regardless of the underlying modeling tool.

<div class="grid cards" markdown>

-   **Canonical Metadata Mapping**

    ---

    Translates tool-specific UML representations (such as Sparx EA XMI tags) into output-agnostic intermediate metadata objects.

-   **Dependency Resolution**

    ---

    Parses inter-model catalog references across packages and shared libraries (e.g., mapping primitive scalar types from `Core Types` into domain entities).

-   **Pre-Flight Validation**

    ---

    Inspects class hierarchies, association multiplicities, and required attributes prior to generation, surfacing warnings or errors before running generators.

-   **Modular Architecture**

    ---

    Allows enterprise teams to write custom loaders for alternate UML tools or proprietary data formats without modifying active output generators.

</div>

---

## Model Ingestion Pipeline

The loader process executes in four distinct phases:

1. **Source Ingestion:** Reads the exported XML/XMI file (e.g., `library.xml`) from the project root or specified directory path.
2. **Package & Entity Parsing:** Extracts classes, attributes, associations, compositions, inheritance links, tagged values, and stereotypes.
3. **Catalog & Type Binding:** Resolves primitive datatypes and external references against declared dependency catalogs (such as `core-types` and `personal-details`).
4. **Canonical Model Emission:** Emits a validated `InternalModel` object graph consumed by active generators.

---

## Supported & Custom Loaders

=== "Sparx Enterprise Architect Loader"

    ### Built-in XML Ingester
    The default loader shipped with MTT is optimized for **Sparx Enterprise Architect (EA)** XML and XMI exports.

    * **Supported Input:** Standard UML XML export files (e.g., `library.xml`).
    * **Parsed Constructs:** Classes, primitive and complex attributes, associations, compositions, generalizations (inheritance), association classes, tagged values, and stereotypes.
    * **Type Mapping:** Automatically binds native UML primitives to MTT standard scalar types.

=== "Developing Custom Loaders"

    ### Extending for Other Tools
    To ingest models from other platforms (e.g., StarUML, MagicDraw, or custom JSON/YAML schemas), you can implement a custom Loader module:

    * **Implementation:** Map source schema objects directly to the canonical MTT `InternalModel` interface.
    * **Registration:** Declare your custom loader package name and target file path inside `mtt-config.yaml`.

---
