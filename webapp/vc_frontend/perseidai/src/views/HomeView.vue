<template>
  <div class="view-container">
    <!-- Main title -->
    <MainTitleHome />
    <!-- Model type selector -->
    <SelectorModelType @select-model-type="handleModelTypeSelection" />
    <!-- Models and upload container -->
    <div class="model-and-upload-container">
      <!-- Model series selector -->
      <div
        ref="modelSelector"
        class="model-selector"
        :class="{ 'scroll-into-models': isModelTypeSelected }"
      >
        <SelectorModelSeries
          v-if="isModelTypeSelected"
          :selectedModelType="selectedModelType"
          @select-model-series="handleModelSeriesSelection"
        />
      </div>
      <!-- Upload file form -->
      <div
        ref="uploadFileForm"
        class="upload-file-form"
        :class="{ 'scroll-into-upload': isModelSeriesSelected }"
      >
        <UploadFileForm v-if="isModelSeriesSelected" :selectedModelSeries="selectedModelSeries" />
      </div>
    </div>
    <!-- Results of others uploads -->
  </div>
</template>

<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'
import MainTitleHome from '@/components/templates/MainTitleHome.vue'
import SelectorModelType from '@/components/molecules/SelectorModelType.vue'
import SelectorModelSeries from '@/components/molecules/SelectorModelSeries.vue'
import UploadFileForm from '@/components/organisms/UploadFileForm.vue'
import ResultsOthers from '@/components/templates/ResultsOthers.vue'

const isModelTypeSelected = ref(false)
const selectedModelType = ref('') // detector or classificator
const isModelSeriesSelected = ref(false)
const selectedModelSeries = ref('') // yolov5, yolov8, effnet, yolov8cls
const modelSelector = ref<HTMLElement | null>(null)
const uploadFileForm = ref<HTMLElement | null>(null)

const handleModelTypeSelection = (modelType: string) => {
  isModelTypeSelected.value = true
  selectedModelType.value = modelType
  isModelSeriesSelected.value = false
}

const handleModelSeriesSelection = (modelSeries: string) => {
  isModelSeriesSelected.value = true
  selectedModelSeries.value = modelSeries
}

watch(isModelTypeSelected, async (newValue) => {
  if (newValue) {
    await nextTick()
    modelSelector.value?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
})

watch(isModelSeriesSelected, async (newValue) => {
  if (newValue) {
    await nextTick()
    uploadFileForm.value?.scrollIntoView({ behavior: 'smooth', block: 'start' })
  }
})
</script>

<style scoped>
.view-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  color: #232323;
  margin-top: 120px;
  margin-bottom: 160px;
}

.model-and-upload-container {
  display: flex;
  flex-direction: row;
  gap: 100px;
  justify-content: left;
  margin-top: 20px;
  max-width: 25vh;
}

.upload-file-form {
  max-width: 40vh;
}

.model-selector,
.upload-file-form {
  flex: 1;
}

.scroll-into-models {
  transform: translateY(50px);
}

.scroll-into-upload {
  margin-top: 50px;
  transform: translateX(50px);
}

@media (max-width: 1024px) {
  .model-and-upload-container {
    flex-direction: column;
    align-items: center;
  }

  .model-selector,
  .upload-file-form {
    max-width: 100%;
  }

  .scroll-into-models {
    margin-left: 0;
    transform: translateY(-50px);
  }

  .scroll-into-upload {
    margin-left: 0;
    transform: translate(-140px, -140px);
  }
}
</style>
