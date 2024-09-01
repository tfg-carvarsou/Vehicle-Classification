<template>
  <div class="ms-container">
    <!-- Show detector models if 'detector' is selected -->
    <h2 class="ms-title">{{ modelSeriesTitle }}</h2>
    <div v-if="selectedModelType === 'detector'" class="ms-container-detector">
      <div class="ms-options">
        <div
          class="ms-opt"
          id="ms-opt-detector-yolov5"
          :class="{ active: selectedModelSeries === 'yolov5' }"
          @click="selectModelSeries('yolov5')"
        >
          <div class="ms-img ms-img-detector-yolov5">
            <img src="@/assets/images/yolov5.webp" alt="YOLOV5 detector image" />
          </div>
        </div>
        <div
          class="ms-opt"
          id="ms-opt-detector-yolov8"
          :class="{ active: selectedModelSeries === 'yolov8' }"
          @click="selectModelSeries('yolov8')"
        >
          <div class="ms-img ms-img-detector-yolov8">
            <img src="@/assets/images/yolov8.webp" alt="YOLOV8 detector image" />
          </div>
        </div>
      </div>
    </div>

    <!-- Show classificator models if 'classificator' is selected -->
    <div v-if="selectedModelType === 'classificator'" class="ms-container-classificator">
      <div class="ms-options">
        <div
          class="ms-opt"
          id="ms-opt-classificator-effnet"
          :class="{ active: selectedModelSeries === 'effnet' }"
          @click="selectModelSeries('effnet')"
        >
          <div class="ms-img ms-img-classificator-effnet">
            <img src="@/assets/images/effnet.webp" alt="EfficientNet classificator image" />
          </div>
        </div>
        <div
          class="ms-opt"
          id="ms-opt-classificator-yolov8cls"
          :class="{ active: selectedModelSeries === 'yolov8cls' }"
          @click="selectModelSeries('yolov8cls')"
        >
          <div class="ms-img ms-img-classificator-yolov8cls">
            <img src="@/assets/images/yolov8.webp" alt="YOLOV8 classificator image" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits(['select-model-series'])
const selectedModelSeries = ref<string>('')

const selectModelSeries = (modelSeries: string) => {
  selectedModelSeries.value = modelSeries
  emit('select-model-series', modelSeries)
}

defineProps<{
  selectedModelType: string
  modelSeriesTitle: string
}>()
</script>

<style scoped>
.ms-container {
  display: flex;
  flex-direction: column;
  align-items: left;
  margin-top: -30px;
  text-align: center;
}

.ms-title {
  display: flex;
  font-size: 30px;
  font-weight: bold;
  color: #083863;
}

.ms-options {
  display: flex;
  justify-content: inherit;
  gap: 10px;
  margin-top: 20px;
}

.ms-opt {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  padding: 10px;
  border-radius: 12px;
  transition: all 0.3s ease;
  position: relative;
}

.ms-opt:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

.ms-opt.active {
  border: 2px solid #00acea;
  background-color: rgba(0, 172, 234, 0.1);
}

#ms-opt-detector-yolov5.active {
  border: 2px solid #00acea;
  background-color: rgba(0, 172, 234, 0.1);
}

#ms-opt-detector-yolov8.active {
  border: 2px solid #00acea;
  background-color: rgba(8, 56, 99, 0.1);
}

#ms-opt-classificator-effnet.active {
  border: 2px solid #083863;
  background-color: rgba(0, 172, 234, 0.1);
}

#ms-opt-classificator-yolov8cls.active {
  border: 2px solid #083863;
  background-color: rgba(8, 56, 99, 0.1);
}

.ms-img img {
  width: 256px;
  height: 174px;
  border-radius: 30px;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.5);
}

@media (max-width: 1024px) {
  .ms-container {
    margin-top: 50px;
    margin-left: -50px;
  }

  .ms-options {
    justify-content: left;
  }
}
</style>
