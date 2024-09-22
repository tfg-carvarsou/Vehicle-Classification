<template>
  <Suspense>
    <div class="models-view-container">
      <div class="models-view-section">
        <HeaderDetector />
        <div class="models-image-container">
          <img src="@/assets/images/yolov5.webp" class="mv-img" alt="YOLOV5s detector image" />
          <img src="@/assets/images/yolov8.webp" class="mv-img" alt="YOLOV8s detector image" />
        </div>
        <span class="mv-text">
          Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem
          Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
          impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de
          textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo
          sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos
          electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la
          creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más
          recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual
          incluye versiones de Lorem Ipsum.
        </span>
      </div>
      <div class="models-view-section">
        <HeaderClassifier />
        <div class="models-image-container">
          <img
            src="@/assets/images/effnet.webp"
            class="mv-img"
            alt="EfficientNetB1 detector image"
          />
          <img src="@/assets/images/yolov8.webp" class="mv-img" alt="YOLOV8s-cls detector image" />
        </div>
        <span class="mv-text">
          Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. Lorem
          Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, cuando un
          impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una galería de
          textos y los mezcló de tal manera que logró hacer un libro de textos especimen. No sólo
          sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos
          electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la
          creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más
          recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual
          incluye versiones de Lorem Ipsum.
        </span>
      </div>
    </div>
  </Suspense>
</template>

<script setup lang="ts">
import HeaderDetector from '@/components/templates/HeaderDetector.vue'
import HeaderClassifier from '@/components/templates/HeaderClassifier.vue'
</script>

<style scoped>
.models-view-container {
  display: flex;
  justify-content: space-between;
  width: 100%;
  margin: 0 auto;
  padding: 0 20px;
  margin-top: 6rem;
}

.models-view-section {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  text-align: center;
  margin-inline: 50px;
  margin-left: -5px;
}

.models-image-container {
  display: flex;
  gap: 20px;
  justify-content: center;
}

.mv-img {
  width: 256px;
  height: 174px;
  border-radius: 30px;
  box-shadow: 0 4px 4px rgba(0, 0, 0, 0.5);
  margin-top: 2rem;
}

.mv-text {
    font-size: 16px;
    color: #083863;
    margin-top: 3rem;
    margin-bottom: 10rem;
}

:deep(.header-detector-container),
:deep(.header-classifier-container) {
  margin: 0 auto;
}
</style>
