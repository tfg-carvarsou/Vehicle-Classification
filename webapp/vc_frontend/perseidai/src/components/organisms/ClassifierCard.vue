<template>
  <div class="vccard">
    <div class="vccard-header">
      <div class="vccard-type">
        <img :src="type" alt="Card type" />
      </div>
      <div class="vccard-info">
        <div class="filename">{{ filename }}</div>
        <div class="username">{{ username }}</div>
      </div>
      <div class="vccard-model">
        <img :src="model" alt="Card model" />
      </div>
    </div>
    <div class="vccard-image">
      <CardDialog alt="Uploaded image" :filename="filename" :image="image" />
    </div>
    <div class="vccard-footer">
      <div class="prediction label">
        <i>{{ predClass }}</i>
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
  predClass: string
}

defineProps<Props>()
</script>

<style scoped>
.vccard {
  background-color: white;
  border-radius: 8px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.15);
  padding: 16px;
  width: 32.4%;
}

.vccard-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 16px;
}

.vccard-type,
.vccard-model {
  display: flex;
  align-items: center;
}

.vccard-type img {
  width: 60px;
  height: auto;
}

.vccard-model img {
  width: 156px;
  height: auto;
  max-height: 100px;
  margin-left: 45px;
  border-radius: 8px;
}

.vccard-info {
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

.vccard-image {
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

.vccard-image img {
  max-width: 100%;
  max-height: 100%;
  object-fit: cover;
  border-radius: 8px;
}

.vccard-footer {
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.prediction {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
}

.label {
  font-weight: bold;
  font-size: 16px;
}

.inf-time {
  font-size: 14px;
  color: #777;
}
</style>
