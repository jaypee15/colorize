import json
import os
import uuid

from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from .models import Generation
import replicate


def generations(request, *args) -> HttpResponse:
    """
    Render all generations.dj runserver
    """
    generations = Generation.objects.all().order_by('-created_at')
    return render(
        request, 'generations.html', {'generations': generations}
    )


def start_generation(request) -> JsonResponse:
    """
    We call this view to start a new generation.
    """
    image_url = request.POST['image_url']

    secret_id = uuid.uuid4()  # We'll use this to prevent people from sending us fake webhooks.
    generation = Generation.objects.create(secret_key=secret_id, before_url=image_url, status="started")

    uri = reverse('complete-generation', kwargs={'secret_key': secret_id})
    webhook_url = f"{os.environ['WEBHOOK_URL']}{uri}"

    replicate_model_id = "piddnad/ddcolor:ca494ba129e44e45f661d6ece83c4c98a9a7c774309beca01429b58fce8aa695"
    replicate.run(
        replicate_model_id,
        input={"image": image_url, "model_size": "large"},
        webhook=webhook_url,
        webhook_events_filter=["completed"],
    )
    return JsonResponse({"generation_id": generation.id}, status=200)


def check_generation(request, generation_id: int) -> JsonResponse:
    """
    We use this to poll the status of the generation, and then update the UI.
    """
    generation = Generation.objects.get(id=generation_id)
    return JsonResponse({"status": generation.status}, status=200)


@csrf_exempt
def complete_generation(request, secret_key: int) -> HttpResponse:
    """
    The external webhook will call this endpoint when the generation is complete.
    """
    if request.method == 'POST':
        webhook_data = json.loads(request.body.decode("utf"))
        print(f'{webhook_data = }')
        output_image_url = webhook_data['output']

        try:
            generation = Generation.objects.get(secret_key=secret_key)
            generation.after_url = output_image_url
            generation.status = 'completed'
            generation.save()
            return HttpResponse(status=200)
        except Generation.DoesNotExist:
            return HttpResponse(status=404)
    else:
        return HttpResponse(status=403)

