## How to run app:

Firstly, setup virtualenv for app through command:

``` 

virtualenv venv
source venv/bin/activate

```

then install all package by pip:

`pip install -r requirements.txt`


final run app with uwgsi or python command:

`python manage.py runserver`

or

`uwsgi --socket 0.0.0.0:8000 --protocol=http -w wsgi`

or

`./run.sh` 


### Test

to test with dredd please install through command

`npm install -g dredd`


