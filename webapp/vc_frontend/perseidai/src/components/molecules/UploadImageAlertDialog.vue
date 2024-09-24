<template>
  <AlertDialogRoot :open="isDialogOpen">
    <AlertDialogTrigger class="button green" @click="openDialog">
      <FontAwesomeIcon :icon="fas.faFileUpload" /> Upload image
    </AlertDialogTrigger>
    <AlertDialogPortal>
      <AlertDialogOverlay class="alert-dialog-overlay" />
      <AlertDialogContent class="alert-dialog-content" v-if="!isInferenceDeleted">
        <AlertDialogTitle class="alert-dialog-title">
          <div v-if="!isImageUploaded">Confirm uploading this image</div>
          <div v-else>
            <FontAwesomeIcon :icon="fas.faCheck" :style="{ color: 'green' }" />
            Image uploaded successfully
          </div>
        </AlertDialogTitle>
        <div class="alert-dialog-image" v-if="!isImageUploaded">
          <img :src="props.image || 'https://via.placeholder.com/500'" alt="Uploaded image" />
        </div>
        <AlertDialogDescription class="alert-dialog-description" v-if="!isImageUploaded">
          By clicking "Upload now", you agree to our
          <router-link to="/terms-of-service" target="_blank" class="copyright-links">
            Terms of Service
          </router-link>
        </AlertDialogDescription>
        <div v-if="showCardDialog">
          <CardDialog
            :type="modelType"
            :filename="imageName"
            :username="'Anonymous'"
            :code="imageCode"
          />
        </div>
        <div v-if="!showCardDialog && isImageUploaded">
          <img src="@/assets/preloaders/spinner.gif" class="load-spinner" alt="Loading..." />
        </div>
        <div class="alert-dialog-actions">
          <div v-if="isImageUploaded">
            <button class="button red" @click="deleteInference">
              <FontAwesomeIcon :icon="fas.faEraser" /> Delete inference
            </button>
            <AlertDialogCancel class="button mauve" @click="closeRefreshDialog">
              Close
            </AlertDialogCancel>
          </div>
          <div v-else>
            <AlertDialogCancel class="button mauve" @click="closeDialog">
              Cancel
            </AlertDialogCancel>
            <AlertDialogAction class="button green" @click="uploadImage">
              <FontAwesomeIcon :icon="fas.faFileUpload" /> Upload now
            </AlertDialogAction>
          </div>
        </div>
      </AlertDialogContent>
      <DeleteAlertMessage
        v-if="isInferenceDeleted"
        :showAlert="isInferenceDeleted"
        :message="deleteAlertMessage"
      />
    </AlertDialogPortal>
  </AlertDialogRoot>
</template>

<script setup lang="ts">
import { ref, watch } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { DetectorService, ClassifierService, VDModelEnum, VCModelEnum } from '@/api/index'
import type { VDImagePostRequest, VCImagePostRequest } from '@/api/index'
import DeleteAlertMessage from '@/components/atoms/DeleteAlertMessage.vue'
import CardDialog from '@/components/molecules/CardDialog.vue'
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
  imageName: string
}>()

const isDialogOpen = ref(false)
const isImageUploaded = ref(false)
const showCardDialog = ref(false)
const isInferenceDeleted = ref(false)
let deleteAlertMessage = ref('Deleted successfully')
let imageCode = 'undefined'

function openDialog() {
  isDialogOpen.value = true
}

function closeDialog() {
  isDialogOpen.value = false
  isImageUploaded.value = false
  showCardDialog.value = false
}

function closeRefreshDialog() {
  closeDialog()
  location.reload()
}

async function deleteInference(): Promise<void> {
  if (props.modelType === 'detector') {
    try {
      await DetectorService.detectorSnapviewDestroy(imageCode)
      deleteAlertMessage.value = 'Detector inference deleted successfully'
    } catch (error) {
      console.error('Error handling the detector delete request:', error)
    }
  } else if (props.modelType === 'classifier') {
    try {
      await ClassifierService.classifierSnapviewDestroy(imageCode)
      deleteAlertMessage.value = 'Classifier inference deleted successfully'
    } catch (error) {
      console.error('Error handling the classifier delete request:', error)
    }
  } else {
    console.error('Invalid model type selected')
  }
  isInferenceDeleted.value = true
}

async function getBlobImage(): Promise<Blob> {
  return await fetch(props.image as string).then((res) => res.blob())
}

async function uploadImage(): Promise<void> {
  let blob: Blob = await getBlobImage()
  const file = new File([blob], props.imageName, { type: blob.type })

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
    try {
      const response = await DetectorService.detectorSnapzoneCreate(formData)
      imageCode = response.code
      isImageUploaded.value = true
    } catch (error) {
      console.error('Error handling the detector upload request:', error)
    }
  } else if (props.modelType === 'classifier') {
    let model: VCModelEnum | undefined = undefined
    switch (props.modelSeries) {
      case 'effnet':
        model = VCModelEnum.EFFICIENT_NET_B1
        break
      case 'yolov8cls':
        model = VCModelEnum.YOLOV8S_CLS
        break
      default:
        console.error('Invalid classification model series selected')
    }
    const formData: VCImagePostRequest = {
      model: model,
      image: file
    }
    try {
      const response = await ClassifierService.classifierSnapzoneCreate(formData)
      imageCode = response.code
      isImageUploaded.value = true
    } catch (error) {
      console.error('Error handling the classifier upload request:', error)
    }
  } else {
    console.error('Invalid model type selected')
  }
}

watch(isImageUploaded, (newValue) => {
  if (newValue) {
    setTimeout(() => {
      showCardDialog.value = true
    }, 1000)
  }
})

watch(isInferenceDeleted, (newValue) => {
  if (newValue) {
    setTimeout(() => {
      closeRefreshDialog()
    }, 3000)
  }
})
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

.load-spinner {
  width: 50px;
  height: auto;
  margin: 0 auto;
}

.alert-dialog-actions {
  display: flex;
  gap: 15px;
  justify-content: flex-end;
  margin-top: 20px;
}

.alert-dialog-actions > div {
  display: flex;
  gap: 15px;
}

.button {
  padding: 4px 8px;
  font-size: 14px;
  font-weight: 500;
  line-height: 1;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  height: 32px;
  cursor: pointer;
  transition:
    background-color 0.3s ease,
    transform 0.2s ease;
}

.button.red {
  background-color: #ef4444;
  margin-right: 256px;
}

.button.red:hover {
  background-color: #dc2626;
  transform: translateY(-2px);
}

.button.mauve {
  background-color: #cccccc;
  color: #333333;
}

.button.mauve:hover {
  background-color: #bbbbbb;
}

.button.green {
  background-color: #02af98;
  color: #ffffff;
}

.button.green:hover {
  background-color: #027666;
  transform: translateY(-2px);
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
