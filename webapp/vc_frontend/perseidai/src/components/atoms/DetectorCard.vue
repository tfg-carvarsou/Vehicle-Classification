<template>
  <div class="vd-card">
    <div class="vdcard-header">
      <div class="vdcard-type">
        <img :src="props.type" />
      </div>
      <div class="vdcard-info">
        <div class="filename">{props.filename}</div>
        <div class="username">Anonymous</div>
      </div>
      <div class="vdcard-model">
        <img src="@/assets/images/yolov5.webp" />
      </div>
    </div>
    <div class="vdcard-image">
      <span>Placeholder</span>
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
      <div class="inf-time">0.983ms</div>
    </div>
  </div>
</template>

<script>
export default {
  name: 'DetectorCard',
  data() {
    return {
      detections: [
        { count: 12, label: 'car', color: '#f44336' },
        { count: 1, label: 'big truck', color: '#4caf50' },
        { count: 3, label: 'small bus', color: '#2196f3' }
      ]
    }
  }
}

props = defineProps<{
  type: string,
  filename: string, 
  username: string,
  model: string,
  image: string
}>
</script>

<style scoped>
.vd-card {
  margin-top: 32px;
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 16px;
  width: 500px;
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
  margin-left: auto;
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
  height: 200px;
  background-color: #f2f2f2;
  border-radius: 8px;
  margin-bottom: 16px;
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
}
</style>
