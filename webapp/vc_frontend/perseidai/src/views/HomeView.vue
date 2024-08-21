<template>
  <div class="main-header">
    <h1>
      <div v-if="showLine1" class="typing-effect line-1">
        <span>Test Real-Time</span>
        <span class="mh-1"><i> AI</i></span>
        <span> Vehicle</span>
      </div>
      <div v-if="showLine2" class="typing-effect line-2">
        <span class="mh-2"> Detection</span>
        <span> and</span>
        <span class="mh-3"> Classification</span>
      </div>
      <div v-if="showLine3" class="typing-effect line-3">
        <span> Models.</span>
      </div>
    </h1>
  </div>
</template>

<script setup lang="ts">
import { ref, onMounted } from 'vue'
const showLine1 = ref(false)
const showLine2 = ref(false)
const showLine3 = ref(false)

onMounted(() => {
  setTimeout(() => {
    showLine1.value = true
  }, 0)

  setTimeout(() => {
    showLine2.value = true
  }, 1900)

  setTimeout(() => {
    showLine3.value = true
  }, 3800)
})
</script>

<style scoped>
.main-header {
  display: inline-block;
  height: 100vh;
  padding-top: 100px;
  font-size: 22px;
  color: #232323;
}

.typing-effect {
  overflow: hidden;
  white-space: nowrap;
  font-size: inherit;
  border-right: 2px solid #232323;
}

/* Individual line animations */
.line-1 {
  animation:
    typing 2s steps(30) forwards,
    blink 1.75s steps(1) forwards;
}

.line-2 {
  animation:
    typing 2s steps(30) forwards,
    blink 1.8s steps(1) forwards;
}

.line-3 {
  animation:
    typing 2s steps(30) forwards,
    blink 0.55s steps(1) forwards;
}

.line-1,
.line-2,
.line-3 {
  margin-right: 15vh;
}

/* Animation for typing effect */
@keyframes typing {
  from {
    width: 0;
  }
  to {
    width: 100%;
  }
}

/* Animation to hide the cursor */
@keyframes blink {
  from {
    border-right-color: #232323;
  }
  to {
    border-right-color: transparent;
  }
}

.mh-1 {
  color: #02af98;
}

.mh-2 {
  color: #00acea;
}

.mh-3 {
  color: #083863;
}
</style>
