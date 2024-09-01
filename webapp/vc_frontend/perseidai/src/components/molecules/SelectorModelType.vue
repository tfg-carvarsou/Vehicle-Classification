<template>
  <div class="mt-container">
    <h2 class="mt-title">Try it out</h2>
    <div class="mt-options">
      <div
        class="mt-opt"
        id="mt-opt-detector"
        :class="{ active: selectedModelType === 'detector' }"
        @click="selectModelType('detector')"
      >
        <div class="mt-icon mt-icon-detector">
          <img src="@/assets/icons/detector-type.webp" alt="Detector icon" />
        </div>
        <span class="mt-icon-detector-text">Detector</span>
      </div>
      <div
        class="mt-opt"
        id="mt-opt-classificator"
        :class="{ active: selectedModelType === 'classificator' }"
        @click="selectModelType('classificator')"
      >
        <div class="mt-icon mt-icon-classificator">
          <img src="@/assets/icons/classificator-type.webp" alt="Classificator icon" />
        </div>
        <span class="mt-icon-classificator-text">Classificator</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'

const emit = defineEmits(['select-model-type'])
const selectedModelType = ref<string>('')

const selectModelType = (modelType: string) => {
  selectedModelType.value = modelType
  emit('select-model-type', modelType)
}
</script>

<style scoped>
.mt-container {
  display: flex;
  flex-direction: column;
  align-items: left;
  margin-top: 20px;
  text-align: center;
}

.mt-title {
  display: flex;
  font-size: 30px;
  font-weight: bold;
  color: #083863;
}

.mt-options {
  display: flex;
  justify-content: inherit;
  gap: 10px;
  margin-left: 150px;
  margin-top: 20px;
}

.mt-opt {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  padding: 10px;
  border-radius: 12px;
  transition: all 0.3s ease;
  position: relative;
}

.mt-opt:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
}

#mt-opt-detector.active {
  border: 2px solid #00acea;
  background-color: rgba(0, 172, 234, 0.1);
}

#mt-opt-classificator.active {
  border: 2px solid #083863;
  background-color: rgba(8, 56, 99, 0.1);
}

.mt-opt span {
  font-weight: bold;
  margin-top: 8px;
  transition: color 0.3s ease;
}

.mt-icon img {
  width: 90px;
  height: 90px;
  transition: transform 0.3s ease;
}

.mt-icon img:hover {
  transform: scale(1.1);
}

.mt-icon-detector-text {
  color: #00acea;
}

.mt-icon-classificator-text {
  color: #083863;
}

.mt-opt.active .mt-icon-detector-text {
  color: #00acea;
}

.mt-opt.active .mt-icon-classificator-text {
  color: #083863;
}

@media (max-width: 1024px) {
  .mt-options {
    margin-left: 0;
  }
}
</style>
