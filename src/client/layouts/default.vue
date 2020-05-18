<template>
  <v-app :style="`background-color: ${$vuetify.theme.currentTheme.secondary}`">
    <Loader :loading="!hydrated" />
    <template v-if="hydrated">
      <nuxt />
      <Scroller />
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
import Scroller from '@/components/Scroller.vue'
import TheDrawer from '@/components/app/TheDrawer.vue'
import TheHeader from '@/components/app/TheHeader.vue'
import TheFooter from '@/components/app/TheFooter.vue'
export default Vue.extend({
  components: { Loader, Scroller, TheDrawer, TheHeader, TheFooter },
  computed: { ...mapState(['hydrated']) },
  mounted() {
    setTimeout(() => this.$store.commit('hydrate'), 100)
  }
})
</script>
