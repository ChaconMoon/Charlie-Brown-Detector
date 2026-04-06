import pathlib

from ultralytics import YOLO

model = YOLO(model="./best_model/charlie-brown-detector.pt")

result = model.predict(
    source="19501230.webp",
    show=True,
    stream=True,
)

for i, r in enumerate(result):
    current_index = i

    while pathlib.Path(f"./model_results/result-{current_index}.jpg").exists():
        current_index += 1

    r.save(f"./model_results/result-{current_index}.jpg")
