from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image

print("Loading AI model...")

processor = BlipProcessor.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

model = BlipForConditionalGeneration.from_pretrained(
    "Salesforce/blip-image-captioning-base"
)

print("Model loaded successfully!")

image = Image.open("test.jpg").convert("RGB")

inputs = processor(image, return_tensors="pt")

output = model.generate(**inputs)

caption = processor.decode(output[0], skip_special_tokens=True)

print("\nGenerated Caption:")
print(caption)