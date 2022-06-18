<template>
  <div class="container-xxl">
    <ViewTitle title="자동화 행동절차" sub-title="행동절차와 매크로를 구성합니다."/>
    <AutomationActionTree/>
  </div>
</template>

<script lang="ts">
import {defineComponent} from 'vue';
import AutomationActionTree from '@/components/automation/action/AutomationActionTree.vue';
import ViewTitle from "@/components/viewTitle/ViewTitle.vue";

export default defineComponent({
  name: "AutomationActionsView",
  components: {
    AutomationActionTree, ViewTitle
  }
})
</script>

<style scoped>

</style>