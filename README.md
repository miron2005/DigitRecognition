Распознавание рукописных цифр (DigitRecognition)
Проект реализует сверточную нейронную сеть (CNN) для распознавания рукописных цифр с использованием датасета MNIST. Модель достигает высокой точности классификации и готова к использованию на новых изображениях.

Ключевые особенности
🧠 Глубокая CNN-архитектура с BatchNormalization и Dropout

📊 Визуализация процесса обучения и метрик

💾 Сохранение и загрузка обученной модели

🖼️ Поддержка распознавания пользовательских изображений

📦 Автоматическая упаковка в ZIP-архив для удобного экспорта

Технологии
Python 3

TensorFlow/Keras

NumPy

Matplotlib

Pillow (PIL)

Google Colab (для облачного выполнения)

Структура проекта
model_mnist.h5 - предобученная модель

script.py - скрипт для распознавания

label.txt - метки классов

0.jpg-9.jpg - примеры изображений цифр

