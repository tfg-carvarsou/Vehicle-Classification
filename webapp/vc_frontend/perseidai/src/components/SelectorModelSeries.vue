<template>
  <div class="ms-container">
    <!-- Show detector models if 'detector' is selected -->
    <div v-if="selectedModelType === 'detector'" class="ms-container-detector">
      <h2 class="ms-title">Choose a detection model</h2>
      <!-- Detector models -->
      <div class="ms-options">
        <div class="ms-opt" id="ms-opt-detector-yolov5" @click="selectModelSeries('yolov5')">
          <div class="ms-img ms-img-detector-yolov5">
            <img src="@/assets/images/yolov5.webp" alt="YOLOV5 detector image" />
          </div>
        </div>
        <div class="ms-opt" id="ms-opt-detector-yolov8" @click="selectModelSeries('yolov8')">
          <div class="ms-img mt-img-detector-yolov8">
            <img src="@/assets/images/yolov8.webp" alt="YOLOV8 detector image" />
          </div>
        </div>
      </div>
    </div>

    <!-- Show classificator models if 'classificator' is selected -->
    <div v-if="selectedModelType === 'classificator'" class="ms-container-classificator">
      <h2 class="ms-title">Choose a classification model</h2>
      <!-- Classificator models -->
      <div class="ms-options">
        <div class="ms-opt" id="ms-opt-classificator-effnet" @click="selectModelSeries('effnet')">
          <div class="ms-img ms-img-classificator-effnet">
            <img src="@/assets/images/effnet.webp" alt="EfficientNet classificator image" />
          </div>
        </div>
        <div
          class="ms-opt"
          id="ms-opt-classificator-yolov8cls"
          @click="selectModelSeries('yolov8cls')"
        >
          <div class="ms-img mt-img-classificator-yolov8cls">
            <img src="@/assets/images/yolov8.webp" alt="YOLOV8 classificator image" />
          </div>
          <span class="ms-text">for Classification</span>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  selectedModelType: string
}>()
const emit = defineEmits(['select-model-series'])
const selectModelSeries = (modelSeries: string) => {
  emit('select-model-series', modelSeries)
}
</script>

<style scoped>
.ms-container {
  display: flex;
  flex-direction: column;
  align-items: left;
  margin-top: 20px;
  text-align: center;
  color: #083863;
}

.ms-title {
  display: flex;
  font-size: 30px;
  font-weight: bold;
}

.ms-options {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.ms-opt {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
}

.ms-img img {
  width: 256px;
  height: 174px;
  border-radius: 30px;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.5);
}
</style>
