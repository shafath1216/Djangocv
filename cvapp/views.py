from django.shortcuts import render,redirect
from .models import CV
# Create your views here.
def index(request):

  return render(request,'index.html')



def preview_cv(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        education = request.POST.get('education')
        previous_experience = request.POST.get('previous_experience')
        image = request.FILES.get('image')

        cv = CV(
            name=name,
            address=address,
            education=education,
            previous_experience=previous_experience,
            image=image
        )
        cv.save()

        # Now pass the saved instance to the template
        context = {
            'cv':cv,
        }
        return render(request, 'preview_cv.html', context)

    # fallback if not POST
    return render(request, 'index.html')