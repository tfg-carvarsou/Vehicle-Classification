<template>
  <div class="vdcard">
    <div class="vdcard-header">
      <div class="vdcard-type">
        <img :src="type" alt="Card type" />
      </div>
      <div class="vdcard-info">
        <div class="filename">{{ filename }}</div>
        <div class="username">{{ username }}</div>
      </div>
      <div class="vdcard-model">
        <img :src="model" alt="Card model" />
      </div>
    </div>
    <div class="vdcard-image">
      <CardDialog alt="Uploaded image" :filename="filename" :image="image" />
    </div>
    <div class="vdcard-footer">
      <div class="detections">
        <div class="detection" v-for="(detection, index) in detections" :key="index">
          <div class="count" :style="{ backgroundColor: detection.color }">
            {{ detection.count }}
          </div>
          <div class="label">{{ detection.label }}</div>
        </div>
      </div>
      <div class="inf-time">{{ infTime }}ms</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { reactive } from 'vue'
import CardDialog from '@/components/molecules/CardDialog.vue'

interface Props {
  type: string
  filename: string
  username: string
  model: string
  image: string
  infTime: number
}

defineProps<Props>()

const detections = reactive([
  {
    count: 12,
    label: 'car',
    color: '#f44336'
  },
  { count: 1, label: 'big truck', color: '#4caf50' },
  { count: 3, label: 'small bus', color: '#2196f3' }
])
</script>

<style scoped>
.vdcard {
  margin-top: 32px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
  padding: 16px;
  width: 33%;
}

.vdcard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.vdcard-type,
.vdcard-model {
  display: flex;
  align-items: center;
}

.vdcard-type img {
  width: 60px;
  height: auto;
}

.vdcard-model img {
  width: 156px;
  height: auto;
  max-height: 100px;
  margin-left: 45px;
  border-radius: 8px;
}

.vdcard-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  margin-right: auto;
  padding-left: 16px;
}

.filename {
  font-weight: bold;
  font-size: 18px;
}

.username {
  font-size: 14px;
  color: #777;
}

.vdcard-image {
  width: 100%;
  height: 200px;
  background-color: #f2f2f2;
  border-radius: 8px;
  margin-bottom: 16px;
  overflow: hidden;
  display: flex;
  align-items: center;
  justify-content: center;
}

.vdcard-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  border-radius: 8px;
}

.vdcard-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.detections {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.detection {
  display: flex;
  align-items: center;
  margin-bottom: 8px;
}

.count {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 30px;
  height: 30px;
  border-radius: 50%;
  font-size: 14px;
  margin-right: 8px;
}

.label {
  font-size: 14px;
}

.inf-time {
  font-size: 14px;
  color: #777;
  margin-bottom: 100px;
}
</style>
