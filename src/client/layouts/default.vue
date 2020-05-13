<template>
  <v-app :style="`background-color: ${$vuetify.theme.currentTheme.primary}`">
    <template v-if="hydrated">
      <nuxt />
      <TheDrawer />
      <TheHeader />
      <TheFooter />
    </template>
    <Loader v-else />
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapState } from 'vuex'
import Loader from '@/components/Loader.vue'
import TheDrawer from '@/components/app/TheDrawer.vue'
import TheHeader from '@/components/app/TheHeader.vue'
import TheFooter from '@/components/app/TheFooter.vue'
export default Vue.extend({
  components: {
    Loader,
    TheDrawer,
    TheHeader,
    TheFooter
  },
  computed: {
    ...mapState(['hydrated'])
  },
  mounted() {
    this.$store.commit('hydrate')
  }
})
</script>
