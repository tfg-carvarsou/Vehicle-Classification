<template>
  <AlertDialogRoot>
    <AlertDialogTrigger class="button green">
      <FontAwesomeIcon :icon="fas.faFileUpload" /> Upload image
    </AlertDialogTrigger>
    <AlertDialogPortal>
      <AlertDialogOverlay class="alert-dialog-overlay" />
      <AlertDialogContent class="alert-dialog-content">
        <AlertDialogTitle class="alert-dialog-title">Confirm uploading this image</AlertDialogTitle>
        <div class="alert-dialog-image">
          <img :src="props.image || '@/assets/images/placeholder.png'" alt="Uploaded image" />
        </div>
        <AlertDialogDescription class="alert-dialog-description">
          By clicking "Upload now", you agree to our
          <router-link to="/terms-of-service" target="_blank" class="copyright-links">
            Terms of Service
          </router-link>
        </AlertDialogDescription>
        <div class="alert-dialog-actions">
          <AlertDialogCancel class="button mauve">Cancel</AlertDialogCancel>
          <AlertDialogAction class="button green" @click="uploadImage">
            <FontAwesomeIcon :icon="fas.faFileUpload" /> Upload now
          </AlertDialogAction>
        </div>
      </AlertDialogContent>
    </AlertDialogPortal>
  </AlertDialogRoot>
</template>

<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { DetectorService, VDModelEnum, VCModelEnum } from '@/api/index'
import type { VDImagePostRequest } from '@/api/index'
import {
  AlertDialogAction,
  AlertDialogCancel,
  AlertDialogContent,
  AlertDialogDescription,
  AlertDialogOverlay,
  AlertDialogPortal,
  AlertDialogRoot,
  AlertDialogTitle,
  AlertDialogTrigger
} from 'radix-vue'

const props = defineProps<{
  modelType: string
  modelSeries: string
  image: string | null
}>()

async function getBlobImage(): Promise<Blob> {
  return await fetch(props.image as string).then((res) => res.blob())
}

async function uploadImage() {
  let image: Blob = await getBlobImage()
  const file = new File([image], 'upload.jpg', { type: image.type })

  if (props.modelType === 'detector') {
    let model: VDModelEnum | undefined = undefined
    switch (props.modelSeries) {
      case 'yolov5':
        model = VDModelEnum.YOLOV5S
        break
      case 'yolov8':
        model = VDModelEnum.YOLOV8S
        break
      default:
        console.error('Invalid detection model series selected')
    }

    const formData: VDImagePostRequest = {
      model: model,
      image: file
    }
    DetectorService.detectorSnapzoneCreate(formData)
      .then((response) => {
        console.log(response) //todel
      })
      .catch((error) => {
        console.error('Error handling the upload request:', error)
      })
  } else if (props.modelType === 'classifier') {
    let model: VCModelEnum
    switch (props.modelSeries) {
      case 'effnet':
        console.log('EfficientNetB1 model selected')
        model = VCModelEnum.EFFICIENT_NET_B1
        break
      case 'yolov8cls':
        console.log('YOLOv8s-cls model selected')
        model = VCModelEnum.YOLOV8S_CLS
        break
      default:
        console.error('Invalid classification model series selected')
    }
  } else {
    console.error('Invalid model type selected')
  }
}
</script>

<style scoped>
button {
  all: unset;
  cursor: pointer;
}

.alert-dialog-overlay {
  background-color: rgba(0, 0, 0, 0.6);
  position: fixed;
  inset: 0;
  animation: overlayShow 150ms cubic-bezier(0.16, 1, 0.3, 1);
}

.alert-dialog-content {
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

.alert-dialog-content:focus {
  outline: none;
}

.alert-dialog-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 8px;
  color: #083863;
}

.alert-dialog-image {
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: 100%;
  max-height: 49vh;
  margin-bottom: 8px;
  overflow: hidden;
}

.alert-dialog-image img {
  max-width: 100%;
  height: auto;
}

.alert-dialog-description {
  font-size: 16px;
  line-height: 1.5;
  margin-bottom: 20px;
  color: #083863;
}

.button {
  padding: 4px 8px;
  font-size: 14px;
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

.button.mauve {
  background-color: #cccccc;
  color: #333333;
}

.button.mauve:hover {
  background-color: #bbbbbb;
}

.alert-dialog-actions {
  display: flex;
  gap: 15px;
  justify-content: flex-end;
  margin-top: 20px;
}

@keyframes overlayShow {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

/* Content Animation */
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
