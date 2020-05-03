<template>
  <v-app-bar color="primary" app dense elevate-on-scroll>
    <nuxt-link class="empty-link" to="/" exact>
      <v-toolbar-title
        class="font-weight-black"
        style="color: var(--v-secondary-base);"
      >
        <v-icon
          color="secondary"
          style="vertical-align: inherit"
          left
          v-text="icon"
        />
        Human Benchmark
      </v-toolbar-title>
    </nuxt-link>
    <v-spacer />
    <wrapper :show="!$vuetify.breakpoint.xs">
      <v-toolbar-items>
        <v-tabs
          :slot="$vuetify.breakpoint.xs ? 'extension' : ''"
          background-color="transparent"
          class="d-flex justify-center"
          color="secondary"
          height="100%"
          optional
        >
          <v-tab
            v-for="page in pages"
            :key="page.name"
            :to="page.url"
            nuxt
            v-text="page.name"
          />
        </v-tabs>
      </v-toolbar-items>
    </wrapper>
    <v-app-bar-nav-icon
      style="color: var(--v-secondary-base);"
      @click.stop="drawer = !drawer"
    />
    <!-- <TheDrawer v-model="drawer" /> -->
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      drawer: false,
      icons: [
        'mdi-chess-bishop',
        'mdi-chess-king',
        'mdi-chess-knight',
        'mdi-chess-pawn',
        'mdi-chess-queen',
        'mdi-chess-rook'
      ],
      pages: [
        {
          name: 'Home',
          url: '/'
        },
        {
          name: 'About',
          url: '/about'
        }
      ]
    }
  },
  computed: {
    icon(): string {
      const idx = Math.floor(Math.random() * this.icons.length)
      return this.icons[idx]
    }
  }
})
</script>

<style lang="scss" scoped>
.empty-link {
  color: inherit;
  text-decoration: none;
}
</style>
