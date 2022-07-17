<template>
  <div class="container-xxl">
    <ViewTitle title="요원 작업 요청" sub-title="수동 작업이 필요한 경우 요원에게 작업을 요청합니다."/>
    <AutomationAgentJobRequestScreenForm/>
  </div>
</template>

<script>
import ViewTitle from "@/components/viewTitle/ViewTitle.vue";
import AutomationAgentJobRequestScreenForm from "@/components/automation/agentJob/AutomationAgentJobRequestScreenForm.vue";
export default {
  name: "AutomationAgentJobView.vue",
  components: {
    AutomationAgentJobRequestScreenForm,
    ViewTitle
  }
}
</script>

<style scoped>

</style>