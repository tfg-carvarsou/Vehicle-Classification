<template>
  <DialogRoot>
    <DialogTrigger class="dialog-trigger">
      <img :src="image" alt="Open Image" />
    </DialogTrigger>
    <DialogPortal>
      <DialogOverlay class="dialog-overlay" />
      <DialogContent class="dialog-content">
        <div class="dialog-header">
          <DialogTitle class="dialog-title">
            {{ filename }}
          </DialogTitle>
          <DialogClose class="close-button">
            <FontAwesomeIcon class="close-button-icon" :icon="fas.faClose" />
          </DialogClose>
        </div>
        <div class="dialog-image">
          <img :src="image" alt="Image preview" />
        </div>
      </DialogContent>
    </DialogPortal>
  </DialogRoot>
</template>

<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import {
  DialogClose,
  DialogContent,
  DialogOverlay,
  DialogPortal,
  DialogRoot,
  DialogTitle,
  DialogTrigger
} from 'radix-vue'

defineProps<{
  filename: string
  image: string
}>()
</script>

<style scoped>
.dialog-trigger {
  border: none;
}
.dialog-trigger img {
  cursor: pointer;
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  transition: transform 0.3s ease;
}

.dialog-trigger img:hover {
  transform: scale(1.1);
}

.dialog-overlay {
  background-color: rgba(0, 0, 0, 0.6);
  position: fixed;
  inset: 0;
  animation: overlayShow 150ms cubic-bezier(0.16, 1, 0.3, 1);
}

.dialog-content {
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

.dialog-header {
  display: flex;
  align-items: center;
  justify-content: center;
  position: relative;
  margin-bottom: 16px;
}

.dialog-title {
  font-size: 24px;
  font-weight: bold;
  color: #083863;
}

.close-button {
  all: unset;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  position: absolute;
  left: 95%;
  width: 32px;
  height: 32px;
  border-radius: 50%;
  background-color: transparent;
  transition: background-color 0.3s ease, transform 0.2s ease;
}

.close-button:hover {
  background-color: rgba(8, 56, 99, 0.1);
  transform: scale(1.1);
}

.close-button-icon {
  font-size: 16px;
  transition: color 0.3s ease;
}

.dialog-image {
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: 100%;
  max-height: 100%;
  overflow: hidden;
}

.dialog-image img {
  max-width: 100%;
  height: auto;
}

@keyframes overlayShow {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

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
