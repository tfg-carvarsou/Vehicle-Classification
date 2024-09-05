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
          v-for="(vdcard, index) in detectorCards"
          :key="index"
          :type="vdcard.type"
          :filename="vdcard.filename"
          :username="vdcard.username"
          :model="vdcard.model"
          :image="vdcard.image"
          :infTime="vdcard.infTime"
        />
      </div>
      <div class="classifier-card-list" v-if="isClassificatorCardListShown">
        <div class="results-others-title" v-if="!isHomeView">
          <h1>
            See results of
            <span class="classifier-title">&nbsp;Classifier&nbsp;</span>
            uploads
          </h1>
        </div>
        <ClassificatorCard
          v-for="(vccard, index) in classifierCards"
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
import { ref, onMounted } from 'vue'
import { DetectorService, ClassifierService } from '@/api/index'
import type { VDImageGet, VCImageGet } from '@/api/index'
import DetectorCard from '@/components/organisms/DetectorCard.vue'
import ClassificatorCard from '@/components/organisms/ClassificatorCard.vue'
import detectorTypeImage from '@/assets/icons/detector-type.webp'
import classificatorTypeImage from '@/assets/icons/classifier-type.webp'
import yolov5ModelImage from '@/assets/images/yolov5.webp'
import yolov8ModelImage from '@/assets/images/yolov8.webp'
import effnetModelImage from '@/assets/images/effnet.webp'

const detectorCards = ref<any[]>([])
const classifierCards = ref<any[]>([])

async function generateCards(service: any): Promise<any[]> {
  let cards: any[] = [];
  //TODO: Iterate over their correspondant images in each service
  
  if (service == DetectorService) {
    const detectorListAll: VDImageGet[] = await service.detectorSnapzoneList();
    const oneImage = detectorListAll[0];
    cards = [
      {
        type: detectorTypeImage,
        filename: oneImage.image.split('/')[6].split('.')[0],
        username: 'Anonymous',
        model: oneImage.model === 'YOLOv5s' ? yolov5ModelImage : yolov8ModelImage,
        image: oneImage.image,
        infTime: oneImage.inf_time
        // TODO: Add label_count_dict
      }
    ];
  }
  
  if (service == ClassifierService) {
    const classifierListAll: VCImageGet[] = await service.classifierSnapzoneList();
    const oneImage = classifierListAll[0];
    cards = [
      {
        type: classificatorTypeImage,
        filename: oneImage.image.split('/')[6].split('.')[0],
        username: 'Anonymous',
        model: oneImage.model === 'EfficientNetB1' ? effnetModelImage : yolov8ModelImage,
        image: oneImage.image,
        infTime: oneImage.inf_time
        // TODO: Add pred_class
      }
    ];
  }
  
  return cards;
}

const props = defineProps<{
  isHomeView: boolean
  isDetectorCardListShown: boolean
  isClassificatorCardListShown: boolean
}>()

onMounted(async () => {
  if (props.isDetectorCardListShown) {
    detectorCards.value = await generateCards(DetectorService);
  }
  if (props.isClassificatorCardListShown) {
    classifierCards.value = await generateCards(ClassifierService);
  }
})
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

.classifier-title {
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
.classifier-card-list {
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
