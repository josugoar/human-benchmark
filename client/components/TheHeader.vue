<template>
  <v-app-bar app short>
    <v-app-bar-nav-icon class="d-flex d-sm-none" />
    <v-toolbar-title class="pa-0">
      <v-container align="center">
        <v-icon>
          mdi-cursor-text
        </v-icon>
        Type
        <strong>
          Test
        </strong>
      </v-container>
    </v-toolbar-title>
    <v-spacer />
    <v-toolbar-items>
      <v-tabs
        background-color="transparent"
        class="d-none d-sm-flex"
        height="100%"
        mobile-break-point="0"
        optional
      >
        <v-tab v-for="page in pages" :key="page.id" :to="page.url" nuxt>
          <v-icon left>
            {{ page.icon }}
          </v-icon>
          {{ page.name }}
        </v-tab>
      </v-tabs>
    </v-toolbar-items>
  </v-app-bar>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      pages: [
        {
          id: 1,
          name: 'Practice',
          url: '#practice',
          icon: 'mdi-flash'
        },
        {
          id: 2,
          name: 'Scores',
          url: '#scores',
          icon: 'mdi-chart-bell-curve'
        }
      ]
    }
  }
})
</script>
