<template>
  <MonitorPhoneScreen :udid="udid"/>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import MonitorPhoneScreen from '@/components/monitor/phone/MonitorPhoneScreen.vue';

export default defineComponent({
  name: "MonitorPhoneView",
    components: {
    MonitorPhoneScreen
  },
  data() {
    return {
      udid: this.$route.query.udid as string
    }
  }
})
</script>

<style scoped>

</style>