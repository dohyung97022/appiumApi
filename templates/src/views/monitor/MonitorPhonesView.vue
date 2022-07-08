<template>
  <MonitorPhoneScreens/>
  <MonitorPhoneSaveButton/>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MonitorPhoneScreens from '@/components/monitor/phone/MonitorPhoneScreens.vue';
import MonitorPhoneSaveButton from "@/components/monitor/phone/MonitorPhoneSaveButton.vue";

export default defineComponent({
  name: "MonitorPhonesView",
  components: {
    MonitorPhoneSaveButton,
    MonitorPhoneScreens
  }
})
</script>

<style scoped>

</style>