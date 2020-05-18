<template>
  <v-system-bar class="ma-1" color="transparent">
    <v-spacer />
    <v-btn
      v-for="button in buttons"
      :key="button.label"
      class="mx-1"
      text
      x-small
      v-text="button.label"
    />
  </v-system-bar>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data: () => ({
    buttons: [
      {
        label: 'Log In'
      },
      {
        label: 'Log Out'
      }
    ]
  })
})
</script>
