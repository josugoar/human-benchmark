<template>
  <v-container style="text-align: center;">
    <h1 v-if="error.statusCode === 404" v-text="notFound" />
    <h1 v-else v-text="otherError" />
    <nuxt-link to="/" exact>Return</nuxt-link>
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
      notFound: '404 Not Found',
      otherError: 'An error occurred'
    }
  },
  head() {
    return {
      title: this.error.statusCode === 404 ? this.pageNotFound : this.otherError
    }
  }
})
</script>

<style scoped>
h1 {
  font-size: 20px;
}
</style>
