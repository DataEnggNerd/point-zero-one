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
    # Django API
    CountLog.objects.create()
    return {"count":CountLog.objects.count()}
