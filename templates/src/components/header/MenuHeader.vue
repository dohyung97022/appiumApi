<template>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">

    <!--  메인 아이콘  -->
    <router-link class="navbar-brand" to="/">{{headerValues.title}}</router-link>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>

    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <!-- header 루프 -->
      <ul class="navbar-nav" v-for="menu in headerValues.menus" v-bind:key="menu.title">

        <!-- 1 depth 일 경우 -->
        <li class="nav-item" v-if="menu.subMenu.length === 0">
          <router-link class="nav-link active" aria-current="page" :to="menu.path">{{menu.title}}</router-link>
        </li>

        <!-- 2 depth 일 경우 -->
        <li class="nav-item dropdown" v-else>

          <router-link class="nav-link dropdown-toggle" aria-current="page" :to="menu.path"  id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            {{menu.title}}
          </router-link>

          <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            <router-link class="dropdown-item" :to="subMenu.path" v-for="subMenu in menu.subMenu" v-bind:key="subMenu.title">{{subMenu.title}}</router-link>
          </ul>
        </li>
      </ul>
    </div>
  </div>

</nav>
  <!-- 라우터 내용이 나오는 곳 -->
  <router-view></router-view>
</template>

<script lang="ts">
import {defineComponent, ref} from 'vue';
import Header from "@/components/header/model/Header";
import {header} from "@/router/routes";

export default defineComponent({
  name: 'MenuHeader',
  props: { },
  setup() {
    const headerValues = ref<Header>(header)
    return { headerValues }
  }
});
</script>

<style scoped>

</style>