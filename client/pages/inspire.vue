<template>
  <v-layout>
    <v-flex class="text-center">
      <img src="/v.png" alt="Vuetify.js" class="mb-5" />
      <strong>{{ random }}</strong>
      <blockquote class="blockquote">
        &#8220;First, solve the problem. Then, write the code.&#8221;
        <footer>
          <small>
            <em>&mdash;John Johnson</em>
          </small>
        </footer>
      </blockquote>
    </v-flex>
  </v-layout>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'Home',
  data() {
    return {
      random: 0
    }
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
  },
  created() {
    this.randomize()
  }
})
</script>
