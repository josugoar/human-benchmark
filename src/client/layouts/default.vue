<template>
  <v-app>
    <TheHeader :drawer="drawer" />
    <TheDrawer v-model="drawer" />
    <nuxt />
    <TheFooter />
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import TheHeader from '@/components/app/TheHeader.vue'
import TheDrawer from '@/components/app/TheDrawer.vue'
import TheFooter from '@/components/app/TheFooter.vue'
export default Vue.extend({
  components: {
    TheHeader,
    TheDrawer,
    TheFooter
  },
  data() {
    return {
      drawer: false
    }
  },
  mounted() {
    this.$store.commit('hydrate')
  }
})
</script>
