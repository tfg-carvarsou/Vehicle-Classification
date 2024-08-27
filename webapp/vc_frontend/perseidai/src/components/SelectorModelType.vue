<template>
  <div class="mt-container">
    <h2 class="mt-title">Try it out</h2>
    <div class="mt-options">
      <div class="mt-option" id="mt-option-detector" @click="selectModelType('detector')">
        <div class="mt-icon mt-icon-detector">
          <img src="@/assets/icons/detector-type.webp" alt="Detector icon" />
        </div>
        <span class="mt-icon-detector-text">Detector</span>
      </div>
      <div class="mt-option" id="mt-option-classificator" @click="selectModelType('classificator')">
        <div class="mt-icon mt-icon-classificator">
          <img src="@/assets/icons/classificator-type.webp" alt="Classificator icon" />
        </div>
        <span class="mt-icon-classificator-text">Classificator</span>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
const emit = defineEmits(['select-model-type'])
const selectModelType = (modelType: string) => {
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
  color: #083863;
}

.mt-title {
  display: flex;
  font-size: 30px;
  font-weight: bold;
}

.mt-options {
  display: flex;
  justify-content: center;
  gap: 20px;
  margin-top: 20px;
}

.mt-option {
  display: flex;
  flex-direction: column;
  align-items: center;
  cursor: pointer;
  padding: 10px;
}

.mt-option span {
  font-weight: bold;
}

.mt-icon img {
  width: 90px;
  height: 90px;
}

.mt-icon-detector-text {
  color: #00acea;
}

.mt-icon-classificator-text {
  color: #083863;
}
</style>
