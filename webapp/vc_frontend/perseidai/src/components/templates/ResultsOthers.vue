<template>
  <div class="results-others-container">
    <div class="results-others-title" v-if="isHomeView">
      <h1>See results of others uploads</h1>
    </div>
    <div class="results-others-cards">
      <div class="detector-card-list" v-if="isDetectorCardListShown">
        <div class="results-others-title" v-if="!isHomeView">
          <h1>
            See results of
            <span class="detector-title">&nbsp;Detector&nbsp;</span>
            uploads
          </h1>
        </div>
        <DetectorCard
          v-for="(vdcard, index) in vdcards"
          :key="index"
          :type="vdcard.type"
          :filename="vdcard.filename"
          :username="vdcard.username"
          :model="vdcard.model"
          :image="vdcard.image"
          :infTime="vdcard.infTime"
        />
      </div>
      <div class="classificator-card-list" v-if="isClassificatorCardListShown">
        <div class="results-others-title" v-if="!isHomeView">
          <h1>
            See results of
            <span class="classificator-title">&nbsp;Classificator&nbsp;</span>
            uploads
          </h1>
        </div>
        <ClassificatorCard
          v-for="(vccard, index) in vccards"
          :key="index"
          :type="vccard.type"
          :filename="vccard.filename"
          :username="vccard.username"
          :model="vccard.model"
          :image="vccard.image"
          :infTime="vccard.infTime"
        />
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import DetectorCard from '@/components/organisms/DetectorCard.vue'
import ClassificatorCard from '@/components/organisms/ClassificatorCard.vue'
import detectorTypeImage from '@/assets/icons/detector-type.webp'
import classificatorTypeImage from '@/assets/icons/classificator-type.webp'
import yolov5ModelImage from '@/assets/images/yolov5.webp'
import effnetModelImage from '@/assets/images/effnet.webp'
import yolov8ModelImage from '@/assets/images/yolov8.webp'
import placeholderImage from '@/assets/images/placeholder.png'

const vdcards = reactive([
  {
    type: detectorTypeImage,
    filename: 'filename1',
    username: 'Anonymous',
    model: yolov5ModelImage,
    image: placeholderImage,
    infTime: 0.983
  },
  {
    type: detectorTypeImage,
    filename: 'filename2',
    username: 'Anonymous',
    model: yolov5ModelImage,
    image: placeholderImage,
    infTime: 0.835
  },
  {
    type: detectorTypeImage,
    filename: 'filename3',
    username: 'Anonymous',
    model: yolov8ModelImage,
    image: placeholderImage,
    infTime: 0.534
  }
])

const vccards = reactive([
  {
    type: classificatorTypeImage,
    filename: 'filename4',
    username: 'Anonymous',
    model: effnetModelImage,
    image: placeholderImage,
    infTime: 0.981
  },
  {
    type: classificatorTypeImage,
    filename: 'filename5',
    username: 'Anonymous',
    model: yolov8ModelImage,
    image: placeholderImage,
    infTime: 1.134
  },
  {
    type: classificatorTypeImage,
    filename: 'filename6',
    username: 'Anonymous',
    model: effnetModelImage,
    image: placeholderImage,
    infTime: 0.823
  }
])

defineProps<{
  isHomeView: boolean
  isDetectorCardListShown: boolean
  isClassificatorCardListShown: boolean
}>()
</script>

<style scoped>
.results-others-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-top: 200px;
  margin-bottom: 130px;
  width: 200%;
}

.results-others-title h1 {
  display: flex;
  line-height: 1.3;
  font-size: 2.8rem;
  font-weight: 500;
  margin-bottom: 32px;
}

.detector-title {
  font-weight: inherit;
  color: #00acea;
}

.classificator-title {
  font-weight: inherit;
  color: #083863;
}

.results-others-cards {
  display: flex;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
  max-width: 1200px;
}

.detector-card-list,
.classificator-card-list {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.vdcard,
.vccard {
  width: calc(33.333% - 11px);
  box-sizing: border-box;
}
</style>
