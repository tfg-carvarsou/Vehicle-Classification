<template>
  <div class="upload-image-form">
    <h2 class="uff-title">Upload your image</h2>
    <div v-bind="api.getRootProps()">
      <div v-bind="api.getDropzoneProps()">
        <input v-bind="api.getHiddenInputProps()" />
        Drag and drop an image here, or
        <div class="browse">
          <FontAwesomeIcon :icon="fas.faSearch" />
          <i> Browse</i>
        </div>
      </div>

      <ul v-bind="api.getItemGroupProps()">
        <li v-for="file in api.acceptedFiles" :key="file.name" v-bind="api.getItemProps({ file })">
          <div v-bind="api.getItemNameProps({ file })">
            {{ file.name }}
          </div>
          <UploadImageAlertDialog
            v-if="showImageAlertDialog"
            :modelType="selectedModelType"
            :modelSeries="selectedModelSeries"
            :image="imageToUpload"
            :imageName="file.name"
          />
          <button class="button red" v-bind="api.getItemDeleteTriggerProps({ file })">
            <FontAwesomeIcon :icon="fas.faDeleteLeft" /> Delete
          </button>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup lang="ts">
import * as fileUpload from '@zag-js/file-upload'
import { normalizeProps, useMachine } from '@zag-js/vue'
import { ref, computed, watch } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome'
import { fas } from '@fortawesome/free-solid-svg-icons'
import UploadImageAlertDialog from '@/components/molecules/UploadImageAlertDialog.vue'

const imageLoaded = ref<string | ArrayBuffer | null>(null)
const imageToUpload = ref<string | null>(null)
const showImageAlertDialog = ref(false)

const [state, send] = useMachine(
  fileUpload.machine({
    id: '1',
    name: 'vehicle-upload',
    accept: {
      'image/png': ['.png'],
      'image/jpg': ['.jpg', '.jpeg'],
      'image/webp': ['.webp']
    },
    maxFiles: 1,
    maxFileSize: 1024 * 1024 * 10,
    onFileAccept(details) {
      const reader = new FileReader()
      reader.onload = (event) => {
        imageLoaded.value = event.target ? event.target.result : null
      }
      reader.readAsDataURL(details.files[0])
    }
  })
)

const api = computed(() => fileUpload.connect(state.value, send, normalizeProps))

watch(imageLoaded, (newValue) => {
  if (typeof newValue === 'string') {
    imageToUpload.value = newValue
    showImageAlertDialog.value = true
  } else {
    console.error('Loaded image is not a string')
  }
})

defineProps<{
  selectedModelType: string
  selectedModelSeries: string
}>()
</script>

<style scoped>
.upload-image-form {
  display: flex;
  width: 400%;
  flex-direction: column;
  align-items: left;
  margin-top: -30px;
  text-align: center;
}

.uff-title {
  display: flex;
  font-size: 30px;
  font-weight: bold;
  margin-bottom: 17px;
  color: #083863;
}

.browse i {
  font-weight: bold;
}

[data-part='root'] {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  width: 180%;
  border: 2px dashed #cccccc;
  border-radius: 8px;
  background-color: #f9f9f9;
  cursor: pointer;
  transition:
    background-color 0.3s ease,
    border-color 0.3s ease;
}

[data-part='root']:hover {
  background-color: #f0f0f0;
  border-color: #bbbbbb;
}

[data-part='dropzone'] {
  width: 100%;
  padding: 40px;
  text-align: center;
  color: #666666;
  font-size: 16px;
  transition: color 0.3s ease;
}

[data-part='dropzone']:hover {
  color: #333333;
}

button {
  all: unset;
  font-size: 14px;
  font-weight: 500;
  line-height: 1;
  align-items: center;
  justify-content: center;
  color: #ffffff;
  border: none;
  border-radius: 4px;
  height: 32px;
  cursor: pointer;
  transition:
    background-color 0.3s ease,
    transform 0.2s ease;
}

button:hover {
  background-color: #027666;
  transform: translateY(-2px);
}

ul {
  margin-top: 20px;
  width: 100%;
  list-style-type: none;
  padding: 0;
}

li {
  display: flex;
  justify-content: end;
  align-items: center;
  gap: 10px;
  padding: 8px 12px;
  margin-bottom: 8px;
  border-radius: 4px;
  background-color: #ffffff;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.3s ease;
}

li:hover {
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.15);
}

li > div {
  font-size: 14px;
  color: #333333;
}

li button {
  padding: 4px 8px;
  font-size: 14px;
  color: #ffffff;
  background-color: #ef4444;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

li button:hover {
  background-color: #c0392b;
}

@media (max-width: 1024px) {
  .upload-image-form {
    margin-left: 0;
  }

  .uff-title {
    margin-left: 0;
  }

  [data-part='root'] {
    width: 180%;
  }
}
</style>
