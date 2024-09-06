<template>
  <Suspense>
    <div class="home-view-container">
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
            :modelSeriesTitle="modelSeriesTitle"
            @select-model-series="handleModelSeriesSelection"
          />
        </div>
        <!-- Upload file form -->
        <div
          ref="uploadImageForm"
          class="upload-image-form"
          :class="{ 'scroll-into-upload': isModelSeriesSelected }"
        >
          <UploadImageForm v-if="isModelSeriesSelected" :selectedModelSeries="selectedModelSeries" />
        </div>
      </div>
      <!-- Results of others uploads -->
      <ResultsOthers
        :isHomeView="isHomeView"
        :isDetectorCardListShown="isDetectorCardListShown"
        :isClassifierCardListShown="isClassifierCardListShown"
      />
    </div>
  </Suspense>
</template>

<script setup lang="ts">
import { ref, watch, nextTick } from 'vue'
import MainTitleHome from '@/components/templates/HeaderHome.vue'
import SelectorModelType from '@/components/molecules/SelectorModelType.vue'
import SelectorModelSeries from '@/components/molecules/SelectorModelSeries.vue'
import UploadImageForm from '@/components/organisms/UploadImageForm.vue'
import ResultsOthers from '@/components/templates/ResultsOthers.vue'

const isHomeView = ref(true)
const isDetectorCardListShown = ref(true)
const isClassifierCardListShown = ref(true)
const modelSeriesTitle = ref('Choose your model')
const isModelTypeSelected = ref(false)
const selectedModelType = ref('') // detector or classifier
const isModelSeriesSelected = ref(false)
const selectedModelSeries = ref('') // yolov5, yolov8, effnet, yolov8cls
const modelSelector = ref<HTMLElement | null>(null)
const uploadImageForm = ref<HTMLElement | null>(null)
const scrollOffset = 370

const handleModelTypeSelection = (modelType: string) => {
  isModelTypeSelected.value = true
  selectedModelType.value = modelType
  isModelSeriesSelected.value = false
  modelSeriesTitle.value =
    modelType === 'detector' ? 'Choose your detection model' : 'Choose your classification model'
}

const handleModelSeriesSelection = (modelSeries: string) => {
  isModelSeriesSelected.value = true
  selectedModelSeries.value = modelSeries
}

const scrollToElement = (element: HTMLElement | null, offset: number) => {
  if (element) {
    const rect = element.getBoundingClientRect()
    window.scrollTo({
      top: window.scrollY + rect.top - offset,
      behavior: 'smooth'
    })
  }
}

watch(isModelTypeSelected, async (newValue) => {
  if (newValue) {
    await nextTick()
    scrollToElement(modelSelector.value, scrollOffset)
  }
})

watch(isModelSeriesSelected, async (newValue) => {
  if (newValue) {
    await nextTick()
    scrollToElement(uploadImageForm.value, scrollOffset)
  }
})
</script>

<style scoped>
.home-view-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  color: #232323;
  margin-top: 120px;
}

.model-and-upload-container {
  display: flex;
  flex-direction: row;
  gap: 100px;
  justify-content: left;
  margin-top: 20px;
  max-width: 25vh;
}

.upload-image-form {
  max-width: 40vh;
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
  .upload-image-form {
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
