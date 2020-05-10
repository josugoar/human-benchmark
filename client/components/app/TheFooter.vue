<template>
  <v-footer absolute app>
    <v-container>
      <v-row align="center" justify="center">
        Powered by
        <v-btn
          v-for="reference in references"
          :key="reference.name"
          :href="reference.url"
          aria-label="Reference"
          class="ml-1"
          rel="noopener"
          target="_blank"
          icon
        >
          <v-avatar size="25" tile>
            <v-img
              :alt="reference.name"
              :src="require(`@/assets/icons/${reference.icon}`)"
              contain
            />
          </v-avatar>
        </v-btn>
      </v-row>
    </v-container>
  </v-footer>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data() {
    return {
      references: [
        {
          icon: 'nuxt.png',
          name: 'Nuxt.js',
          url: 'https://www.nuxtjs.org/'
        },
        {
          icon: 'django.png',
          name: 'Django',
          url: 'https://www.djangoproject.com/'
        },
        {
          icon: 'tensorflow.png',
          name: 'TensorFlow',
          url: 'https://www.tensorflow.org/'
        }
      ]
    }
  }
})
</script>
