<template>
  <Suspense>
    <div class="classifier-view-container">
      <HeaderClassifier />
      <div class="model-selector">
        <SelectorModelSeries
          :selectedModelType="'classifier'"
          :modelSeriesTitle="modelSeriesTitle"
          @select-model-series="handleModelSeriesSelection"
        />
      </div>
      <div
        ref="uploadImageForm"
        class="upload-image-form"
        :class="{ 'scroll-into-upload': isModelSeriesSelected }"
      >
        <UploadImageForm
          v-if="isModelSeriesSelected"
          :selectedModelType="'classifier'"
          :selectedModelSeries="selectedModelSeries"
        />
      </div>
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
import { updateText } from '@/utils/text'
import HeaderClassifier from '@/components/templates/HeaderClassifier.vue'
import SelectorModelSeries from '@/components/molecules/SelectorModelSeries.vue'
import UploadImageForm from '@/components/organisms/UploadImageForm.vue'
import ResultsOthers from '@/components/templates/ResultsOthers.vue'

const modelSeriesTitle = ref('Choose your model')
updateText('.ms-title', modelSeriesTitle.value)

const isHomeView = ref(false)
const isDetectorCardListShown = ref(false)
const isClassifierCardListShown = ref(true)
const isModelSeriesSelected = ref(false)
const selectedModelSeries = ref('')
const uploadImageForm = ref<HTMLElement | null>(null)
const scrollOffset = 370

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

watch(isModelSeriesSelected, async (newValue) => {
  if (newValue) {
    await nextTick()
    scrollToElement(uploadImageForm.value, scrollOffset)
  }
})
</script>

<style scoped>
:deep(.ms-container),
:deep(.upload-image-form) {
  all: unset;
  display: flex;
  flex-direction: column;
  width: 100%;
}

:deep(.ms-options),
:deep([data-part='root']) {
  margin-left: 300px;
  margin-top: -120px;
  width: 65%;
}

:deep(.results-others-container) {
  display: flex;
  align-items: flex-start;
  flex-direction: column;
  color: #232323;
  max-width: 1200px;
}

:deep(.results-others-title h1) {
  margin-left: 300px;
}

.classifier-view-container {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  width: 100%;
  margin-top: 150px;
}

.scroll-into-upload {
  margin-top: 20px;
  transform: translateY(100px);
}
</style>
