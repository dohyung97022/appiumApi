<template>
  <div class="hello">
    <h1>There is no better place than <a href="/">127.0.0.1</a></h1>
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';

export default defineComponent({
  name: 'HelloWorld',
  props: {
    msg: String,
  },
});
</script>

<style scoped>
</style>
