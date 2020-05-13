<template>
  <v-navigation-drawer v-model="drawer" color="primary" app temporary>
    <v-list>
      <v-list-item class="my-3">
        <v-list-item-avatar>
          <v-img alt="Avatar" src="https://via.placeholder.com/150" />
        </v-list-item-avatar>
        <v-list-item-content>
          <v-list-item-title>Lorem Ipsum</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
      <v-list-item v-for="n in 3" :key="n" link>
        <v-list-item-icon>
          <v-icon>mdi-record</v-icon>
        </v-list-item-icon>
        <v-list-item-content>
          <v-list-item-title>Lorem ipsum</v-list-item-title>
        </v-list-item-content>
      </v-list-item>
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
export default Vue.extend({
  asyncData: () => ({}),
  data: () => ({ drawer: false }),
  mounted() {
    EventBus.$on('toggle', () => {
      this.drawer = !this.drawer
    })
  }
})
</script>
