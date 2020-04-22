<template>
  <v-layout>
    <strong>{{ random }}</strong>
  </v-layout>
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
    }
  }
})
</script>
