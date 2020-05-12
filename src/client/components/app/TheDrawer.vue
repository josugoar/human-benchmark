<template>
  <v-navigation-drawer v-model="drawer" app temporary>
    <v-list-item>
      <v-list-item-avatar>
        <v-img alt="Avatar" src="https://via.placeholder.com/150" />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title>Lorem Ipsum</v-list-item-title>
      </v-list-item-content>
    </v-list-item>
    <template #append>
      <v-row justify="center">
        <v-icon class="mr-3">mdi-theme-light-dark</v-icon>
        <v-switch v-model="$vuetify.theme.dark">Logout</v-switch>
      </v-row>
    </template>
  </v-navigation-drawer>
</template>

<script lang="ts">
import Vue from 'vue'
import { EventBus } from '@/components/EventBus'
export default Vue.extend({
  asyncData() {},
  data() {
    return {
      drawer: false
    }
  },
  mounted() {
    EventBus.$on('toggle', () => {
      this.drawer = !this.drawer
    })
  }
})
</script>
