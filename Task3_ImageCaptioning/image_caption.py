# Image Caption Generator
# CodSoft AI Internship - Task 3

captions = {
    "dog": [
        "A cute dog is sitting on the grass.",
        "A dog is playing outdoors.",
        "A friendly dog is looking at the camera."
    ],

    "cat": [
        "A cat is resting peacefully.",
        "A cute cat is sitting on a chair.",
        "A cat is looking curiously at the camera."
    ],

    "car": [
        "A car is parked on the road.",
        "A modern car is moving on the street.",
        "A shiny car is standing near a building."
    ],

    "flower": [
        "A beautiful flower is blooming.",
        "Colorful flowers are growing in the garden.",
        "A flower is shining in the sunlight."
    ],

    "mountain": [
        "A scenic mountain view under the blue sky.",
        "Snow-covered mountains are visible.",
        "A beautiful mountain landscape can be seen."
    ]
}

print("=" * 50)
print("        IMAGE CAPTION GENERATOR")
print("=" * 50)

print("\nAvailable Objects:")

for item in captions:
    print("-", item)

choice = input("\nEnter object name: ").lower()

if choice in captions:

    import random

    caption = random.choice(captions[choice])

    print("\nGenerated Caption:")
    print(caption)

else:
    print("\nObject not found.")