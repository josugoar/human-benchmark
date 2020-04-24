<template>
  <v-card>
    <v-app-bar dark>
      <v-app-bar-nav-icon>
        <v-icon>mdi-cursor-text</v-icon>
      </v-app-bar-nav-icon>
      <v-toolbar-title>TypeTest</v-toolbar-title>
      <v-spacer></v-spacer>
      <v-toolbar-items>
        <v-tabs
          background-color="transparent"
          height="100%"
          optional
          right
          show-arrows
        >
          <v-tab to="#practice" nuxt>
            <v-icon left>mdi-flash</v-icon>
            Practice
          </v-tab>
          <v-tab to="#scores" nuxt>
            <v-icon left>mdi-chart-bell-curve</v-icon>
            Scores
          </v-tab>
        </v-tabs>
      </v-toolbar-items>
    </v-app-bar>
  </v-card>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({})
</script>

<style lang="scss" scoped>
.v-tab__items {
  height: 100%;
}
</style>
