import pathlib

from ultralytics import YOLO

model = YOLO(model="./best_model/charlie-brown-detector.pt")

result = model.predict(
    source="aef6aa5f5375a034a6dbfa1e11b54bac51536530f50c8b6f3bb4cc0cd33fd60d._BR-6_AC_SX720_FMjpg_.jpg",
    show=True,
    stream=True,
)

for i, r in enumerate(result):
    current_index = i

    while pathlib.Path(f"./model_results/result-{current_index}.jpg").exists():
        current_index += 1

    r.save(f"./model_results/result-{current_index}.jpg")
