import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset

class SimpleOCRDataset(Dataset):
    def __init__(self, data, labels):
        self.data = data
        self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

class OCRModel(nn.Module):
    def __init__(self):
        super(OCRModel, self).__init__()
        self.lstm = nn.LSTM(input_size=28, hidden_size=128, batch_first=True)
        self.fc = nn.Linear(128, 26)  # Assuming 26 characters (A-Z)

    def forward(self, x):
        out, _ = self.lstm(x)
        return self.fc(out[:, -1, :])

# Training loop here
