<template>
  <div class="container-xxl">
    <ViewTitle title="핸드폰 행동절차" sub-title="핸드폰의 행동절차를 구성합니다."/>
    <div class="row row-cols-2 justify-content-between">
      <!--     핸드폰 화면     -->
      <div class="col-4 col-auto">
        <MonitorPhoneScreen/>
      </div>
      <!--     행동 리스트     -->
      <div class="col-8">
        <AutomationPhoneActionList/>
      </div>
    </div>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import ViewTitle from "@/components/viewTitle/ViewTitle.vue";
import MonitorPhoneScreen from "@/components/monitor/phone/MonitorPhoneScreen.vue";
import AutomationPhoneActionList from "@/components/automation/phoneAction/AutomationPhoneActionList.vue";

export default defineComponent({
  name: "AutomationPhoneActionView",

  components: {
    AutomationPhoneActionList,
    MonitorPhoneScreen,
    ViewTitle
  }
})
</script>

<style scoped>
</style>