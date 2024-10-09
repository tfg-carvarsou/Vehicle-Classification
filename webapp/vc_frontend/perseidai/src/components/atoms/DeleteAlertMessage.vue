<template>
  <div v-if="showAlert" class="alert-container">
    <div class="alert alert-delete" role="alert">
      {{ message }}
      <button @click="closeAlert" class="close-btn">
        <FontAwesomeIcon :icon="fas.faClose" />
      </button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import { ref, onMounted, onUnmounted } from 'vue'

const props = defineProps<{
  showAlert: boolean
  message: string
}>()

const showAlert = ref(props.showAlert)
const message = ref(props.message)
let timeout: ReturnType<typeof setTimeout> | null = null

const showDeleteAlert = (msg: string = 'Deleted successfully') => {
  message.value = msg
  showAlert.value = true
  if (timeout) {
    clearTimeout(timeout)
  }
  timeout = setTimeout(() => {
    showAlert.value = false
  }, 3000)
}

const closeAlert = () => {
  showAlert.value = false
  if (timeout) {
    clearTimeout(timeout)
  }
}

onMounted(() => {
  showDeleteAlert(props.message)
})

onUnmounted(() => {
  showAlert.value = false
  if (timeout) {
    clearTimeout(timeout)
  }
})
</script>

<style scoped>
.alert-container {
  position: fixed;
  top: 80px;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  z-index: 1000;
}

.alert {
  padding: 10px 20px;
  border-radius: 4px;
  display: flex;
  align-items: center;
  justify-content: space-between;
}

.alert-delete {
  background-color: #ef4444;
  border-color: #a83232;
  color: #ffffff;
}

.close-btn {
  background: none;
  border: none;
  color: inherit;
  font-size: 1.5rem;
  cursor: pointer;
  margin-left: 10px;
}
</style>
