<template>
  <div class="results-others-container">
    <div class="results-others-title">
      <h1>See results of others uploads</h1>
    </div>
    <div class="results-others-cards">
      <DetectorCard
        v-for="(card, index) in cards"
        :key="index"
        :type="card.type"
        :filename="card.filename"
        :username="card.username"
        :model="card.model"
        :image="card.image"
        :infTime="card.infTime"
      />
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue';
import DetectorCard from '@/components/atoms/DetectorCard.vue';
import detectorTypeImage from '@/assets/icons/detector-type.webp';
import yolov5ModelImage from '@/assets/images/yolov5.webp';
import yolov8ModelImage from '@/assets/images/yolov8.webp';
import placeholderImage from '@/assets/images/placeholder.png';

const cards = reactive([
  {
    type: detectorTypeImage,
    filename: 'filename1',
    username: 'Anonymous1',
    model: yolov5ModelImage,
    image: placeholderImage,
    infTime: 0.983
  },
  {
    type: detectorTypeImage,
    filename: 'filename2',
    username: 'Anonymous2',
    model: yolov5ModelImage,
    image: placeholderImage,
    infTime: 0.634
  },
  {
    type: detectorTypeImage,
    filename: 'filename3',
    username: 'Anonymous3',
    model: yolov8ModelImage,
    image: placeholderImage,
    infTime: 0.534
  }
]);
</script>

<style scoped>
.results-others-container {
  display: flex;
  align-items: center;
  flex-direction: column;
  margin-top: 100px;
  width: 200%;
}

.results-others-title h1 {
  display: flex;
  line-height: 1.3;
  font-size: 2.8rem;
  font-weight: 500;
}

.results-others-cards {
  display: flex;
  justify-content: center;
  gap: 16px;
  flex-wrap: wrap;
  max-width: 1200px;
}

.vd-card {
  width: calc(33.333% - 11px);
  box-sizing: border-box;
  margin-bottom: 16px;
}

</style>
