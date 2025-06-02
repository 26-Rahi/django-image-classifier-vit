# django-image-classifier-vit
# Django Image Classifier with Vision Transformer (ViT)

This is a Django web application that uses a Hugging Face Vision Transformer model (google/vit-base-patch16-224) to classify uploaded images. It also includes an evaluation system with a *confusion matrix* to visualize model performance.

---

# Features

- Upload any image (JPG, PNG, etc.)
- Automatically classifies the image using google/vit-base-patch16-224
- Stores predictions in the database
- Allows setting the *true label* (ground truth)
- Displays a *confusion matrix* using scikit-learn and matplotlib


# Example Use Case

Upload an image like a dog, car, tree, etc.  
Get a prediction like "Labrador retriever" or "sports car".

Admin can manually label the image with the true class.  
