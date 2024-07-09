from django.http import HttpResponse
from pets.models import Pet
def record(request):
    test1=Pet(name="jack",score='12')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
