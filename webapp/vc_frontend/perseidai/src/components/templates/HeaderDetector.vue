<template>
  <div class="header-detector-container">
    <div class="header-detector-icon">
      <img src="@/assets/icons/detector-type.webp" alt="Detector logo" />
    </div>
    <h1 class="header-detector-title">
      Available
      <span>&nbsp;Detection&nbsp;</span>
      Models
    </h1>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.header-detector-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 9rem;
  margin-left: 10rem;
  margin-top: -4rem;
  width: 100%;
}

.header-detector-icon img {
  height: 90px;
  width: auto;
}

.header-detector-title {
  display: flex;
  line-height: 1.3;
  font-size: 2.8rem;
  font-weight: 500;
  color: #232323;
  text-align: center;
}

.header-detector-title span {
  font-weight: inherit;
  color: #00acea;
}
</style>
