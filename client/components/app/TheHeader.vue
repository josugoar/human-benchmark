<template>
  <v-app-bar color="primary" app dense elevate-on-scroll>
    <nuxt-link class="empty-link" to="/" exact>
      <v-toolbar-title
        :style="{ color: $vuetify.theme.currentTheme.secondary }"
        class="font-weight-black"
      >
        <v-icon
          color="secondary"
          style="vertical-align: inherit;"
          left
          v-text="icon"
        />
        Human Benchmark
      </v-toolbar-title>
    </nuxt-link>
    <v-spacer />
    <component
      :is="$vuetify.breakpoint.xs ? 'template' : 'v-toolbar-items'"
      v-if="$store.state.hydrated"
      :slot="$vuetify.breakpoint.xs ? 'extension' : 'default'"
    >
      <v-tabs
        background-color="transparent"
        class="d-flex justify-center"
        color="secondary"
        optional
      >
        <v-tab
          v-for="page in $store.state.sources.pages"
          :key="page.name"
          :to="page.url"
          nuxt
          v-text="page.name"
        />
      </v-tabs>
    </component>
    <v-app-bar-nav-icon color="secondary" @click.stop="" />
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      icons: [
        'mdi-chess-bishop',
        'mdi-chess-king',
        'mdi-chess-knight',
        'mdi-chess-pawn',
        'mdi-chess-queen',
        'mdi-chess-rook'
      ]
    }
  },
  computed: {
    icon(): string {
      return this.icons[Math.floor(Math.random() * this.icons.length)]
    }
  },
  mounted() {
    this.$store.commit('hydrate')
  }
})
</script>

<style lang="scss" scoped>
.empty-link {
  color: inherit;
  text-decoration: none;
}
</style>
