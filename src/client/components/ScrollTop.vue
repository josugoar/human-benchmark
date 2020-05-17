<template>
  <v-fab-transition>
    <v-btn
      v-show="offsetTop > 10"
      v-scroll="onScroll"
      aria-label="Top"
      fab
      fixed
      bottom
      right
      @click.stop="$vuetify.goTo(goTo)"
    >
      <v-icon>mdi-arrow-up-thick</v-icon>
    </v-btn>
  </v-fab-transition>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  props: { goTo: { type: Number, default: 0 } },
  data: () => ({ offsetTop: 0 }),
  methods: {
    onScroll() {
      this.offsetTop = window.scrollY
    }
  }
})
</script>
