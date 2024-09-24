<template>
  <DialogRoot>
    <DialogTrigger class="card-dialog-trigger button green"> Check results </DialogTrigger>
    <DialogPortal>
      <DialogOverlay class="card-dialog-overlay" />
      <DialogContent class="card-dialog-content">
        <div class="card-dialog-header">
          <DialogTitle class="card-dialog-title">Inference Results</DialogTitle>
          <DialogClose class="close-button">
            <FontAwesomeIcon class="close-button-icon" :icon="fas.faClose" />
          </DialogClose>
        </div>
        <DialogDescription class="card-dialog-description">
          <div v-if="type === 'detector'">
            <DetectorCard
              :type="detectorTypeImage"
              :filename="filename.slice(0, filename.lastIndexOf('.'))"
              :username="'Anonymous'"
              :model="model"
              :image="responseVDImage.image"
              :infTime="responseVDImage.inf_time ?? 0"
              :labelCountDict="responseVDImage.label_count_dict ?? {}"
            />
          </div>
          <div v-else-if="type === 'classifier'">
            <ClassifierCard
              :type="classifierTypeImage"
              :filename="filename.slice(0, filename.lastIndexOf('.'))"
              :username="'Anonymous'"
              :model="model"
              :image="responseVCImage.image"
              :infTime="responseVCImage.inf_time ?? 0"
              :predClass="responseVCImage.pred_class ?? ''"
            />
          </div>
        </DialogDescription>
      </DialogContent>
    </DialogPortal>
  </DialogRoot>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { DetectorService, ClassifierService } from '@/api/index'
import type { VDImage, VCImage } from '@/api/index'
import {
  DialogClose,
  DialogContent,
  DialogDescription,
  DialogOverlay,
  DialogPortal,
  DialogRoot,
  DialogTitle,
  DialogTrigger
} from 'radix-vue'
import DetectorCard from '@/components/organisms/DetectorCard.vue'
import ClassifierCard from '@/components/organisms/ClassifierCard.vue'
import detectorTypeImage from '@/assets/icons/detector-type.webp'
import classifierTypeImage from '@/assets/icons/classifier-type.webp'
import yolov5ModelImage from '@/assets/images/yolov5.webp'
import yolov8ModelImage from '@/assets/images/yolov8.webp'
import effnetModelImage from '@/assets/images/effnet.webp'

const props = defineProps<{
  type: string
  filename: string
  username: string
  code: string
}>()
let model = ''

let responseVDImage = ref<VDImage>({
  code: '',
  model: undefined,
  image: '',
  inf_time: 0,
  label_count_dict: {}
})

let responseVCImage = ref<VCImage>({
  code: '',
  model: undefined,
  image: '',
  inf_time: 0,
  pred_class: ''
})

async function getUploadedVDImage(): Promise<void> {
  responseVDImage.value = await DetectorService.detectorSnapviewRetrieve(props.code)
}

async function getUploadedVCImage(): Promise<void> {
  responseVCImage.value = await ClassifierService.classifierSnapviewRetrieve(props.code)
}

onMounted(() => {
  if (props.type === 'detector') {
    getUploadedVDImage()
    model = responseVDImage.value.model === 'YOLOv5s' ? yolov5ModelImage : yolov8ModelImage
  } else if (props.type === 'classifier') {
    getUploadedVCImage()
    model = responseVCImage.value.model === 'EfficientNetB1' ? effnetModelImage : yolov8ModelImage
  }
})
</script>

<style scoped>
.card-dialog-trigger {
  font: inherit;
  border: none;
}

.button {
  padding: 4px 8px;
  font-size: 16px;
  font-weight: 500;
  line-height: 1;
  color: #ffffff;
  background-color: #ef4444;
  border: none;
  border-radius: 4px;
  height: 32px;
  cursor: pointer;
  transition:
    background-color 0.3s ease,
    transform 0.2s ease;
}

.button.green {
  background-color: #02af98;
  color: #ffffff;
}

.button.green:hover {
  background-color: #027666;
  transform: translateY(-2px);
}

.card-dialog-overlay {
  background-color: rgba(0, 0, 0, 0.6);
  position: fixed;
  inset: 0;
  animation: overlayShow 150ms cubic-bezier(0.16, 1, 0.3, 1);
}

.card-dialog-content {
  background-color: #ffffff;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  position: fixed;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  width: 90vw;
  max-width: 500px;
  max-height: 85vh;
  padding: 20px;
  animation: contentShow 150ms cubic-bezier(0.16, 1, 0.3, 1);
  text-align: center;
  color: #083863;
}

.card-dialog-header {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  margin-bottom: 16px;
}

.card-dialog-title {
  font-size: 24px;
  font-weight: bold;
  color: #083863;
}

.close-button {
  all: unset;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  left: 95%;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: transparent;
  transition:
    background-color 0.3s ease,
    transform 0.2s ease;
}

.close-button:hover {
  background-color: rgba(8, 56, 99, 0.1);
  transform: scale(1.1);
}

.close-button-icon {
  font-size: 16px;
  transition: color 0.3s ease;
}

.card-dialog-description div {
  display: flex;
  flex-direction: column;
  width: 100%;
}

@keyframes overlayShow {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes contentShow {
  from {
    opacity: 0;
    transform: translate(-50%, -48%) scale(0.96);
  }
  to {
    opacity: 1;
    transform: translate(-50%, -50%) scale(1);
  }
}
</style>
