<template>
  <div class="home-container">
    <!-- Main Header: Title and Image -->
    <div class="home-title">
      <h1>
        <div class="line-first">
          <span>Test Real-Time</span>
          <span class="text-ai"><i> AI</i></span>
          <span> Vehicle</span>
        </div>
        <div class="line-second">
          <span class="text-detection"> Detection</span>
          <span> and</span>
          <span class="text-classification"> Classification</span>
        </div>
        <div class="line-third">
          <span> Models.</span>
        </div>
      </h1>
    </div>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.home-container {
  display: flex;
  flex-direction: column;
  align-items: left;
  width: 100%;
}

.home-title {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: left;
  font-size: 22px;
  margin-right: 5vh;
}

.home-title h1 {
  line-height: 1.3;
  font-size: 2.8rem;
}

.text-ai {
  color: #02af98;
}

.text-detection {
  color: #00acea;
}

.text-classification {
  color: #083863;
}

@media (max-width: 1024px) {
  .home-title {
    padding-top: 50px;
  }
}
</style>
