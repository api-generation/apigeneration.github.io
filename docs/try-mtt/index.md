



## Options to try MTT out. A Test

There are two options for seeing what MTT can do for you:

1) Browse the [example projects](/learn/projects)  and the outputs generated from the models. These projects include everything you need to get a feeling for both the information models used as input to the MTT and the range and quality of the generated outputs. 
2) Follow the instructions to enable the MTT as a trial GitHub app. Note you may need to register for an API Generation’s account if you haven’t already got one. This will enable you to run MTT on information models in your own GitHub account & commit the generated outputs  to your GitHub account on a trial basis. The trial models can have a maximum of seven classes, API Generation’s core-types library can be the only dependency and each registered user can run the MTT a maximum of 5 times. To start creating your own model library & generating outputs from it, sign up at GitHub marketplace. 

## Use MTT as a GitHub App

To set up MTT, as a GitHub App, and generate outputs complete the following steps:

### Add MTT as a GitHub App

Follow the <a href="https://github.com/apps/model-transform-tool/installations/new" target="_blank">MTT Installation</a> link to start the GitHub App installation process. 

This starts with a page to choose which GitHub account to install MTT onto. The example below shows both personal and organisation accounts being available.

<div class=" text-center">
<figure class="figure ">
  <img class="p-2 border border-dark" src="assets/github-install-mtt.png" alt="Install MTT onto a GitHub account" width="600"/>
  <figcaption class="figure-caption"><span class="lead">Install MTT onto a GitHub account</span></figcaption>
</figure>
</div>

Selecting an account provides control of which repositories MTT can access and shows which permissions MTT requires. Selecting Install 

<div class=" text-center">
<figure class="figure ">
  <img class="p-2 border border-dark" src="assets/github-install-select-repos.png" alt="Install MTT on GitHub" width="600"/>
  <figcaption class="figure-caption"><span class="lead">Select repositories and permissions</span></figcaption>
</figure>
</div>

If 2FA is enabled on the GitHub account (recommended) then verify that MTT should be allowed access to the repos.

<div class=" text-center">
<figure class="figure ">
  <img class="p-2 border border-dark" src="assets/github-confirm-access.png" alt="Confirm acess to Repos" width="400"/>
  <figcaption class="figure-caption"><span class="lead">Confirm acess to Repos</span></figcaption>
</figure>
</div>

If everything has gone correctly then the final screen summarises the MTT installation and provides options to disable or remove the MTT App.

<div class=" text-center">
<figure class="figure ">
  <img class="p-2 border border-dark" src="assets/github-mtt-installed.png" alt="MTT intalled on GitHub account" width="600"/>
  <figcaption class="figure-caption"><span class="lead">MTT intalled on GitHub account</span></figcaption>
</figure>
</div>

### Run MTT on example project

To run MTT on an example project, in your GitHub repository follow the steps below:

Go to the <a href="https://github.com/API-Generation/library" target="_blank">Library repository</a>. This should display the Library project files.

<div class=" text-center">
<figure class="figure ">
  <img class="p-2 border border-dark" src="assets/library-repository.png" alt="Library example project repo" width="800"/>
  <figcaption class="figure-caption"><span class="lead">Library example project repo</span></figcaption>
</figure>
</div>

Either 'Fork' or download a zip of the library repo. If you've used a download then the files will need to be uploaded to your own repository.

In GitHub, edit the **mtt-config.yaml** file and make the changes shown below and commit the updates.
<div class=" text-center">
<figure class="figure ">
  <img class="p-2 border border-dark" src="assets/edit-mtt-config.png" alt="Edit mtt-config.yaml" width="800"/>
  <figcaption class="figure-caption"><span class="lead">Edit mtt-config.yaml</span></figcaption>
</figure>
</div>

Go to the [MTT home page](https://mtt.apigeneration.tech) which should display the the page below.
<div class=" text-center">
<figure class="figure ">
  <img class="p-2 border border-dark" src="assets/mtt-home.png" alt="Library example project repo" width="800"/>
  <figcaption class="figure-caption"><span class="lead">MTT Home page</span></figcaption>
</figure>
</div>
Click on 'Select Project' under GitHub Projects and it should show the page below.

<div class=" text-center">
<figure class="figure ">
  <img class="p-2 border border-dark" src="assets/mtt-github-projects.png" alt="Select project and generators" width="800"/>
  <figcaption class="figure-caption"><span class="lead">Select project and generators</span></figcaption>
</figure>
</div>

Check the generators you want to run and once the MTT generators have completed a run summary page should be displayed with links to the outputs committed to GitHub.

**Note:** If you check MKDocs then a large number of files are generated and written to GitHub. This can take several minutes so please be patient; it's saving you a lot of work.

