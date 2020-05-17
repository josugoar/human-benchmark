<template>
  <v-app :style="`background-color: ${$vuetify.theme.currentTheme.primary}`">
    <Loader :loading="!hydrated" />
    <template v-if="hydrated">
      <nuxt />
      <ScrollTop />
      <TheDrawer />
      <TheHeader />
      <TheFooter />
    </template>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapState } from 'vuex'
import Loader from '@/components/Loader.vue'
import ScrollTop from '@/components/ScrollTop.vue'
import TheDrawer from '@/components/app/TheDrawer.vue'
import TheHeader from '@/components/app/TheHeader.vue'
import TheFooter from '@/components/app/TheFooter.vue'
export default Vue.extend({
  components: { Loader, ScrollTop, TheDrawer, TheHeader, TheFooter },
  computed: { ...mapState(['hydrated']) },
  mounted() {
    setTimeout(() => {
      this.$store.commit('hydrate')
    }, 100)
  }
})
</script>
