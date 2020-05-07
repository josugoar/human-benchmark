<template>
  <v-container>
    <h1 v-if="error.statusCode === 404" v-text="pageNotFound" />
    <h1 v-else v-text="otherError" />
    <nuxt-link to="/">
      Home
    </nuxt-link>
  </v-container>
</template>

<script>
import Vue from 'vue'
export default Vue.extend({
  layout: 'empty',
  props: {
    error: {
      type: Object,
      default: null
    }
  },
  data() {
    return {
      pageNotFound: '404 Not Found',
      otherError: 'An error occurred'
    }
  },
  head() {
    const title =
      this.error.statusCode === 404 ? this.pageNotFound : this.otherError
    return {
      title
    }
  }
})
</script>

<style scoped>
h1 {
  font-size: 20px;
}
</style>
