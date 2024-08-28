<template>
    <div class="results-others-container">
        <div class="results-others-title">
            <h1>See results of others uploads</h1>
        </div>

        <!-- Size three array of results -->
        <div class="results-others-cards"">
            <DetectorCard />
        </div> 

    </div>
</template>

<script lang="ts">
// @ts-ignore
import DetectorCard from '@/components/atoms/DetectorCard.vue'

export default {
    name: 'ResultsOthers',
    data() {
      return {
        cards: [
          { type: '@/assets/icons/detector-type.webp', 
            filename: 'filename1', 
            username: 'Anonymous1',
            model: '@/assets/images/yolov5.webp',
            image: '@/assets/images/placeholder.png',
            },
            { type: '@/assets/icons/detector-type.webp', 
            filename: 'filename2', 
            username: 'Anonymous2',
            model: '@/assets/images/yolov5.webp',
            image: '@/assets/images/placeholder.png',
            },
            { type: '@/assets/icons/detector-type.webp', 
            filename: 'filename3', 
            username: 'Anonymous3',
            model: '@/assets/images/yolov8.webp',
            image: '@/assets/images/placeholder.png',
            },
        ]
      }
    }
}
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
</style>