<template>
  <!-- ADD CROSS BUTTON -->
  <!-- ADD ELO AND MOVE SETTING -->
  <v-navigation-drawer v-model="drawer" color="primary" app temporary>
    <TheSystemBar />
    <v-list nav>
      <v-list-item>
        <v-list-item-avatar left>
          <v-img alt="Avatar" src="https://via.placeholder.com/150" />
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title class="title">Lorem Ipsum</v-list-item-title>
          <v-list-item-subtitle>Lorem ipsum</v-list-item-subtitle>
        </v-list-item-content>
        <v-list-item-action>
          <v-btn aria-label="Settings" icon>
            <v-icon>mdi-cog</v-icon>
          </v-btn>
        </v-list-item-action>
      </v-list-item>
      <v-divider inset />
      <v-subheader>Lorem ipsum</v-subheader>
      <v-list-item-group>
        <v-list-item
          v-for="item in items"
          :key="item.name"
          :to="item.url"
          exact
          nuxt
        >
          <v-list-item-icon>
            <v-icon v-text="item.icon" />
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.name" />
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
    <template #append>
      <v-row justify="center">
        <v-switch
          v-model="$vuetify.theme.dark"
          color="secondary"
          prepend-icon="mdi-theme-light-dark"
        />
      </v-row>
    </template>
  </v-navigation-drawer>
</template>

<script lang="ts">
import Vue from 'vue'
import { EventBus } from '@/components/utils/EventBus'
import TheSystemBar from '@/components/app/TheSystemBar.vue'
export default Vue.extend({
  components: { TheSystemBar },
  asyncData: () => ({}),
  data: () => ({
    items: [
      { icon: 'mdi-view-dashboard', name: 'Dashboard', url: '#Drawer-1' },
      { icon: 'mdi-record', name: 'Lorem ipsum', url: '#Drawer-2' },
      { icon: 'mdi-record', name: 'Lorem ipsum', url: '#Drawer-3' }
    ],
    drawer: false
  }),
  mounted() {
    EventBus.$on('toggle', () => {
      this.drawer = !this.drawer
    })
  }
})
</script>
