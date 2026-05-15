import torch
import torch.nn as nn
from torchvision import models, transforms

dev = torch.device("cuda" if torch.cuda.is_available() else "cpu")
PATH = "model/Discord AntiScam Vision.pth"
LABELS = [ "✅ SAFE!!!!", "🚨 SCAM!!!!" ]
def get_model():
    net = models.mobilenet_v3_small(weights=None)
    in_f = net.classifier[ 3 ].in_features
    net.classifier[ 3 ] = nn.Linear(in_f, 2)
    net.load_state_dict(torch.load(PATH, map_location=dev))
    net.to(dev)
    net.eval()
    return net
from PIL import Image
import io
import requests
def predict(url, net):
    try:
        resp = requests.get(url, timeout=10)
        img = Image.open(io.BytesIO(resp.content)).convert('RGB')
        
        tf = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([ 0.485, 0.456, 0.406 ], [ 0.229, 0.224, 0.225 ])
        ])
        x = tf(img).unsqueeze(0).to(dev)
        with torch.no_grad():
            out = net(x)
            probs = torch.nn.functional.softmax(out[ 0 ], dim=0)  
        conf, idx = torch.max(probs, 0)
        return LABELS[ idx ], conf.item() * 100
    except Exception as e:
        return f"error: {e}", 0

if __name__ == "__main__":
    m = get_model()
    
    while True:
        url = input("\nImage url: ").strip()

            
        res, acc = predict(url, m)
        print(f"Result: {res} ({acc:.2f}%)")
