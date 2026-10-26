# Learn About MTT

> *"A picture paints a thousand words."*  
> — Fred R. Barnard

Learn how to use **Model Transform Tools (MTT)** to generate API specifications, message schemas, and documentation from pictorial representations of your business information.

---

## Getting Started

<div class="grid cards" markdown>

-   :material-information-outline:{ .lg .middle } **MTT Overview**

    ---

    Understand the core architecture, transformation engine concepts, and execution pipeline.

    [:octicons-arrow-right-24: Read Overview](learn/mtt-overview/)

-   :material-folder-outline:{ .lg .middle } **Project Structure**

    ---

    Explore repository layout, configuration files, and source control organization.

    [:octicons-arrow-right-24: Explore Layout](learn/projects/)

-   :material-play-circle-outline:{ .lg .middle } **Running the Tool**

    ---

    Execute transformations locally, via command line, or inside automated GitHub Actions.

    [:octicons-arrow-right-24: View Guide](learn/running-mtt/)

-   :material-auto-fix:{ .lg .middle } **Example Projects**

    ---

    Browse live sample models and their generated OpenAPI specs, GraphQL schemas, and docs.

    [:octicons-arrow-right-24: Browse Examples](learn/example-projects/)

</div>

---

## Technical References

<div class="grid cards" markdown>

-   :material-cube-outline:{ .md .middle } **UML & Models**

    Guidelines for modeling domain entities, attributes, and relationships.

    [View Specs →](learn/models/)

-   :material-file-import-outline:{ .md .middle } **Model Loaders**

    How graphical diagrams are ingested and parsed into internal metadata.

    [View Loaders →](learn/loaders/)

-   :material-cog-outline:{ .md .middle } **Generators**

    Standards for generating OpenAPI 3.0, GraphQL, Protobuf, and Markdown outputs.

    [View Generators →](learn/standard-generators/)

</div>

---

## Frequently Asked Questions

??? question "Why can't I just use Generative AI to design my APIs?"

    While Generative AI can assist in drafting initial snippets, enterprise API generation requires **100% deterministic precision, strict governance, and repeatable standards**.

    * **Zero Hallucinations:** Generative models can introduce subtle field mismatches or non-standard syntax. MTT guarantees exact schema compliance every time.
    * **Single Source of Truth:** Updating a core visual model automatically propagates breaking changes cleanly across OpenAPI, GraphQL, Protobuf, and documentation.
    * **Governance & Compliance:** Architectural rules are built directly into MTT generators rather than relying on prompt engineering.

??? question "How does MTT integrate with existing GitHub repositories?"

    MTT uses standard repository structures for models and configs. You can execute transformations on local file stores or automate artifact generation directly within GitHub Actions pipelines.

[:octicons-question-24: View Full FAQ Page](faq/){ .md-button }

---

---

!!! tip "Ready to run a transformation?"
    Return to the main MTT Manager web application to select your local or remote project and execute transforms.

    [Launch MTT Tool →](https://apigeneration.tech/try-mtt){ .md-button .md-button--primary }
