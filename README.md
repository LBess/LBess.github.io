# Click [here](https://lbess.github.io) to see my portfolio

Made with the [Personal Web](https://github.com/bjacquemet/personal-web) theme for [Hugo](https://gohugo.io/hugo-pipes/scss-sass/)

### Building and Deploying

* The Github actions are set up such that all you have to do is push the hugo project to the remote repository without building it. A Github action is in place
to build the project to the `pages` branch, which is then deployed to the website. Note: A webscraper action is in place which regularly updates the remote repository,
so you will either need to pull these changes or just ignore them on a new push via `git push -f`.
* If not using Github actions to build, run `hugo` to build and save the changes in `public/`, otherwise the Github-page won't be updated.
* The website can be built and run locally via `hugo server`
