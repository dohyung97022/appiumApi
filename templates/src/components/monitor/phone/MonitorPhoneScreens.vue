<template>
  <template v-for="phone_screen in phone_screens" v-bind:key="phone_screen[0]">

    <div class="card mb-3" style="width: 400px;">
      <div class="row g-0">
        <img class="col-md-4 rounded-start" :src="phone_screen[1]" style="width: 150px;"/>
        <div class="col-md-7">
          <div class="card-body">
            <h6 class="card-title">{{ phone_screen[0] }}</h6>
            <div class="card-group card-mg-b">
              <router-link class="btn btn-primary" :to="'/automation/phoneAction?udid=' + phone_screen[0]">action</router-link>
            </div>
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

export default defineComponent ({
  name: "MonitorPhoneScreens",

  components: {
  },

  props: {
  },

  data() {
    return {
      phone_screens: new Map<string, string>() as Map<string, string>
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
      socket.on('phone_screens_connect', (data: PhoneScreen) => {
        this.phone_screens.set(data.udid, data.img)
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