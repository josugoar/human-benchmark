<template>
  <v-fab-transition>
    <v-btn
      v-show="offsetTop > threshold"
      v-scroll="onScroll"
      aria-label="Top"
      bottom
      fab
      fixed
      right
      @click.stop="$vuetify.goTo(goTo)"
    >
      <v-icon>mdi-arrow-up-thick</v-icon>
    </v-btn>
  </v-fab-transition>
</template>

<script lang="ts">
import Vue from 'vue'
import OffsetThreshold from '@/components/utils/OffsetThreshold'
export default Vue.extend({
  mixins: [OffsetThreshold],
  props: {
    goTo: { type: Number, default: 0 },
    threshold: { type: Number, default: 100 }
  }
})
</script>
