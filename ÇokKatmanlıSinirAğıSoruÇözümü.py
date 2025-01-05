# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 10:25:45 2024

@author: bingl
"""

import numpy as np

# Aktivasyon fonksiyonu ve türevi (Sigmoid)
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def sigmoid_derivative(x):
    return x * (1 - x)

# XOR yerine görseldeki veri seti
X = np.array([[0.12, -0.69], [0.85, -0.50], [-0.51, -0.35]])
y = np.array([[0], [1], [2]])

# Ağırlıkları ve biasları rastgele başlatma
np.random.seed(42)
input_layer_neurons = 2  # Giriş katmanındaki nöron sayısı
hidden_layer_neurons = 3  # Gizli katmanındaki nöron sayısı
output_neurons = 1  # Çıkış katmanındaki nöron sayısı

# Ağırlıklar
weights_input_hidden = np.random.uniform(size=(input_layer_neurons, hidden_layer_neurons))
weights_hidden_output = np.random.uniform(size=(hidden_layer_neurons, output_neurons))

# Biaslar
bias_hidden = np.random.uniform(size=(1, hidden_layer_neurons))
bias_output = np.random.uniform(size=(1, output_neurons))

# Öğrenme hızı
lr = 0.1

# Eğitim
epochs = 10000
for epoch in range(epochs):
    # İleri yayılım
    hidden_layer_input = np.dot(X, weights_input_hidden) + bias_hidden
    hidden_layer_output = sigmoid(hidden_layer_input)

    output_layer_input = np.dot(hidden_layer_output, weights_hidden_output) + bias_output
    output = sigmoid(output_layer_input)

    # Hata hesaplama
    error = y - output
    d_output = error * sigmoid_derivative(output)

    # Geri yayılım
    error_hidden_layer = d_output.dot(weights_hidden_output.T)
    d_hidden_layer = error_hidden_layer * sigmoid_derivative(hidden_layer_output)

    # Ağırlık ve bias güncellemeleri
    weights_hidden_output += hidden_layer_output.T.dot(d_output) * lr
    weights_input_hidden += X.T.dot(d_hidden_layer) * lr
    bias_output += np.sum(d_output, axis=0, keepdims=True) * lr
    bias_hidden += np.sum(d_hidden_layer, axis=0, keepdims=True) * lr

# Test
print("Eğitim Tamamlandı!")
print("Sonuçlar:")
print(output)
