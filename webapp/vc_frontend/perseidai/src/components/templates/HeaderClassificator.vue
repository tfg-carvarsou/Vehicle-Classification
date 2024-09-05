<template>
  <div class="header-classificator-container">
    <div class="header-classificator-icon">
      <img src="@/assets/icons/classificator-type.webp" alt="Classificator logo" />
    </div>
    <h1 class="header-classificator-title">
      Available
      <span>&nbsp;Classification&nbsp;</span>
      Models
    </h1>
  </div>
</template>

<script setup lang="ts"></script>

<style scoped>
.header-classificator-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 9rem;
  margin-left: 10rem;
  margin-top: -4rem;
  width: 100%;
}

.header-classificator-icon img {
  height: 90px;
  width: auto;
}

.header-classificator-title {
  display: flex;
  flex-wrap: wrap;
  line-height: 1.3;
  font-size: 2.8rem;
  font-weight: 500;
  color: #232323;
  text-align: center;
}

.header-classificator-title span {
  font-weight: inherit;
  color: #083863;
}
</style>
