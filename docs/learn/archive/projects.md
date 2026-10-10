## Projects

Projects are where the key inputs and outputs for the MTT are held. These are:

- **The exported Information Model**. The UML, or other, definition of the information types and relationships that is to be used as the requirements for the generation process. The library.xml file in the figure below.

- **The mtt-config file**. Which defines project-specific configuration information that is required for the MTT to run. For example: which loader to use, which generators are applicable to this  project, any inter-project dependencies, etc.

- **The config folder**. Any project-specific loader or generator configuration. If many projects use common configuration files then these can be defined once and referenced from many projects mtt-config files.

- **The generated folder**. Where the generated files are written. Each projects mtt-config can define a different folder structure if needed. The MTT will create the folder structure as specified in the mtt-config file so does not need to be created manually.

- **Other files and folders**. The files and folders discussed above are either required or generated. However, other files and folders can be stored in the same repository.  As shown below, the Sparx EA published html filles are stored in the model folder [Library model](https://mtt.apigeneration.tech/repo-static/library/model/index.htm) and the generated markdown files are run through the [MkDocs](https://squidfunk.github.io/mkdocs-material/) tool to generate a complete model documentation website [Library documentation](https://mtt.apigeneration.tech/repo-static/library/site/index.html)


<div class=" text-center">
<figure class="figure ">
  <img class="p-2 border border-dark" src="/static/assets/learn/project-folder-structure.png" alt="Project Folder Structure" width="400"/>
  <figcaption class="figure-caption"><span class="lead">Project Folder Structure</span></figcaption>
</figure>
</div>

This file structure and file contents are the same whether the project is hosted on GitHub or locally.

### Local Projects

Local projects can be stored anywhere on a file system but it is recommended that a simple structure, similar to GitHub, is used with a repo-base folder and all MTT projects located under that. Unlike with GitHub repositories, maintaining version control through Git or similar, is a manual process and not managed by the MTT

### GitHub Projects

MTT has a tight integration with projects stored in GitHub repositories and will manage retrieving the input files and storing and committing and output back to GitHub. Consequently, to run the MTT on a GitHub project requires the user to have a  GitHub account and for the MTT to be registered as a GitHub application by the user/organisation. MTT can also be invoked directly from GitHub, using Actions, as part of a CD/CI workflow.
