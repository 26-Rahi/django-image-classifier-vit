from transformers import ViTFeatureExtractor, ViTForImageClassification
from PIL import Image
import torch

# Load model and feature extractor only once
feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')
model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')

def classify_image_with_evaluation(image_path, top_k=3):
    image = Image.open(image_path).convert('RGB')
    inputs = feature_extractor(images=image, return_tensors="pt")
    outputs = model(**inputs)

    logits = outputs.logits
    probs = torch.nn.functional.softmax(logits, dim=-1)  # Convert to probabilities

    top_probs, top_indices = torch.topk(probs, k=top_k, dim=-1)
    top_probs = top_probs[0].tolist()
    top_indices = top_indices[0].tolist()

    top_predictions = [
        {"label": model.config.id2label[idx], "score": round(prob * 100, 2)}
        for idx, prob in zip(top_indices, top_probs)
    ]

    # Add low-confidence warning if needed
    warning = None
    if top_predictions[0]["score"] < 50:
        warning = f"⚠ Warning: Model is unsure. Confidence is only {top_predictions[0]['score']}%."

    return top_predictions, warning