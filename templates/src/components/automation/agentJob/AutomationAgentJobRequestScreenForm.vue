<template>
  <div class="input-group w-25">
    <!--  핸드폰 화면  -->
    <img v-if="phone_screen != null" :src="phone_screen.img" v-on:click="phone_touch($event)" class="img-thumbnail">
    <!--  이메일 입력  -->
    <input placeholder="요원 이메일" type="text" class="form-control" v-model="assignJobToAgentParameters.agent_email"/>
    <!--  작업 요청  -->
    <button type="button" class="btn btn-outline-secondary" v-on:click="assign_job_to_agent">작업 요청</button>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue";
import axios from "axios";
import {socket, connect} from "@/components/socket/model/Socket";
import PhoneScreen from "@/components/automation/agentJob/model/PhoneScreen";

export default defineComponent({
  name: "AutomationAgentJobRequestScreenForm",

  data() {
    return {
      udid: '',
      phone_screen: null as PhoneScreen | null,
      assignJobToAgentParameters: {
        job: 'BING_CAPTCHA',
        agent_email: ''
      }
    }
  },

  methods: {
    assign_job_to_agent() {
      // job 요청
      axios.get('http://127.0.0.1:8082/api/automation/agentJob/udid', {params: this.assignJobToAgentParameters})
          .then(res => {
            if (res.data.toString() == {}.toString()) {
              alert("할당 가능한 작업이 없습니다.")
            }
            this.udid = res.data
          })
          .catch(error => (console.log(error)))

      // room 연결
      connect()
      this.phone_connect()
      this.phone_screen_connect()
    },


    // agent 의 room join
    phone_connect() {
      socket.emit('join_room', this.assignJobToAgentParameters.agent_email);
    },

    // 핸드폰 화면 소켓 수신
    phone_screen_connect() {
      socket.on('phone_screen_connect', (data: PhoneScreen) => {
        this.phone_screen = data
        this.udid = data.udid
      })
    },

    // 터치 소켓 전송
    phone_touch(event: PointerEvent) {
      // 이미지가 없을 경우
      if (this.phone_screen?.img == '') return
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