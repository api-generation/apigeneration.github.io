### Generators

Running one or more generators, over an information-model,  to produce output files is the fundamental purpose of the MTT.

#### Existing Generators

There are a number of Generators currently available with the MTT but, as described below, tailoring or developing new generators is often needed for a particular application.

##### API Specification Generators

- **OpenAPI Specifications**. Generates an interface specification that complies to the [OpenAPI standard](https://swagger.io/specification/). 
- **GraphQL Specifications**. Generates an interface specification that complies to the [GraphQL standard](https://graphql.org/). 

##### Schema Definition Generators

- **AOCO (Common Services)**. Generates a set of Micro Format Definition (MGD) documents that conform to the AOCO standard. AOCO is a military standard, primarily used for exchanging information in command and control environments.
- **Reversed**. Generates a set of JSON Schema definitions that conform to the Reversed standard, which the MTT team invented to illustrate the generation of JSON Schema definitions.

##### Markdown Document Generators

- **Information Model documenter**. Generates a set of text documents that conform to the [Markdown standard](hhttps://www.markdownguide.org/basic-syntax/) to document the input information-model. The generated Markdown documents can then be used as documentation on GitHub, for example, or run through tools such as [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) to generate documentation websites.

#### Developing New Generators

As described in [MTT Overview](#mtt-overview), a core design principle of the MTT Internal Model is to make adding new Generators, flexible, quick and easy.

However, creating a new Generator does require some key information to be available as described and illustrated below. The figure aims to bring out two key points, using the OpenAPI and Reversed standards as examples:

1. **Dependencies between standards**. As shown, the OpenAPI standard and the Reversed standard depend on the [JSON Schema Standard](https://json-schema.org/l) and the [JSON Standard](https://www.json.org/json-en.html) for their syntax.
2. **Generators must to conform to all relevant standards**. As shown, both the OpenAPI and Reversed standards depend on the lower-level JSON and JSON-Schema standard, for the format (syntax) of the generated files, but it is the higher-level OpenAPI and Reversed standards that define the structure (semantics) of what the generators must produce. 

<div class="text-center">
    <figure class="figure">
        <img class=" p-2 border border-dark" src="/static/assets/learn/generator-dependencies.png"
             alt="Generator Dependencies" width="800"/>
        <figcaption class="figure-caption"><span class="lead">Generator Dependencies</span></figcaption>
    </figure>
</div>
