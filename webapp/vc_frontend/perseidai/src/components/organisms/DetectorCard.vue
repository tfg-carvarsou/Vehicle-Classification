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
          <div
            class="count"
            :style="{ backgroundColor: detection.bgColor, color: detection.color }"
          >
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
import CardDialog from '@/components/molecules/CardDialog.vue'

interface Props {
  type: string
  filename: string
  username: string
  model: string
  image: string
  infTime: number
  labelCountDict: Record<string, number>
}

const props = defineProps<Props>()
let detections: any[] = []
const colorList = ['#111f64', '#cced00', '#02f33f', '#c100ff']

function isLightColor(color: string): boolean {
  const hex = color.replace('#', '')
  const r = parseInt(hex.slice(0, 2), 16)
  const g = parseInt(hex.slice(2, 4), 16)
  const b = parseInt(hex.slice(4, 6), 16)
  const brightness = (r * 299 + g * 587 + b * 114) / 1000
  return brightness > 128
}
function getTextColor(backgroundColor: string): string {
  return isLightColor(backgroundColor) ? 'black' : 'white'
}

for (const [label, count] of Object.entries(props.labelCountDict)) {
  const bgColor = colorList[detections.length % colorList.length]
  detections.push({
    count,
    label: label.split(';')[1],
    bgColor,
    color: getTextColor(bgColor)
  })
}
</script>

<style scoped>
.vdcard {
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
  font-weight: bold;
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
