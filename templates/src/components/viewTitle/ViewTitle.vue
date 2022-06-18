<template>
  <div class="mb-5 mt-4">
    <nav aria-label="breadcrumb">
      <ol class="breadcrumb fw-lighter">
        <li class="breadcrumb-item"><a href="/">Home</a></li>
        <li class="breadcrumb-item" v-for="breadCrumb in this.$data.breadCrumbs" v-bind:key="breadCrumb.path">
          <a v-if="breadCrumb.isLink" :href="breadCrumb.path">{{ breadCrumb.title }}</a>
          <span v-else>{{ breadCrumb.title }}</span>
        </li>
      </ol>
    </nav>

    <h1>{{ this.title }}</h1>
    <h6 class="fw-light">{{ this.subTitle }}</h6>
  </div>
</template>

<script lang="ts">
import {defineComponent} from "vue";
import BreadCrumb from "@/components/viewTitle/model/breadCrumb";
import {pathExists} from "@/router/routes";

export default defineComponent({
  name: "ViewTitle",

  props: {
    title: String,
    subTitle: String
  },

  data() {
    return {
      breadCrumbs: [] as Array<BreadCrumb>
    }
  },

  created() {
    this.breadCrumbs = this.createBreadCrumbsFromUrlPath();
  },

  methods: {
    createBreadCrumbsFromUrlPath() {
      let breadCrumbs = []

      const titles = this.$route.path.split('/')
      titles.shift() // 첫 문자열 '' 제거

      // path 내에서 breadCrumb 추출
      for (let i = 0; i <= titles.length - 1; i++) {
        const paths = this.$route.path.split('/').slice(0, i + 2),
            path = paths.join('/');
        breadCrumbs.push(new BreadCrumb(titles[i], path, pathExists(path)))
      }

      return breadCrumbs
    }
  },
})
</script>

<style scoped>

</style>