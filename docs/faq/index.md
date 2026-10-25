# Frequently Asked Questions (FAQ)

Find answers to common questions about **Model Transform Tools (MTT)**, supported information modeling formats, generator capabilities, deployment options, and troubleshooting.

---

## General Concepts

??? question "What is Model Transform Tools (MTT)?"
    MTT is an enterprise transform engine that ingests pictorial domain information models (such as UML) and automatically generates deterministic API specifications (OpenAPI, GraphQL), message schemas (Protobuf, JSON Schema), and static technical documentation (MkDocs).

??? question "What input modeling tools are supported?"
    MTT natively supports **Sparx Enterprise Architect (EA)** via exported XML/XMI model files (`library.xml`). Because MTT uses an output-agnostic internal model metadata layer, custom model loaders can easily be written to ingest models from other structured modeling platforms.

??? question "What output specifications can MTT generate out of the box?"
    MTT includes pre-built generators for:

    * **API Specifications:** OpenAPI 3.0+ (RESTful JSON/YAML) and GraphQL schemas.
    * **Data Schemas:** Protobuf definitions, AOCO Micro Format MGD documents, and Reversed JSON Schema definitions.
    * **Documentation:** Complete Markdown documentation suites ready for rendering via Material for MkDocs.

??? question "Why generate specifications from visual models instead of writing code directly?"
    Designing specifications visually provides significant advantages:

    * **Define Once, Generate Many:** A single domain model produces consistent OpenAPI, GraphQL, and Protobuf specs without duplicating effort.
    * **Architectural Consistency:** Enterprise rules and naming conventions are enforced centrally inside the generators.
    * **Skill Inclusivity:** Domain experts, business analysts, and architects can review visual UML diagrams before any code is written.
    * **Framework Independence:** You generate standard contracts rather than locked-in server code, giving implementation teams complete language freedom.

---

## Deployment & Security

??? question "What is the difference between GitHub Projects and Local Projects?"
    * **GitHub Projects:** Integrated directly with GitHub web services and workflows. MTT automatically fetches input models from target repositories and commits generated specifications back to specified branches.
    * **Local Projects:** Run entirely on your local machine or internal network via the official MTT Docker container. All model parsing and artifact generation happen on-premises without transferring data off your local environment.

??? question "Is my domain model data secure when using MTT?"
    Yes. When running locally via Docker, model files never leave your file system. When using the managed cloud web instance, MTT operates on your explicitly authorized GitHub repositories using secure OAuth application permissions.

??? question "Can MTT be integrated into automated CI/CD pipelines?"
    Yes. MTT includes native support for **GitHub Actions**. You can configure workflows to automatically re-trigger transformation pipelines, validate domain models, and publish versioned API artifacts whenever changes are committed or merged.

---

## Models & Dependencies

??? question "How does MTT handle dependencies between multiple projects?"
    MTT resolves inter-project catalog dependencies automatically during execution. For example, a high-level application model (such as `Library`) can reference shared entity packages (such as `Personal Details`) and primitive data catalogs (such as `Core Types`). As long as dependency paths are defined in your `mtt-config.yaml` file, MTT imports and links them at runtime.

??? question "Where are generated files stored in my project repository?"
    By default, generated artifacts are written to the `generated/` folder within your project repository directory. You can customize output directory paths and file structure rules inside your project's `mtt-config.yaml` configuration file.

---

## Troubleshooting & Validation

??? question "Why did my generation run fail with a validation error?"
    MTT validates information models before running generators. Common causes for validation failures include:

    * **Missing Catalog Dependencies:** The model references external types or shared packages that are not present in the workspace directory or `mtt-config.yaml`.
    * **Nested Package Export:** Exporting a child sub-folder from Sparx EA instead of the root package wrapper.
    * **Unresolved Data Types:** Using custom attribute types that have not been mapped to a primitive in `Core Types`.

??? question "What should I do if I see validation warnings on the Artefacts Summary page?"
    Validation warnings highlight non-critical issues (such as unpopulated descriptions or unused entity relationships). **Warnings will not stop the generators from running**, but addressing them ensures your generated API contracts and documentation sites are complete.

??? question "How do I access generated files when running MTT locally?"
    Due to browser security restrictions, the MTT web interface displays the **absolute local file path** to your output directory instead of a clickable browser hyperlink. Copy and paste the displayed directory path into your operating system's file explorer to open the output files.

---

## Customization & Extension

??? question "Can I create custom generators for our internal corporate standards?"
    Yes. Adding a new generator is straightforward because MTT decouples model parsing from output generation. Custom generators can be written in standard programming languages to consume the MTT internal metadata model and produce custom code templates, database DDLs, or proprietary message formats.

??? question "Where can I find sample projects to test drive MTT?"
    Pre-configured example projects (`Library`, `Property Ownership`, `Personal Details`, and `Core Types`) are available in the [Example Projects](../example-projects/) section. You can run these immediately from the project dropdown menu in the MTT Manager interface.

---

!!! tip "Need Further Assistance?"
    * Learn how project configurations are structured in [Project Structure](../projects/).
    * Step through execution workflows in [Running the Tool](../running-mtt/).
