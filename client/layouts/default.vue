<template>
  <v-app>
    <TheNavbar />
    <nuxt />
    <TheFooter />
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import TheNavbar from '@/components/TheNavbar.vue'
import TheFooter from '@/components/TheFooter.vue'
export default Vue.extend({
  components: {
    TheNavbar,
    TheFooter
  }
})
</script>
