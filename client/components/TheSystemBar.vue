<template>
  <v-system-bar app>
    <v-spacer />
    <v-btn v-for="game in games" :key="game.id">
      <v-icon>{{ game.icon }}</v-icon>
    </v-btn>
  </v-system-bar>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      games: [
        {
          id: 1,
          icon: 'Game 1'
        },
        {
          id: 2,
          icon: 'Game 2'
        },
        {
          id: 3,
          icon: 'Game 3'
        }
      ]
    }
  }
})
</script>
