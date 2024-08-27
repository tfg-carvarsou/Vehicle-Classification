<template>
  <div v-bind="api.getRootProps()">
    <div v-bind="api.getDropzoneProps()">
      <input v-bind="api.getHiddenInputProps()" />
      Drag and drop an image here
    </div>

    <button v-bind="api.getTriggerProps()">Browse image</button>

    <ul v-bind="api.getItemGroupProps()">
      <li v-for="file in api.acceptedFiles" :key="file.name" v-bind="api.getItemProps({ file })">
        <div v-bind="api.getItemNameProps({ file })">{{ file.name }}</div>
        <button v-bind="api.getItemDeleteTriggerProps({ file })">Delete</button>
      </li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import * as fileUpload from '@zag-js/file-upload'
import { normalizeProps, useMachine } from '@zag-js/vue'
import { computed } from 'vue'

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
    onFileChange(details) {
      const reader = new FileReader()
      reader.onload = (event) => {
        event.target ? event.target.result : null
      }
      reader.readAsDataURL(details.acceptedFiles[0])
    }
  })
)

const api = computed(() => fileUpload.connect(state.value, send, normalizeProps))
</script>

<style scoped>
[data-part='root'] {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 16px;
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
  margin-top: 16px;
  padding: 8px 16px;
  font-size: 14px;
  color: #ffffff;
  background-color: #02af98;
  border: none;
  border-radius: 4px;
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
  justify-content: space-between;
  align-items: center;
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
  font-size: 12px;
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
</style>
