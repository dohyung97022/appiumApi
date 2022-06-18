import { io } from "socket.io-client";
import {Socket} from "socket.io-client/build/esm/socket";

// global 소켓
export let socket: Socket

export function connect() {

  // 연결
  socket = io('ws://127.0.0.1:8082', {transports: ['websocket']})

  // 연결 확인
  socket.on("connect", () => {
    console.log("connected")
  })
}
