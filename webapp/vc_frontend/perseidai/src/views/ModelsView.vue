<template>
  <Suspense>
    <div class="models-view-container">
      <div class="models-view-section">
        <HeaderDetector />
        <div class="models-image-container">
          <img src="@/assets/images/yolov5.webp" class="mv-img" alt="YOLOV5s detector image" />
          <img src="@/assets/images/yolov8.webp" class="mv-img" alt="YOLOV8s detector image" />
        </div>
        <p class="mv-text">
          Among the most prominent models for object detection is the You Only Look Once (YOLO) series, designed to provide real-time results with high accuracy and minimal processing time. Although there are more than a dozen versions of YOLO, this project uses YOLOv5 and YOLOv8 models to recognize the number and type of vehicles present in images.
          <br>
          <br>
          <a href="https://github.com/ultralytics/yolov5">YOLOv5</a>, introduced in 2020 by Glenn Jocher, marked a significant advancement in performance, flexibility, and ease of use. Its rise in popularity was due to its modular design, allowing model customization and export to various formats such as ONNX, CoreML, and TFLite for deployment.
          <br>
          <br>
          <a href="https://github.com/ultralytics/ultralytics">YOLOv8</a>, introduced in 2023, is the most advanced framework from Ultralytics (state-of-the-art, SOTA), designed to enhance the performance of real-time object detection with advanced functionalities.
        </p>
      </div>
      <div class="models-view-section">
        <HeaderClassifier />
        <div class="models-image-container">
          <img
            src="@/assets/images/effnet.webp"
            class="mv-img"
            alt="EfficientNetB1 detector image"
          />
          <img src="@/assets/images/yolov8.webp" class="mv-img" alt="YOLOV8s-cls detector image" />
        </div>
        <p class="mv-text">
          The <a href="https://research.google/blog/efficientnet-improving-accuracy-and-efficiency-through-automl-and-model-scaling/">EfficientNet</a> architecture is a series of convolutional neural network (CNN) models developed by Google AI, which stood out in the field of image classification for its ability to efficiently balance accuracy and computational efficiency. EfficientNet's innovative approach is based on a method called <strong>Compound Scaling</strong>, which simultaneously adjusts three key dimensions of the model: depth (number of layers), width (number of filters), and input resolution.
          <br>
          <br>
            Unlike other scaling approaches that adjust only one dimension, EfficientNet proposes a balanced strategy, scaling these three dimensions together, resulting in significant improvements in accuracy without a disproportionate increase in computational requirements. In fact, EfficientNet has demonstrated superior performance in image classification benchmarks like ImageNet, outperforming larger models in terms of both efficiency and accuracy.
          <br>
          <br>
            However, YOLOv8 also includes a variant focused on image classification called <strong>YOLOv8-cls</strong>. Although YOLO is primarily known for its speed and accuracy in object detection, YOLOv8-cls aims to bring those capabilities to the image classification domain. This version of YOLOv8-cls inherits the network architecture used in object detection, specifically optimizing it for classification tasks.
        </p>
      </div>
    </div>
  </Suspense>
</template>

<script setup lang="ts">
import HeaderDetector from '@/components/templates/HeaderDetector.vue'
import HeaderClassifier from '@/components/templates/HeaderClassifier.vue'
</script>

<style scoped>
.models-view-container {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin: 0 auto;
  padding: 0 20px;
  margin-top: 6rem;
}

.models-view-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin-inline: 50px;
  margin-left: -5px;
}

.models-image-container {
  display: flex;
  gap: 20px;
  justify-content: center;
}

.mv-img {
  width: 256px;
  height: 174px;
  border-radius: 30px;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.5);
  margin-top: 2rem;
}

.mv-text {
  font-size: 1.3rem;
  text-align: justify;
  color: #083863;
  margin-top: 3rem;
  margin-bottom: 10rem;
}

:deep(.header-detector-container),
:deep(.header-classifier-container) {
  margin: 0 auto;
}
</style>
