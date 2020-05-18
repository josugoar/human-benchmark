<template>
  <v-system-bar class="ma-1" color="transparent">
    <v-spacer />
    <v-btn
      v-for="button in buttons"
      :key="button.text"
      class="mx-1"
      text
      x-small
      v-text="button.text"
    />
  </v-system-bar>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data: () => ({
    buttons: [
      {
        text: 'Log In'
      },
      {
        text: 'Log Out'
      }
    ]
  })
})
</script>
