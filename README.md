# python-tutorial

## Requirements
- python 3
- github account + git
- heroku account
- PyCharm

## How to start development
1. Clone project, you should use PyCharm, following this [instruction](https://www.jetbrains.com/help/pycharm/set-up-a-git-repository.html#clone-repo)
2. Run app.py, preferable from IDE `Shift + F10`
3. Go to `http://127.0.0.1:5000/` and check result

## How to run application on heroku
1. Login to heroku
2. Create new app, fill in the `App name`, and choose closest region
3. Now go to Deploy and select `GitHub` as a deployment method
4. Connect to GitHub
5. Choose this repository from list
6. Enable Automatic Deploys
7. Select branch
8. Click Deploy
9. To check app online click Open App

## How to add new module
Each module are similar, when creating a new module, it's best to take a look at `new_module` package
1. Copy `new_module` package, and name the new module
2. Replace all occurrences of `new_module` with new module name
3. Rename template file to new module name
4. Register new module in `createApp` method
```python
    from application.new_module_name import new_module_name
    app.register_blueprint(new_module_name)
``` 
5. Add link to new module in `base.html`
```html
    <a href="/new_module_name">New module name</a>
```

## Github
### Must have
https://www.jetbrains.com/help/idea/sync-with-a-remote-repository.html
https://www.jetbrains.com/help/idea/commit-and-push-changes.html
https://www.jetbrains.com/help/idea/manage-branches.html

### Later
https://www.jetbrains.com/help/idea/apply-changes-from-one-branch-to-another.html
https://www.jetbrains.com/help/idea/resolve-conflicts.html