import torch
import argparse
import torch.nn as nn
import torch.optim as optim
import time
from tqdm.auto import tqdm
from model import load_model
from datasets import download_dataset, crop_dataset, get_datasets, get_data_loaders
from utils import save_model, save_plots

DEVICE = ('cuda' if torch.cuda.is_available() else 'cpu')

# Construct the argument parser
parser = argparse.ArgumentParser()
parser.add_argument(
    '-e', '--epochs', type=int, default=5,
    help='Number of epochs to train our network for'
)
parser.add_argument(
    '-lr', '--learning-rate', type=float,
    dest='learning_rate', default=0.001,
    help='Learning rate for training the model'
)
args = vars(parser.parse_args())

# Training function.
def train(model, trainloader, optimizer, criterion):
    model.train()
    print('Training')
    train_running_loss = 0.0
    train_running_correct = 0
    counter = 0
    for i, data in tqdm(enumerate(trainloader), total=len(trainloader)):
        counter += 1
        image, labels = data
        image = image.to(DEVICE)
        labels = labels.to(DEVICE)
        optimizer.zero_grad()
        # Forward pass.
        outputs = model(image)
        # Calculate the loss.
        loss = criterion(outputs, labels)
        train_running_loss += loss.item()
        # Calculate the accuracy.
        _, preds = torch.max(outputs.data, 1)
        train_running_correct += (preds == labels).sum().item()
        # Backpropagation.
        loss.backward()
        # Update the weights.
        optimizer.step()
    
    # Loss and accuracy for the complete epoch.
    epoch_loss = train_running_loss / counter
    epoch_acc = 100. * (train_running_correct / len(trainloader.dataset))
    return epoch_loss, epoch_acc 

# Validation function.
def validate(model, testloader, criterion, class_names):
    model.eval()
    print('Validation')
    valid_running_loss = 0.0
    valid_running_correct = 0
    counter = 0
    with torch.no_grad():
        for i, data in tqdm(enumerate(testloader), total=len(testloader)):
            counter += 1
            
            image, labels = data
            image = image.to(DEVICE)
            labels = labels.to(DEVICE)
            # Forward pass.
            outputs = model(image)
            # Calculate the loss.
            loss = criterion(outputs, labels)
            valid_running_loss += loss.item()
            # Calculate the accuracy.
            _, preds = torch.max(outputs.data, 1)
            valid_running_correct += (preds == labels).sum().item()
        
    # Loss and accuracy for the complete epoch.
    epoch_loss = valid_running_loss / counter
    epoch_acc = 100. * (valid_running_correct / len(testloader.dataset))
    return epoch_loss, epoch_acc

def debug_mode():
    debug = False
    return debug

def main():
    debug = debug_mode()

    download_dataset('./scripts/stanford_dataset.sh')
    crop_dataset()

    if debug:
        # Load the training and validation datasets.
        train_ds, test_ds, dataset_classes = get_datasets()
        print(f"[INFO]: Number of training images: {len(train_ds)}")
        print(f"[INFO]: Number of validation images: {len(test_ds)}")
        # Load the training and validation data loaders.
        train_loader, valid_test = get_data_loaders(train_ds, test_ds)
        # Learning_parameters. 
        lr = args['learning_rate']
        epochs = args['epochs']
        
        print(f"Computation device: {DEVICE}")
        print(f"Learning rate: {lr}")
        print(f"Epochs to train for: {epochs}\n")
        # Load the model.
        model = load_model(
            pretrained=True,
            fine_tune=True, 
            num_classes=len(dataset_classes)
        ).to(DEVICE)
        
        # Total parameters and trainable parameters.
        total_params = sum(p.numel() for p in model.parameters())
        print(f"{total_params:,} total parameters.")
        total_trainable_params = sum(
            p.numel() for p in model.parameters() if p.requires_grad)
        print(f"{total_trainable_params:,} training parameters.")
        # Optimizer.
        optimizer = optim.Adam(model.parameters(), lr=lr)
        # Loss function.
        criterion = nn.CrossEntropyLoss()
        # Lists to keep track of losses and accuracies.
        train_loss, valid_loss = [], []
        train_acc, valid_acc = [], []
        # Start the training.
        for epoch in range(epochs):
            print(f"[INFO]: Epoch {epoch+1} of {epochs}")
            train_epoch_loss, train_epoch_acc = train(model, train_loader, 
                                                    optimizer, criterion)
            valid_epoch_loss, valid_epoch_acc = validate(model, valid_test,  
                                                        criterion, dataset_classes)
            train_loss.append(train_epoch_loss)
            valid_loss.append(valid_epoch_loss)
            train_acc.append(train_epoch_acc)
            valid_acc.append(valid_epoch_acc)
            print(f"Training loss: {train_epoch_loss:.3f}, training acc: {train_epoch_acc:.3f}")
            print(f"Validation loss: {valid_epoch_loss:.3f}, validation acc: {valid_epoch_acc:.3f}")
            print('-'*50)
            time.sleep(2)
        # Save the trained model weights.
        save_model(epochs, model, optimizer, criterion)
        # Save the loss and accuracy plots.
        save_plots(train_acc, valid_acc, train_loss, valid_loss)
        print('TRAINING COMPLETE')

if __name__ == '__main__':
    main()