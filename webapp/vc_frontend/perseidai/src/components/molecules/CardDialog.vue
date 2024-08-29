<template>
  <DialogRoot>
    <DialogTrigger>
      <img :src="image" class="dialog-trigger-image" alt="Open Image" />
    </DialogTrigger>
    <DialogPortal>
      <DialogOverlay class="dialog-overlay" />
      <DialogContent class="dialog-content">
        <DialogTitle class="dialog-title">Image Preview</DialogTitle>
        <div class="dialog-image">
          <img :src="image" alt="Image preview" />
        </div>
        <DialogClose class="close-button">Close</DialogClose>
      </DialogContent>
    </DialogPortal>
  </DialogRoot>
</template>

<script setup lang="ts">
import {
  DialogClose,
  DialogContent,
  DialogOverlay,
  DialogPortal,
  DialogRoot,
  DialogTitle,
  DialogTrigger
} from 'radix-vue';

defineProps<{
  image: string;
}>();
</script>

<style scoped>
.dialog-trigger-image {
  cursor: pointer;
  max-width: 100%;
  height: auto;
  border-radius: 8px;
  transition: transform 0.3s ease;
}

.dialog-trigger-image:hover {
  transform: scale(1.05);
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

.dialog-title {
  font-size: 24px;
  font-weight: bold;
  margin-bottom: 16px;
  color: #083863;
}

.dialog-image {
  display: flex;
  justify-content: center;
  align-items: center;
  max-width: 100%;
  max-height: 49vh;
  overflow: hidden;
}

.dialog-image img {
  max-width: 100%;
  height: auto;
}

.close-button {
  all: unset;
  cursor: pointer;
  padding: 4px 8px;
  font-size: 14px;
  border-radius: 4px;
  height: 32px;
  transition: background-color 0.3s ease, transform 0.2s ease;
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
