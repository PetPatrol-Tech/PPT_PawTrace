from django.http import HttpResponse
from Pets.models import Pet
def record(request):
    test1 = Pet(pet_name="jack", pet_age=12, pet_category="Dog", resident_id=1)  # 确保 resident_id 是有效的
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
