<template>
  <img v-if="phone_screen != null" :src="phone_screen.img" v-on:click="phone_touch($event)" class="img-thumbnail">
</template>

<script lang="ts">
import { socket, connect } from "@/components/socket/model/Socket";
import { defineComponent } from "vue";
import PhoneScreen from "@/components/monitor/phone/model/PhoneScreen";

export default defineComponent ({
  name: "MonitorPhoneScreen",

  data() {
    return {
      udid: this.$route.query.udid as string,
      phone_screen: null as PhoneScreen|null
    }
  },

  async created() {
    connect()
    this.phone_connect()
    this.phone_screen_connect()
  },

  methods: {

    // 핸드폰 udid 의 room join
    phone_connect() {
      socket.emit('join_room', this.udid);
    },

    // 핸드폰 화면 소켓 수신
    phone_screen_connect() {
      socket.on('phone_screen_connect', (data: PhoneScreen) => {
        this.phone_screen = data
      })
    },

    // 터치 소켓 전송
    phone_touch(event: PointerEvent) {
      // 터치된 곳이 이미지일 경우
      if (event.target instanceof HTMLImageElement) {
        // 데이터 전송
        socket.emit('phone_touch', {
          udid: this.udid,
          touch_x: event.offsetX,
          touch_y: event.offsetY,
          touch_w: event.target.naturalWidth,
          touch_h: event.target.naturalHeight
        });
      }
    }
  }
})
</script>

<style scoped>

</style>