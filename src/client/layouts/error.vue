<template>
  <v-container style="text-align: center;">
    <h1 v-if="error.statusCode === 404" v-text="notFound" />
    <h1 v-else v-text="otherError" />
    <nuxt-link to="/" exact>Return</nuxt-link>
  </v-container>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  layout: 'empty',
  props: {
    error: {
      type: Object,
      default: null
    }
  },
  data: () => ({
    notFound: '404 Not Found',
    otherError: 'An error occurred'
  }),
  head() {
    return {
      title: this.error.statusCode === 404 ? this.notFound : this.otherError
    }
  }
})
</script>

<style scoped>
a {
  color: blue;
  text-decoration: underline;
}
</style>
