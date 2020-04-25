<template>
  <v-content class="vaporwave-bg">
    <v-container class="sunset-bg" fill-height>
      <strong @click="randomize">
        {{ random }}
      </strong>
    </v-container>
  </v-content>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'Home',
  asyncData() {},
  data() {
    return {
      random: 0
    }
  },
  created() {
    this.randomize()
  },
  methods: {
    async randomize() {
      const path = 'http://localhost:5000/api'
      await this.$axios
        .get(path)
        .then((response) => {
          this.random = response.data
        })
        .catch((error) => {
          console.log(error)
        })
    },
    offset() {}
  }
})
</script>

<style lang="scss" scoped>
.vaporwave-bg {
  background-image: url('/images/vaporwave-background.svg');
  background-position: center center;
  background-size: cover;
}
.sunset-bg {
  background-image: url('/images/sunset.png');
  background-position: center center;
  background-size: cover;
}
</style>
