<template>
  <div v-if="visible" class="modal-overlay">
    <div class="modal">
      <h3>{{ title }}</h3>
      <slot></slot>
      <button @click="$emit('close')">Close</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "CustomModal",
  props: {
    visible: Boolean,
    title: String,
  },
};
</script>

<style scoped>
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(0, 0, 0, 0.5);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 1000; /* Ensure it is on top of other elements */
}

.modal {
  background: white;
  padding: 20px;
  border-radius: 5px;
  width: 300px;
  z-index: 1001; /* Ensure it is on top of the overlay */
}

button {
  margin-top: 10px;
}
</style>

