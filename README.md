## How it Works

* **Architecture:** Uses **MobileNetV3-Small** via **PyTorch**. The model is a 6MB binary classifier specifically optimized to run on lower end devices or process large amounts of media easily if used on larger scales like checking every image sent in a Discord server for any malicious scams the model specifically trained to detect.

* **Processing:** Images downloaded, resized to **224x224**, and normalized. The network outputs a probability score (0-100%) based on pixel patterns rather than text OCR so it'll be lighter to run on any device for larger production use.

* **Detection:** Specifically trained to identify MrBeast or fake tweet phishing templates, including photos of fake crypto websites and specific layouts.

* **Contextual Intelligence:** Uses **Hard Negative Mining** to distinguish between raw scam graphics and screenshots of the Discord UI. This ensures it flags actual scams while ignoring users reporting or discussing them.