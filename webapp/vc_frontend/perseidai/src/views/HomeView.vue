<template>
  <div class="view-container">
    <!-- Main Header: Title and Image -->
    <div class="mh-container">
      <div class="mh-title">
        <h1>
          <div class="mh-line-1">
            <span>Test Real-Time</span>
            <span class="mh-text-1"><i> AI</i></span>
            <span> Vehicle</span>
          </div>
          <div class="mh-line-2">
            <span class="mh-text-2"> Detection</span>
            <span> and</span>
            <span class="mh-text-3"> Classification</span>
          </div>
          <div class="mh-line-3">
            <span> Models.</span>
          </div>
        </h1>
          <!-- Subtitle: Try it out and selector -->
        <div class="sb-container">
          <h2 class="sb-title">Try it out</h2>
          <select class="sb-type-selector">
            <option value="sb-type-detector">Detector</option>
            <option value="sb-type-classificator">Classificator</option>
          </select>
        </div>
      </div>
      <div class="mh-img">
        <img src="@/assets/images/placeholder.png" alt="placeholder" />
      </div>
    </div>
  </div>
</template>

<!-- 
TODO: 
    -> Al seleccionar entre Detector o Classificator,
       hay un scroll automatico que lleva al selector de modelos
    -> Al seleccionar entre modelos, 
       aparece el campo de subida de imagen
    -> Al subir la imagen, aparece el resultado de la inferencia
-->

<script setup lang="ts">
</script>

<style scoped>
.view-container {
  color: #232323;
}

.mh-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  height: 60vh;
  width: auto;
  flex-wrap: wrap;
}

.mh-title {
  flex: 1;
  display: inline-block;
  flex-direction: column;
  align-items: center;
  font-size: 22px;
  margin-right: 5vh;
}

.mh-text-1 {
  color: #02af98;
}

.mh-text-2 {
  color: #00acea;
}

.mh-text-3 {
  color: #083863;
}

.mh-img img {
  flex: 1;
  max-width: 100%;
  height: auto;
  object-fit: cover;
}

.sb-container {
  display: flex;
  flex-direction: column;
  align-items: left;
  margin-top: 20px;
  color: #083863;
}

h1 {
  line-height: 1.3;
  font-size: 2.8rem;
}

@media (max-width: 1024px) {
  .mh-container {
    flex-direction: row;
    align-items: center;
  }

  .mh-title {
    height: auto;
    padding-top: 50px;
  }

  .mh-img img {
    width: 100%;
  }
}
</style>
