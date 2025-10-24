<template>
  <div class="tooltip-container">
    <button @mouseover="showTooltip = true" @mouseleave="showTooltip = false" @click="toggleTooltip">
      ?
    </button>
    <div v-if="showTooltip" class="tooltip-content">
      <p><span class="color-box red"></span> Red: No recent snapshot or snapshot is older than 30 days.</p>
      <p><span class="color-box orange"></span> Orange: Manually ignored, reason is avilable in the properties window.</p>
      <p><span class="color-box yellow"></span> Yellow: Snapshot is not from today but less than 30 days old.</p>
      <p><span class="color-box green"></span> Green: Snapshot is from today.</p>
      <!-- Add more legend items as needed -->
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showTooltip: false
    };
  },
  methods: {
    toggleTooltip() {
      this.showTooltip = !this.showTooltip;
    }
  }
};
</script>

<style scoped>
.tooltip-container {
  position: fixed;
  bottom: 10px;
  right: 10px;
  z-index: 1000;
}

.tooltip-container button {
  background-color: #007bff;
  color: white;
  border: none;
  border-radius: 50%;
  width: 40px;
  height: 40px;
  cursor: pointer;
  font-size: 18px;
}

.tooltip-content {
  position: absolute;
  bottom: 50px;
  right: 0;
  background-color: white;
  border: 1px solid #ccc;
  border-radius: 5px;
  padding: 10px;
  box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  width: 300px; /* Set the width of the tooltip */
  max-width: 90vw; /* Ensure it doesn't exceed the viewport width */
  box-sizing: border-box;
}

.color-box {
  display: inline-block;
  width: 10px;
  height: 10px;
  margin-right: 5px;
}

.color-box.red {
  background-color: #ffcccc;
}

.color-box.yellow {
  background-color: yellow;
}

.color-box.green {
  background-color: #ccffcc;
}

.color-box.orange {
  background-color: #ffa500;
}

</style>

