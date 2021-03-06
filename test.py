  
from utils.losses import CrossEntropyLoss
from utils.device import default_device

from models.enet import ENet
from dataloader.cityscapes import CityScapesDataLoader

import torch 
import numpy as np 
import torch

#This will call tester.py which is just the basic function. All the arguements like optimizer, scheduler etc will be provided from here to tester.
# we need to make this test.py in class so that we can call it from run.py
#copied most stuff from train.py mradul made and made some minor changes to it

class Test:
    def __init__(self, config):
        self.config = config
        self.model = ENet(self.config)
        self.dataloader = CityScapesDataLoader(self.config)
        self.loss = CrossEntropyLoss(self.config)

        self.optimizer = torch.optim.Adam(self.model.parameters(),
                                          lr=self.config.learning_rate,
                                          weight_decay=self.config.weight_decay)

        self.scheduler = torch.optim.lr_scheduler.ExponentialLR(self.optimizer,
                                                                gamma=self.config.gamma)

        self.test_dataloader = self.dataloader.test_loader

        self.current_epoch = 1

        self.device = default_device()

        self.model = self.model.to(self.device)
        self.loss = self.loss.to(self.device)

    def forward(self):
      tester(epochs=self.epochs, model=self.model, train_loader=self.train_loader, val_loader=self.valid_loader, criterion=self.criterion, optimizer=self.optimizer, scheduler=self.scheduler, checkpoint_path, best_model_path)
