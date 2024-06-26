import os

import torch
import torch.optim as optim
import torchvision.transforms as transforms
from get_loader import get_loader
from model import ImageCaptioningModel
from utils import load_checkpoint, print_examples


def test_model():
    transform = transforms.Compose(
        [
            transforms.Resize((299, 299)),
            transforms.ToTensor(),
            transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5)),
        ]
    )

    train_loader, dataset = get_loader(
        root_folder="asset/flickr8k",
        annotation_file="flickr8k_annotations/Flickr8k.token.txt",
        transform=transform,
        num_workers=2,
    )

    torch.backends.cudnn.benchmark = True
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    load_model = True
    train_cnn = True

    # Hyperparameters
    embed_size = 256
    hidden_size = 256
    vocab_size = len(dataset.vocab)
    num_layers = 1
    learning_rate = 3e-4
    num_epochs = 100

    # initialize model, loss etc
    model = ImageCaptioningModel(embed_size, hidden_size, vocab_size, num_layers).to(device)
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)

    # Only finetune the CNN
    for name, param in model.encoderCNN.inception.named_parameters():
        if "fc.weight" in name or "fc.bias" in name:
            param.requires_grad = True
        else:
            param.requires_grad = train_cnn

    if load_model:
        step = load_checkpoint(torch.load("checkpoint.pth.tar", map_location=torch.device('cpu')), model, optimizer)
    model.eval()

    print_examples(model, device, dataset)
    
test_model()
