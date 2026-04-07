# Charlie Brown Detector (A YOLO AI Model)

This YOLO model has been trained to detect [Charlie Brown](https://en.wikipedia.org/wiki/Charlie_Brown), the iconic character from the Peanuts comic strips, across all his visual designs.

The model is based on [YOLO26](https://huggingface.co/Ultralytics/YOLO26) by Ultralytics and was trained locally using a dataset of 61 images covering all of the character's appearances from the 1950s to the 2020s. (Note: This model has not been trained with designs from [Li'l Folks](https://en.wikipedia.org/wiki/Li%27l_Folks).)

## Prerequisites

- [UV](https://docs.astral.sh/uv/) - A fast Python package installer and resolver

## Quick Start

### 1. Install UV

If you don't have UV installed yet, install it with:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

Or visit the [official UV installation guide](https://docs.astral.sh/uv/getting-started/installation/) for other methods.

### 2. Clone the Repository

```bash
git clone https://github.com/ChaconMoon/Charlie-Brown-Detector.git
cd Charlie-Brown-Detector
```

### 3. Install Dependencies

Install all project dependencies using UV:

```bash
uv sync
```

This will create a virtual environment and install all required packages (including `ultralytics`) is a very heavy package, please wait...

### 4. Run the Model

To test the model with your own Peanuts image, edit `main.py` and replace `{Your Peanuts Image Here}` with the path to your image:

```python
result = model.predict(
    source="path/to/your/peanuts/image.jpg",
    show=True,
    stream=True,
)
```

Then run the script:

```bash
uv run python main.py
```

This will:
- Load the trained model from `best_model/charlie-brown-detector.pt`
- Run object detection on your image
- Display the results with bounding boxes
- Save the output to `model_results/` directory

## Project Structure

```
Charlie-Brown-Detector/
├── best_model/              # Trained YOLO model
│   └── charlie-brown-detector.pt
├── dataset/                 # Training dataset
│   └── chralie-brown-detector.ndjson
├── model_results/           # Detection results
│   └── result-*.jpg
├── runs/                    # Training runs and metrics
├── main.py                  # Main inference script
├── pyproject.toml           # Project configuration
├── uv.lock                  # Locked dependencies
└── README.md                # This file
```

## Training

This model was trained with a small dataset containing only 61 images and 92 annotations. The objective was to train a model with the minimum number of images possible and evaluate its precision.

The model achieves approximately 86% precision in most cases. However, when attempting to detect all instances of Charlie Brown in a single image, the precision decreases. This means the model reliably detects around 86% of Charlie Brown instances, but may miss some.

![Precision-Recall Curve](./runs/detect/chaconmoon/charlie-brown-detector/train3/BoxPR_curve.png)

![F1-Confidence Curve](./runs/detect/chaconmoon/charlie-brown-detector/train3/BoxF1_curve.png)

The confusion matrix shows that the model correctly identifies 13 out of 15 cases (87%). The remaining 2 cases were classified as background.

![Confusion Matrix](./runs/detect/chaconmoon/charlie-brown-detector/train3/confusion_matrix.png)

The model exhibits slight overfitting with bounding boxes, meaning it tends to memorize box positions from the training data rather than generalizing well. This is common in small models like this one.

![Results](./runs/detect/chaconmoon/charlie-brown-detector/train3/results.png)

## Results

**All comic strips and episodes were selected randomly.**

In most cases, the detection results are very good. With high-resolution images, the model has no trouble detecting the character, even when multiple instances appear in the same image. Some examples:

### 1950s

This image successfully detects Charlie Brown in 3 instances, but misses one.

<img src="./model_results/result-0.jpg" width=700px/>

In the first two strips, the model confuses Patty with Charlie Brown due to their similar designs.

<img src="./model_results/result-1.jpg" width=700px/>

This strip detects Charlie Brown without issues. This is his first appearance wearing the iconic zig-zag pattern polo, which helps the model recognize him.

<img src="./model_results/result-2.jpg" width=700px/>

### 1960s

This strip detects Charlie Brown in 6 out of 8 cases. For some reason, the model incorrectly identifies a cloud as Charlie Brown.

<img src="./model_results/result-12.jpg" width=700px/>

This strip detects Charlie Brown in 9 out of 10 cases.

<img src="./model_results/result-13.jpg" width=700px/>

This strip achieves perfect detection of Charlie Brown in all instances.

<img src="./model_results/result-14.jpg" width=700px/>

### 1970s-1990s

In this strip, Charlie Brown is only detected once. This likely indicates the need to train the model with a more diverse set of comic gags. The model was primarily trained with images of Charlie Brown throwing a ball (like the first detection here), which explains why only that instance was recognized.

<img src="./model_results/result-15.jpg" width=700px/>

This strip achieves detection in 6 out of 8 cases.

<img src="./model_results/result-16.jpg" width=700px/>

This strip detects Charlie Brown in 2 instances.

<img src="./model_results/result-17.jpg" width=700px/>

### Classic TV Shows

With low-resolution images, the model sometimes misidentifies other characters like Linus or Schroeder as Charlie Brown.

<img src="./model_results/result-18.jpg" width=700px/>

With better resolution, the model works perfectly.

<img src="./model_results/result-19.jpg" width=700px/>

### Modern TV Shows

The modern design of Charlie Brown is detected accurately.

<img src="./model_results/result-20.jpg" width=700px/>

However, it can still be confused with other characters in some cases.

<img src="./model_results/result-21.jpg" width=700px/>

### Other Detections

The model can also detect Charlie Brown plushes and figurines.

<img src="./model_results/result-10.jpg" width=400px/>

<img src="./model_results/result-11.jpg" width=400px/>

## Additional Commands

### Update Dependencies

If `pyproject.toml` has been modified, update your environment:

```bash
uv sync
```

### Run with a Specific Python Version

UV will automatically use the correct Python version specified in `.python-version`. To override:

```bash
uv run --python 3.13 python main.py
```

## License

[Add your license here]

## Acknowledgments

- Ultralytics for YOLO26
- Charles M. Schulz for creating Charlie Brown and Peanuts
