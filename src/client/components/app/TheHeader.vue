<template>
  <v-app-bar color="primary" app dense elevate-on-scroll>
    <nuxt-link to="/" exact>
      <v-toolbar-title class="font-weight-black">
        <v-avatar size="30" style="vertical-align: bottom;" tile>
          <v-img :src="icon" alt="Icon" contain />
        </v-avatar>
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
      aria-label="Toggle"
      color="secondary"
      @click.stop="emitToggle"
    />
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapState } from 'vuex'
import { EventBus } from '@/components/EventBus'
export default Vue.extend({
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
    ...mapState(['env', 'hydrated']),
    icon() {
      return require(`@/assets/icons/main/${
        this.$vuetify.theme.dark ? 'dark.png' : 'light.png'
      }`)
    }
  },
  methods: {
    emitToggle() {
      EventBus.$emit('toggle')
    }
  }
})
</script>
