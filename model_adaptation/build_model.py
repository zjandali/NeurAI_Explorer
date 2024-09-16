import torch
import torch.nn as nn
import random

def build_dynamic_model(keywords):
    layers = []
    input_size = 784  # Example input size (e.g., MNIST)
    output_size = 10   # Example output size

    # Example: Add layers based on keywords
    if 'dropout' in keywords:
        layers.append(nn.Dropout(p=0.5))
    if 'batch normalization' in keywords:
        layers.append(nn.BatchNorm1d(input_size))
    # Add more conditions based on extracted keywords

    # Example: Adding a hidden layer
    hidden_size = random.choice([128, 256, 512])
    layers.append(nn.Linear(input_size, hidden_size))
    layers.append(nn.ReLU())

    # Output layer
    layers.append(nn.Linear(hidden_size, output_size))
    
    model = nn.Sequential(*layers)
    return model
