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
          v-text="rand"
        />
        {{ env.title }}
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
        optional
      >
        <v-tab
          v-for="tab in tabs"
          :key="tab.name"
          :to="tab.url"
          nuxt
          v-text="tab.name"
        />
      </v-tabs>
    </component>
    <v-app-bar-nav-icon
      aria-label="Drawer"
      color="secondary"
      @click.stop="drawer = !drawer"
    />
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapGetters, mapState } from 'vuex'
export default Vue.extend({
  props: {
    drawer: {
      type: Boolean,
      default: false
    }
  },
  data() {
    return {
      tabs: [
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
    ...mapGetters('icons', ['rand']),
    ...mapState(['env', 'hydrated'])
  }
})
</script>

<style lang="scss" scoped>
.empty-link {
  color: inherit;
  text-decoration: none;
}
</style>
