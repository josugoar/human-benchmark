<template>
  <v-container style="text-align: center;">
    <h1 v-if="error.statusCode === 404" v-text="log.notFound" />
    <h1 v-else v-text="log.other" />
    <nuxt-link to="/" exact v-text="text" />
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
      log: {
        notFound: '404 Not Found',
        other: 'An error occurred'
      },
      text: 'Return'
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
