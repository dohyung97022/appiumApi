<template>
  <template v-for="phone_screen in phone_screens" v-bind:key="phone_screen.udid">

    <div class="card mb-3" style="width: 400px;">
      <div class="row g-0">
        <img class="col-md-4 rounded-start" :src="phone_screen.img" style="width: 150px;"/>
        <div class="col-md-7">
          <div class="card-body">
            <h6 class="card-title">{{phone_screen.udid}}</h6>
            <div class="card-group card-mg-b">
              <MonitorPhoneActionsDropdown class="card-mg-b"/>
            <button class="btn btn-primary" type="button">action</button>
            </div>
            <router-link class="btn btn-secondary" :to="'/monitor/phone?udid=' + phone_screen.udid">control</router-link>
          </div>
        </div>
      </div>
    </div>

  </template>
</template>

<script lang="ts">
import { socket, connect } from "@/components/socket/model/Socket";
import { defineComponent } from "vue";
import PhoneScreen from "@/components/monitor/phone/model/PhoneScreen";
import MonitorPhoneActionsDropdown from "@/components/monitor/phone/MonitorPhoneActionsDropdown.vue";

export default defineComponent ({
  name: "MonitorPhoneScreens",

  components: {
    MonitorPhoneActionsDropdown
  },

  props: {
  },

  data() {
    return {
      phone_screens: [] as Array<PhoneScreen>
    }
  },

  async created() {
    connect()
    this.phones_connect()
    this.phone_screens_connect()
  },

  methods: {

    // 핸드폰 리스트 room join
    phones_connect() {
      socket.emit('join_room', 'phone_screens');
    },

    // 핸드폰 리스트 화면 소켓 수신
    phone_screens_connect() {
      socket.on('phone_screens_connect', (data: Array<PhoneScreen>) => {
        this.phone_screens = data
      })
    }
  }
})
</script>

<style scoped>
.card-mg-b{
  margin-bottom: 0.5rem;
}
</style>