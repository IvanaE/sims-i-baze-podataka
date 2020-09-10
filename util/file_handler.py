from abc import ABC, abstractmethod
import os, json

class FileHandler():
    def __init__(self):
        super().__init__()

    
    @abstractmethod
    def load_data(self):
        pass
        
    @abstractmethod
    def get_one(self, id):
        pass

    @abstractmethod
    def get_all(self):
        pass

    @abstractmethod
    def edit(self, id):
        pass

    @abstractmethod
    def delete_one(self, id):
        pass
    
    @abstractmethod
    def insert(self, obj):
        pass

    @abstractmethod
    def insert_many(self, obj):
        pass

    @abstractmethod
    def save(self, obj):
        pass