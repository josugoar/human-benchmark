<template>
  <v-app>
    <nuxt />
    <TheDrawer />
    <TheHeader />
    <TheFooter />
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import TheDrawer from '@/components/app/TheDrawer.vue'
import TheHeader from '@/components/app/TheHeader.vue'
import TheFooter from '@/components/app/TheFooter.vue'
export default Vue.extend({
  components: {
    TheDrawer,
    TheHeader,
    TheFooter
  },
  mounted() {
    this.$store.commit('hydrate')
  }
})
</script>
