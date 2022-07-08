<template>
  <button class="btn btn-secondary" v-on:click="saveAllMonitorPhones">save all phones</button>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import axios from "axios";

export default defineComponent ({
  name: "MonitorPhoneSaveButton",

  data() {
    return {
    }
  },

  methods: {
    saveAllMonitorPhones() {
      axios.post('http://127.0.0.1:8082/api/automation/phones')
          .then(res => {console.log(res)})
          .catch(err => {console.log(err)})
    }
  }
})
</script>

<style scoped>
</style>