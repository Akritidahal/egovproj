from django.shortcuts import render, redirect
from .models import Citizen
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
# Create your views here.
def index(request):
    try:
        citizen = request.user.citizen
        if citizen.is_verified:
            messages.error(request, "You cant fill up the application")
            return redirect('verified_citizen')
        else:
            messages.error(request, "You cant fill up the application")
            return redirect('response')
    except ObjectDoesNotExist:
        if request.method == "POST":
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            email = request.POST['email']
            dob = request.POST["dob"]
            phone = request.POST["Phone"]
            age = request.POST["Age"]
            father_name = request.POST["fathername"]
            mother_name = request.POST["mothername"]
            husband_name = request.POST["husbandname"]
            grandfather_name = request.POST["grand_father_name"]
            father_citizen_number = request.POST["father_citizenship_number"]
            mother_citizen_number = request.POST["mothercitizenshipnumber"]
            husband_citizen_number = request.POST["husbandcitizenshipnumber"]
            birth_certificate_photo = request.POST["birthcerificatephoto"]
            father_citizenship_photo = request.POST["fathercitizenship"]
            mother_citizenship_photo = request.POST["mothercitizenship"]
            husband_citizenship_photo = request.POST["husbandcitizenship"]
            p_zone = request.POST["Zone"]
            p_district = request.POST["District"]
            p_village = request.POST["Village/Municipality"]
            p_ward = request.POST["Ward no"]
            p_tole = request.POST["Tole"]
            p_house_no = request.POST["House no."]
            t_zone = request.POST["zone1"]
            t_district = request.POST["district1"]
            t_village = request.POST["village1"]
            t_ward = request.POST["ward1"]
            t_tole = request.POST["tole1"]
            t_house_no = request.POST["house1"]

            if request.user.is_authenticated:
                print(request.user.first_name)

                citizen = Citizen(user=request.user,first_name=first_name, last_name=last_name,
                                  email=email, dob=dob,
                                  phone=phone, age=age, father_name=father_name, mother_name=mother_name,
                                  husband_name=husband_name,
                                  grandfather_name=grandfather_name, father_citizen_number=father_citizen_number,
                                  mother_citizen_number=mother_citizen_number,
                                  birth_certificate_photo=birth_certificate_photo,
                husband_citizen_number=husband_citizen_number,
                                  father_citizenship_photo=father_citizenship_photo,
                                  mother_citizenship_photo=mother_citizenship_photo,
                                  husband_citizenship_photo=husband_citizenship_photo,
                                  t_zone=t_zone, t_district=t_district, t_village=t_village, t_ward=t_ward, t_tole=t_tole,
                                  t_house_no=t_house_no, p_zone=p_zone, p_district=p_district, p_village=p_village,
                                  p_ward=p_ward,
                                  p_tole=p_tole, p_house_no=p_house_no)
                citizen.is_submitted = True

                citizen.save()
                if citizen.is_submitted == True:
                    if citizen.is_verified == True:
                        return redirect('verified_citizen')
                    else:
                        return redirect('response')

                else:

                    return redirect('index')
            else:
                message.success(request, "You must login first to submit the form")
                return redirect('login')
        else:
            return render(request, 'pages/index.html')


def response(request):
    return render(request, 'pages/response.html')


def verified_citizen(request):
    citizen=Citizen.objects.get(user=request.user)
    context={
        'citizen': citizen
    }
    return render(request,'pages/verified_citizen.html',context)


def render_pdf_view(request):
    citizen = Citizen.objects.get(user=request.user)
    template_path = 'pages/pdf1.html'
    context = {'citizen':citizen}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response