# m03_project
## Quick Start
1. First, clone the repository
2. Next, install dependencies by running: `python3 -m pip install requirements.txt`
	- Note that your IDE may just do this for you
3. Begin all migrations by running `python3 manage.py migrate`
4. Finally, to run run the server run `python3 manage.py runserver`

Currently, the server only has two functional pages, **/auth/register** and **/auth/login**. The code for those two pages is in the **/authentication** directory, and the interesting files are **views.py**, **forms.py** and **urls.py**. All of the current (ugly but minimal) UI code can be found in **authentication/templates/**. There's currently no JS or CSS used, just a very simple website designed to be able to interact with the server.
