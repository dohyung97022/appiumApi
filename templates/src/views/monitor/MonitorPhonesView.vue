<template>
  <MonitorPhoneScreens/>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MonitorPhoneScreens from '@/components/monitor/phone/MonitorPhoneScreens.vue';

export default defineComponent({
  name: "MonitorPhonesView",
    components: {
    MonitorPhoneScreens
  }
})
</script>

<style scoped>

</style>