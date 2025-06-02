from django.shortcuts import render
from .forms import ImageUploadForm
from .utils import classify_image_with_evaluation
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt
import io, base64
from django.shortcuts import render
from .models import UploadedImage

def show_confusion_matrix(request):
    images = UploadedImage.objects.exclude(true_label__isnull=True).exclude(predicted_label__isnull=True)
    if not images:
        return render(request, 'classifier/confusion_matrix.html', {'image_data': None, 'error': "No labeled images yet."})

    y_true = [img.true_label for img in images]
    y_pred = [img.predicted_label for img in images]
    labels = sorted(set(y_true + y_pred))

    cm = confusion_matrix(y_true, y_pred, labels=labels)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=labels)

    fig, ax = plt.subplots(figsize=(8, 6))
    disp.plot(ax=ax, xticks_rotation=45)

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    image_data = base64.b64encode(buf.read()).decode('utf-8')
    buf.close()

    return render(request, 'classifier/confusion_matrix.html', {'image_data': image_data, 'error': None})

def upload_and_classify(request):
    predictions = None
    warning = None
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image_instance = form.save()
            predictions, warning = classify_image_with_evaluation(image_instance.image.path)

            # Save top prediction
            if predictions:
                image_instance.predicted_label = predictions[0]['label']
                image_instance.save()
    else:
        form = ImageUploadForm()

    return render(request, 'classifier/upload.html', {
        'form': form,
        'predictions': predictions,
        'warning': warning
    })