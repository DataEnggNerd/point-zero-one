# NanoDjango, Django on diet
> Sep 29, 2024; Reference: Awesome Python weekly, Issue 435; https://simonwillison.net/2024/Sep/24/nanodjango/

Django is a batteries included framework for Web development in Python. There is no way you can make an API up and running with code less than 100 lines, like what you can achieve in `Flask` or `FastAPI`. 

Apparently, not anymore. At DjangoCon US 2024, [Richard Terry](https://github.com/radiac) has presented his lightning talk on `NanoDjango`, which is the lighter version of Django. 

You can install NanoDjango with `pip install nanodjango`.

And the code for creating a lightweight API looks something like this,

## Sample code

```py title="counter.py"
from django.db import models
from nanodjango import Django

app = Django()

@app.admin
class CountLog(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)

@app.route("/")
def count(request):
    # View
    CountLog.objects.create()
    return f"Number of requests => {CountLog.objects.count()}"

@app.api.get("/add")
def add_counter(request):
    # Django Ninja API
    CountLog.objects.create()
    return {"count":CountLog.objects.count()}

if __name__ == "__main__":
    app.run()
```

Now, run with `nanodjango run counter.py`, Voila :dizzy:

Seems very `Flask` and `FastAPI` like syntax. People like me who started with FastAPI, might find this very comfortable to start with. 

## Interesting things
- 
    - Best part for me is, you can convert this into a full on django project. 
        ```console
        nanodjango convert counter.py /path/to/site --name=test-app # not tested
        ```
    - [DjangoNinja](https://django-ninja.dev) has been used internally for APIs
    - When I installed, I saw `PyDantic` is also a dependency, but couldn't figure out how it is being used in the project. 
  

This is very nice version of Django, which will be a preference for beignners to start with IMO. Hoping to see more. Starred right away! :star: