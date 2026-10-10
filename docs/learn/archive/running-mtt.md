## Running the MTT

This section describes the various steps in selecting a project, running the chosen generators and viewing the results of the generation process.

### MTT Home page

The MTT Home page consists of two sections, Projects and Learn as shown in the figure and described below.

<div class=" text-center">
<figure class="figure">
  <img class = " p-2 border border-dark" src="/static/assets/learn/home-page.png" alt="The MTT home page" width="900"/>
  <figcaption class="figure-caption"><span class="lead">The MTT home page</span></figcaption>
</figure>
</div>

#### Projects

As described, [Projects](#projects) can be stored in either GitHub or Local repositories. Clicking on either of the 'Select Project' buttons will go to a page that has a drop-down of available MTT projects and a set of checkboxes to allow selection of the generators to be run. As shown in the figure below.

<div class=" text-center">
<figure class="figure ">
  <img class="p-2 border border-dark" src="/static/assets/learn/run-generators.png" alt="Running MTT Generators on a project" width="600"/>
  <figcaption class="figure-caption"><span class="lead">Running MTT Generators on a project</span></figcaption>
</figure>
</div>
Once the generators have run, one of two pages will be displayed:

- **Arthefacts Summary**. If the automatic validation of the model does not identify any errors (as opposed to warnings) then the selected generators will be run. Once the run is completed, the Artefacts Summary page will be displayed (see the figure below).  This page has two sections:
  - **A Model Summary**. This has drop-downs that show any warnings that have been identified in the model. Warnings should be addressed but are not serious enough to stop the generators from running. There is also a summary of the model provided.
  - **A Generator Summary**. For each generator that has been run, there is a summary of the artefacts that have been generated. Also, there is a means of accessing the generated artefacts. For GitHub projects, this is a hyperlink to the relevant folder. For local projects, because of browser security restrictions, rather than a link to there is an absolute path to the folder. This can be copied and pasted into a file browser to access the generated files.
- **Error page**. If the model validated has identified errors, that would cause the generators to fail, then the errors are displayed. Errors must be fixed before the MTT can be successfully run. These errors are often caused by missing dependencies or model sub-folders (rather than the model root folder) being chosen during export from the modelling tool.

<div class=" text-center">
<figure class="figure">
  <img class="p-2 border border-dark" src="/static/assets/learn/artefacts-summary.png" alt="Summary of a generate run " width="900"/>
  <figcaption class="lead figure-caption"><span class="lead">Summary of a generate run</span></figcaption>
</figure>
</div>


#### Learn

Currently just this page, though this will be expanded to provide training on developing models suitable for use in generating valid and complete outputs.
