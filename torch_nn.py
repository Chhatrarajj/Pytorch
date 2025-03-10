# -*- coding: utf-8 -*-
"""Torch.nn.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1tAhy-Ilq2pA5v3rjtQXJSJSKukPQjnXf
"""

import torch
import torch.nn as nn

class Model(nn.Module):
    def __init__(self,num_features):
      super().__init__()
      self.network = nn.Sequential(
      nn.Linear(num_features,3),
      nn.ReLU(),
      nn.Linear(3,1),
      nn.Sigmoid()
      )

    def forward(self,features):
      out = self.network(features)

      return out

features = torch.rand(10,5)

model = Model(features.shape[1])

model(features)

model.linear2.weight

model.linear2 .bias

!pip install torchinfo

from torchinfo import summary
summary(model,input_size=(10,5))

