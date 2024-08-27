<template>
  <div class="view-container">
    <!-- Main Header: Title and Image -->
    <div class="mh-container">
      <div class="mh-title">
        <h1>
          <div class="mh-line-1">
            <span>Test Real-Time</span>
            <span class="mh-text-1"><i> AI</i></span>
            <span> Vehicle</span>
          </div>
          <div class="mh-line-2">
            <span class="mh-text-2"> Detection</span>
            <span> and</span>
            <span class="mh-text-3"> Classification</span>
          </div>
          <div class="mh-line-3">
            <span> Models.</span>
          </div>
        </h1>
        <!-- Model type selector -->
        <SelectorModelType 
          @select-model-type="handleModelTypeSelection" />
      </div>
      <div class="mh-img">
        <img src="@/assets/images/placeholder.png" alt="placeholder" />
      </div>
    </div>
    <!-- Model selector -->
    <SelectorModelSeries 
      @select-model-series="handleModelSeriesSelection" 
      v-if="isModelTypeSelected" :selectedModelType="selectedModelType" />
    <!-- Upload file form -->
    <UploadFileForm 
      v-if="isModelSeriesSelected" :selectedModelSeries="selectedModelSeries" />
  </div>
</template>

# TODO: Hover effect on model type and model series selection
# TODO: Fix UploadFileForm CSS

<script setup lang="ts">
import { ref } from 'vue'
import SelectorModelType from '@/components/SelectorModelType.vue'
import SelectorModelSeries from '@/components/SelectorModelSeries.vue'
import UploadFileForm from '@/components/UploadFileForm.vue'

const isModelTypeSelected = ref(false)
const selectedModelType = ref('') // detector or classificator
const handleModelTypeSelection = (modelType: string) => {
  isModelTypeSelected.value = true
  selectedModelType.value = modelType
  isModelSeriesSelected.value = false
}

const isModelSeriesSelected = ref(false)
const selectedModelSeries = ref('') // yolov5, yolov8, effnet, yolov8cls
const handleModelSeriesSelection = (modelSeries: string) => {
  isModelSeriesSelected.value = true
  selectedModelSeries.value = modelSeries
  console.log(selectedModelSeries.value)
}
</script>

<style scoped>
.view-container {
  color: #232323;
}

.mh-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  height: 60vh;
  width: auto;
  flex-wrap: wrap;
}

.mh-title {
  flex: 1;
  display: inline-block;
  flex-direction: column;
  align-items: center;
  font-size: 22px;
  margin-right: 5vh;
}

.mh-text-1 {
  color: #02af98;
}

.mh-text-2 {
  color: #00acea;
}

.mh-text-3 {
  color: #083863;
}

.mh-img img {
  flex: 1;
  max-width: 100%;
  height: auto;
  object-fit: cover;
}

h1 {
  line-height: 1.3;
  font-size: 2.8rem;
}

@media (max-width: 1024px) {
  .mh-container {
    flex-direction: row;
    align-items: center;
  }

  .mh-title {
    height: auto;
    padding-top: 50px;
  }

  .mh-img img {
    width: 100%;
  }
}
</style>
