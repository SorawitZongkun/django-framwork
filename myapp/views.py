from django.shortcuts import render, redirect
from django.http import HttpResponse
from myapp.models import Person
from django.contrib import messages

# Create your views here.


def index(request):
    # return HttpResponse('OMG')
    all_person = Person.objects.all()
    # all_person = Person.objects.filter(age=25)
    return render(request, 'index.html', {"all_person": all_person})


def about(request):
    return render(request, 'about.html')


def form(request):
    if request.method == "POST":
        # รับข้อมูล
        name = request.POST['name']
        age = request.POST['age']
        print(name, age)

        # บันทึกข้อมูล
        person = Person.objects.create(
            name = name,
            age = age
        )
        person.save()
        messages.success(request, "บันทึกข้อมูลเรียบร้อยแล้ว")

        # เปลี่ยนเส้นทาง
        return redirect("/")
    else:
        return render(request, 'form.html')
    
def edit(request, person_id):
    if request.method == "POST":
        name = request.POST['name']
        age = request.POST['age']

        person = Person.objects.get(id=person_id)
        person.name = name
        person.age = age
        person.save()
        messages.success(request, "อัพเดทข้อมูลเรียบร้อยแล้ว")

        # เปลี่ยนเส้นทาง
        return redirect("/")
    else:
        # ดึงข้อมูลประชากรที่ต้องการแก้ไข
        person = Person.objects.get(id=person_id)
        return render(request, "edit.html", {"person": person})
