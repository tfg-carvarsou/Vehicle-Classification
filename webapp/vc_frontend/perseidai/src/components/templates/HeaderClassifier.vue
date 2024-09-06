<template>
  <div class="header-classifier-container">
    <div class="header-classifier-icon">
      <img src="@/assets/icons/classifier-type.webp" alt="Classifier logo" />
    </div>
    <h1 class="header-classifier-title">
      Available
      <span>&nbsp;Classification&nbsp;</span>
      Models
    </h1>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.header-classifier-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 9rem;
  margin-left: 10rem;
  margin-top: -4rem;
  width: 100%;
}

.header-classifier-icon img {
  height: 90px;
  width: auto;
}

.header-classifier-title {
  display: flex;
  flex-wrap: wrap;
  line-height: 1.3;
  font-size: 2.8rem;
  font-weight: 500;
  color: #232323;
  text-align: center;
}

.header-classifier-title span {
  font-weight: inherit;
  color: #083863;
}
</style>
