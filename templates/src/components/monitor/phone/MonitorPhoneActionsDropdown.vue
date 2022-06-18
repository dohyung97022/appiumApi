<template>
  <select class="form-select card-mg-b" v-for="action in actions" v-bind:key="action.action_seq">
    <option :value="action.type">{{action.type}}</option>
  </select>
</template>

<script lang="ts">
import { defineComponent } from "vue";
import Action from "@/components/monitor/phone/model/Action";
import axios from "axios";

export default defineComponent ({
  name: "MonitorPhoneActionsDropdown",

    data() {
      return {
        actions: [] as Array<Action>
      }
    },

  async created() {
    this.get_actions();
    return;
  },

  methods: {

    // 모든 actions 가져오기
    get_actions() {
      axios.get<Action[]>('/api/automation/actions')
          .then(res => {
            this.actions = res.data
          })
          .catch(res => {
            console.log(res)
          })
    }
  }
})
</script>

<style scoped>

</style>