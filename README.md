# PageRecommender
Chrome extension and Django app for recommending articles based on previously tagged articles.

## Setup

### Chrome Extension
To add the Chrome Extension:

1.  Navigate to `chrome://extensions/`
2.  Check the "Developer mode" box
3.  Drag and drop the `chrome_extension` directory onto this page

### Django App
To start the app, run `python PageRecommender/web_app/manage.py runserver 8000`

This should be the default run command when using [PyCharm](https://www.jetbrains.com/pycharm/) with `PageRecommender/web_app` as the project root.
