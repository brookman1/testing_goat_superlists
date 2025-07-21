# Practice Code for Test-Driven Development with Django
For this project the source material used came from this book: [Test-Driven Developmet with Python](https://www.obeythetestinggoat.com/)

## Some General Notes
### Certain Modification Off Script
From Chapter One onwards certain modifications had to be made,
1. Django version was upgraded to 5.2.3
2. gekodriver install was also modified infavor of later version
3. selenium version 4.33.0 is the one used.
4. Python 3.13.5 got the honor or being used for the venv on windows.
5. Parts with `pip install virtualenvwrapper` and `echo "source virtualenvwrapper.sh" >> ~/.bashrc` had to be forgone in favor of `python -m venv .`
6. Source code modification such as: ...`find_element_by_tag_name(`... change to ...`find_element(By.NAME)`...  These got resolved with the help of Google AI enabled search and StackOverflow.  As well as settings.py differences.
7. Some version of bootstrap worked.

Reasons for this included that Django versoin was indeterminable, certain Python version tries.

### Supporting Tools and Services.
1. Git Bash was very convinient in Windows 11
2. Warp terminal worked with a better color scheme, the windows command prompt while indispensable was in on way usable, the color scheme is impossible to get right.
3. gvim used for code editing, this was not ideal but was very responsive and easy to use.  This allowed numerous spelling errors and various *.swp files once made it into the repo.
4. Replit was used as integration hosting, this allowed to forgo registering a domain name.
5. Some differences in settings.py where resolved with a help os Google AI eneabled search and StackOverflow.

## Setups
### Windows 11
To start codding and testing a Windows install was used.

Make a directory:
```bash
mkdir testing_goat; cd testing_got
```

Choose and install some Python 3.x version, then:
```bash
python3 -m venv .
Scripts/activate
pip install Django selenium # this at first picked the versions that are locked in requirements.txt now.
```

### Replit setup
1. Choose a Django project template 
2. Open a Shell window.
3. Clone the github.com repo into the app
```bash
git clone <repo path>
```
4. Do some directory restructuring:
```bash
cd <local dir>
cp -rf * ..
```
5. `settings.py` changes, found the relit code for domain path:
```python
ALLOWED_HOSTS = os.environ["REPLIT_DOMAINS"].split(',')
CSRF_TRUSTED_ORIGINS = [
    "https://" + domain for domain in os.environ["REPLIT_DOMAINS"].split(',')
]
```
Changed the corresponding config variables to the above ones in ```superlists/settings.py```.

