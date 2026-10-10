

# Model Transform Tools

Exposing APIs (Application Programming Interfaces) for your business services offers **significant strategic, operational, and technical benefits**. API Generation's Model Transform Tools (MTT) is a means to significantly reduce costs and improve quality by generating these APIs and other outputs.

It achieves this by taking a model driven approach that provides the following benefits:

- **Define once, generate many:** Defining the business information in a structured but output agnostic model allows the generation of many outputs. The most common outputs are API specifications, such as OpenAPI, GraphQL and Protobuf. However, there are many other possibilities such as documentation using MkDocs, custom data standards, etc.
- **Improve efficiency:** The define-once, generate-many principle means that, by only having to invest in producing and maintaining the information models, API and other development costs and times can be significantly reduced.
- **Incorporate best practice:** The generators incorporate best practice and any local standards. Defining and implementing these rules is done once; resulting in rigour and consistency  across all the generated artefacts.
- **Democratise the development process:** The use of standard UML diagrams, which are quick to learn how to read, enable a wide set of skills and experience to be involved in the model's development and review. This leads to more robust and enduring models and hence generated outputs.
- **Provide technology independence:** By using a model to generating specifications, rather than code, allows greater freedom to choose the technology to implement APIs, etc. For example, there are many open-source tools that take an API specification as input and generate implementation code in a particular programming language or framework.

The following sections provide details on how the MTT is used to achieves these benefits.

### Projects

Projects are where the MTT's input and output files are held, as shown in the figure below. This figure also shows the tool's structure which is useful for providing context to some of the other sections below.

<div class=" text-center">
<figure class="figure">
  <img class = "p-2 border border-dark" src="/static/assets/learn/mtt-overview-2.png" alt="The MTT structure and process" width="800"/>
  <figcaption class="figure-caption"><span class="lead">The MTT structure and process</span></figcaption>
</figure>
</div>


 The key files and folders are:

- **The Information Model:**. This graphical model of the information types and their relationships is used as the main input to the generation process.  UML class models are the default but other formats, such as Resource Descriptor Framework (RDF) are possible. Where necessary, the models can be enriched with tags that provide finer control over what gets generated.
- **Config files:** These define project, loader and generator specific configuration information that is required for the MTT to run. For example: which loader to use, which generators are applicable to this project, any inter-project dependencies, etc.
- **Generated outputs:** Where the generated files are written to. Each project can define a different folder structure if needed. The MTT will create the folder structure as specified in the mtt-config file so does not need to be created manually.

MTT supports two types of project:

- **GitHub Projects**: MTT has a tight integration with projects stored in GitHub repositories and will manage retrieving the input files and storing and committing the outputs back to GitHub. MTT can also be invoked directly from GitHub, using Actions, as part of a CD/CI workflow.
- **Local Projects:** Local projects can be stored anywhere on a file system that MTT has read and write access to. Unlike GitHub repositories, maintaining version control through Git or similar, is a manual process and not managed by the MTT.

Projects can also include dependencies on other projects. This allows a catalogue of models to be developed and reused. For example, many projects could depend on a set of core-types such as : Address, Lat/Long, Name, UUID, etc

See [Projects](/learn/projects) for more details.

### Deployment

The MTT can be run in two ways:

**Web-Service**:  The web-service version of the tool can be run either through the browser user-interface or as a GitHub Action. Integration with GitHub Actions allows the tool to be include as part of development workflows.

**Docker container**: This is ideal where, for business or security reasons, project models and generated artefacts need to be stored locally. In this case the tool can be deployed on local infrastructure as a Docker container.

See [Running the MTT](/learn/running-mtt) for more details.

### Extensibility

The tool's structure and internal information model is designed to allow new generators, for other standards or custom artefacts, to be quickly developed and integrated.
Whilst Sparx Enterprise Architect (EA) is the default UML modelling tool new loaders, for alternative UML & RDF modelling tools, can be easily developed & integrated. The tool's internal model means that all generators will automatically work with any new loaders.

See [Developing New Generators](/learn/new-generators) for more details.
