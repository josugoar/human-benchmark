<template>
  <v-content>
    <v-expansion-panels class="ma-10" inset focusable multiple>
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
  data: () => ({
    panels: [
      {
        header: 'Lorem ipsum 1',
        content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'
      },
      {
        header: 'Lorem ipsum 2',
        content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'
      },
      {
        header: 'Lorem ipsum 3',
        content: 'Lorem ipsum dolor sit amet consectetur adipisicing elit.'
      }
    ]
  })
})
</script>
