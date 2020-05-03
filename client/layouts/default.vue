<template>
  <v-app>
    <TheHeader />
    <nuxt />
    <TheFooter />
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import TheHeader from '@/components/app/TheHeader.vue'
import TheFooter from '@/components/app/TheFooter.vue'
export default Vue.extend({
  components: {
    TheHeader,
    TheFooter
  }
})
</script>
