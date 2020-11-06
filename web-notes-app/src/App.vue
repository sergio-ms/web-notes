<template>
  <div id="app">
    <div class="container">
      <Header />
      <router-view />
    </div>
  </div>
</template>
<script>
import Header from "@/components/Header";
export default {
  name: "app",
  components: {
    Header
  }
};
</script>

<style lang="scss">
@import "~bulma/css/bulma.css";
</style>
