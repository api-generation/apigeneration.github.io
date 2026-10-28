# Model Transform Tools (MTT)

> *"A picture paints a thousand words."*  
> — Fred R. Barnard

Exposing APIs for your business services offers significant benefits, but designing them by hand is slow, repetitive, and error-prone. **Model Transform Tools (MTT)** solves these problems by generating deterministic API specifications, schema definitions, and static documentation directly from graphical domain models.

---

## 🎙️ NotebookLM Deep-Dive Audio Overview

Listen to an AI-generated technical podcast overview of the **Model Transform Tools** platform, architecture, and generation capabilities:

!!! info "MTT Architecture & Overview Podcast"

    <audio controls style="width: 100%; margin-top: 8px; border-radius: 8px;">
      <source src="assets/mtt-podcast.mp3" type="audio/mpeg">
      Your browser does not support the audio element.
    </audio>

    *Automatically generated via NotebookLM & GitHub Actions from current site documentation.*

---

## Why Use MTT?

<div class="grid cards" markdown>

-   **Define Once, Generate Many**

    ---

    Generate **OpenAPI**, **GraphQL**, **Protobuf**, **Markdown**, and custom data standards from a single output-agnostic model.

-   **Improve Efficiency**

    ---

    Reduce development costs significantly. For example: The `Library` sample project automatically generates over **7,500 lines** of OpenAPI and **450+ lines** of GraphQL.

-   **Incorporate Best Practice**

    ---

    Implement local standards and enterprise rules once in the transform engine, resulting in architectural rigor and consistency across all generated artifacts.

-   **Democratise Development**

    ---

    Standard UML diagrams allow business analysts, enterprise architects, and domain experts to participate in model reviews before writing server code.

-   **Technology Independence**

    ---

    Generate implementation-agnostic specifications rather than locked-in framework code, giving engineering teams total freedom to choose target languages.

</div>

---

## Key Documentation & Walkthroughs

<div class="grid cards" markdown>

-   **MTT Overview**

    ---

    Learn about the core transformation engine, intermediate model layer, and supported specifications.

    [:octicons-arrow-right-24: Read Overview](learn/mtt-overview/index.md)

-   **Project Structure**

    ---

    Explore repository layouts, configuration files (`mtt-config.yaml`), and output directory structures.

    [:octicons-arrow-right-24: View Project Structure](learn/projects/index.md)

-   **Running the Tool**

    ---

    Step-by-step instructions for running MTT locally via Docker or in the cloud using the MTT GitHub App.

    [:octicons-arrow-right-24: Learn How to Run](learn/running-mtt/index.md)

-   **Example Projects**

    ---

    Browse sample models (`Library`, `Property Ownership`, `Personal Details`, `Core Types`) and generated outputs.

    [:octicons-arrow-right-24: Browse Examples](learn/example-projects/index.md)

</div>

---

## Get Started

<div class="grid cards" markdown>

-   **New to MTT?**

    ---

    Explore our step-by-step walkthrough to see how model transformations convert graphical UML diagrams into production-ready API specifications.

    [:octicons-rocket-24: Try out MTT](try-mtt/index.md){ .md-button .md-button--primary }

</div>
