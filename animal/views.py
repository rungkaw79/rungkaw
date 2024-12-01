from django.shortcuts import render, redirect
from django.http import HttpResponse
from animal.models import Animal
from django.contrib import messages

# Create your views here.
def page_a(request):
    # animal_name = "อาม"
    # return HttpResponse()
    return render(request,'page_a.html')


def page_b(request):
    # animal_name = "ปิ่น"
    # return HttpResponse()
    return render(request,'page_b.html')

def page_c(request):
    # animal_name = "เป่าเป้ย"
    # return HttpResponse()
    return render(request,'page_c.html')

def create(request):
    if request.method == "POST":
        base_name = request.POST['base_name']
        scientific_name = request.POST['scientific_name']
        number = request.POST['number']
        point = request.POST['point']
        channel = request.POST['channel']
        print(base_name, scientific_name, number, point, channel)

        animal= Animal.objects.create(
            base_name = base_name,
            scientific_name = scientific_name,
            number = number,
            point = point,
            channel = channel
        )
        animal.save()

        messages.success(request, "เพิ่มข้อมูลเรียบร้อยแล้ว")

        return redirect('/animal')
    else:
        return render(request,'create.html')

def index(request):
    animals = Animal.objects.all()
    return render(request,'index.html',{"animals":animals})

def edit(request, animal_id):
    if request.method == "POST":
        base_name = request.POST['base_name']
        scientific_name = request.POST['scientific_name']
        number = request.POST['number']
        point = request.POST['point']
        channel = request.POST['channel']
        print(base_name, scientific_name, number, point, channel)

        animal = Animal.objects.get(id = animal_id)
        animal.base_name = base_name
        animal.scientific_name = scientific_name
        animal.number = number
        animal.point = point
        animal.channel = channel
        animal.save()

        messages.success(request, "อัปเดตข้อมูลเรียบร้อย")

        return redirect('/animal')


    else:
        animal = Animal.objects.get(id = animal_id)
        return render (request, 'edit.html',{"animal":animal})


def delete(request,animal_id):
    animal = Animal.objects.get(id = animal_id)
    animal.delete()


    messages.success(request, "ลบข้อมูลเรียบร้อย")

    return redirect('/animal')


