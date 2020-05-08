<template>
  <v-navigation-drawer app temporary>
    <v-list-item>
      <v-list-item-avatar>
        <v-img src="https://via.placeholder.com/150" />
      </v-list-item-avatar>
      <v-list-item-content>
        <v-list-item-title v-text="text" />
      </v-list-item-content>
    </v-list-item>
  </v-navigation-drawer>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      text: 'Lorem Ipsum'
    }
  }
})
</script>
