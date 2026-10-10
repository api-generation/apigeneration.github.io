## MTT Overview

This section gives an overview of the MTT to put the overall process into context. The figure below shows the key components:

- **Model loaders**. The default modelling tool is Sparx EA and the provided loader for its exported XML format. Any modelling tool that can export an information-model can be used and loaded into the MTT internal model, via a custom model loader. 
- **Internal model**. The internal model provides the secret-sauce that enables two key aspects which separate the MTT from traditional code generators:
  - Generators can be easily developed, using a range of widely-used programming languages and approaches.
  - Supports dependencies between information models, allowing a catalogue of models to be developed and re-used across projects. 
- **Output generators**. Rather than developing models of a particular API or message standard, The MTT works on business information models that are agnostic to the output formats. It is the generators that provide the intelligent mapping from model to specific output. It is this approach that also enables relevant design best-practice and any house standards to be built into the generators.

<div class=" text-center">
<figure class="figure">
  <img class = "p-2 border border-dark" src="/static/assets/learn/mtt-overview.png" alt="The MTT structure and process" width="600"/>
  <figcaption class="figure-caption"><span class="lead">The MTT structure and process</span></figcaption>
</figure>
</div>

### Deployment

The MTT can be run either:

- Using the web service [API Generation MTT](https://mtt.apigeneration.tech), for GitHub based projects (or running the [example projects](#example-projects)). In this case it can also be integrated with GitHub Actions as part of CD/CI workflow.
- On local infrastructure, as a Docker container.  In this case the MTT requires read/write access to  project repositories that are mapped as Docker Volumes.

