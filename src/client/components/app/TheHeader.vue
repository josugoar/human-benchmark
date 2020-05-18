<template>
  <v-app-bar
    v-scroll="onScroll"
    :color="offsetTop === 0 ? 'transparent' : ''"
    scroll-threshold="1"
    app
    short
    elevate-on-scroll
  >
    <v-app-bar-nav-icon aria-label="Drawer" @click.stop="emitToggle" />
    <v-toolbar-title class="font-weight-black">
      <nuxt-link to="/" exact>
        <v-avatar size="30" style="vertical-align: bottom;">
          <v-img
            :src="
              require(`@/assets/icons/main/${
                $vuetify.theme.dark ? 'dark.png' : 'light.png'
              }`)
            "
            alt="Icon"
          />
        </v-avatar>
        Human Benchmark
      </nuxt-link>
    </v-toolbar-title>
    <v-spacer />
    <component
      :is="$vuetify.breakpoint.xs ? 'template' : 'v-toolbar-items'"
      v-if="hydrated"
      :slot="$vuetify.breakpoint.xs ? 'extension' : 'default'"
    >
      <v-tabs
        :height="$vuetify.breakpoint.xs ? 48 : 56"
        background-color="transparent"
        class="d-flex justify-center"
        color="accent"
        optional
      >
        <v-tab
          v-for="tab in tabs"
          :key="tab.label"
          :to="tab.url"
          nuxt
          v-text="tab.label"
        />
      </v-tabs>
    </component>
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapState } from 'vuex'
import OffsetThreshold from '@/components/utils/OffsetThreshold'
import { EventBus } from '@/components/utils/EventBus'
export default Vue.extend({
  mixins: [OffsetThreshold],
  data: () => ({
    tabs: [
      {
        label: 'Ranking',
        url: '/ranking'
      },
      {
        label: 'About',
        url: '/about'
      }
    ]
  }),
  computed: {
    ...mapState(['hydrated'])
  },
  methods: {
    emitToggle: () => EventBus.$emit('toggle')
  }
})
</script>
