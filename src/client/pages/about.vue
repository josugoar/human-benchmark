<template>
  <v-content class="ma-10">
    <v-expansion-panels inset focusable multiple>
      <v-expansion-panel v-for="panel in panels" :key="panel.header">
        <v-expansion-panel-header v-text="panel.header" />
        <v-expansion-panel-content class="pa-5" v-text="panel.content" />
      </v-expansion-panel>
    </v-expansion-panels>
  </v-content>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      panels: [
        {
          header: 'Header 1',
          content:
            'Lorem ipsum dolor sit amet consectetur adipisicing elit. Asperiores, quisquam, ipsum nam magni autem corrupti expedita minus quos eum, nisi hic sapiente ratione ex placeat vel deserunt ad sunt nesciunt.'
        },
        {
          header: 'Header 2',
          content:
            'Lorem ipsum dolor sit amet consectetur adipisicing elit. Asperiores, quisquam, ipsum nam magni autem corrupti expedita minus quos eum, nisi hic sapiente ratione ex placeat vel deserunt ad sunt nesciunt.'
        },
        {
          header: 'Header 3',
          content:
            'Lorem ipsum dolor sit amet consectetur adipisicing elit. Asperiores, quisquam, ipsum nam magni autem corrupti expedita minus quos eum, nisi hic sapiente ratione ex placeat vel deserunt ad sunt nesciunt.'
        }
      ]
    }
  }
})
</script>
