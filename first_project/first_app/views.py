from django.shortcuts import render
from .forms import UploadImageForm
from .utils import detect_faces


def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.cleaned_data['image']
            image_path = 'images/' + image.name
            with open(image_path, 'wb') as file:
                for chunk in image.chunks():
                    file.write(chunk)
            modified_image_path = detect_faces(image_path)
            context = {
                'modified_image_path': modified_image_path
            }
            return render(request, 'result.html', context)
    else:
        form = UploadImageForm()
    context = {'form': form}
    return render(request, 'upload.html', context)
