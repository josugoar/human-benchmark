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
    <component
      :is="$vuetify.breakpoint.xs ? 'template' : 'v-toolbar-items'"
      v-if="hydrated"
      :slot="$vuetify.breakpoint.xs ? 'extension' : 'default'"
    >
      <v-tabs
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
    </component>
    <v-app-bar-nav-icon color="secondary" @click.stop="drawer = !drawer" />
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue'
import TheDrawer from '@/components/app/TheDrawer.vue'
export default Vue.extend({
  components: {
    TheDrawer
  },
  data() {
    return {
      drawer: true,
      hydrated: false,
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
      return this.icons[Math.floor(Math.random() * this.icons.length)]
    }
  },
  mounted() {
    this.hydrated = true
  }
})
</script>

<style lang="scss" scoped>
.empty-link {
  color: inherit;
  text-decoration: none;
}
</style>
