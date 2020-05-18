<template>
  <v-footer absolute app>
    <v-container>
      <v-row align="center" justify="center">
        Powered by
        <v-btn
          v-for="reference in references"
          :key="reference.name"
          :aria-label="reference.name"
          :href="reference.url"
          class="mx-1"
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
  data: () => ({
    references: [
      {
        name: 'Nuxt.js',
        icon: 'nuxt.png',
        url: 'https://www.nuxtjs.org/'
      },
      {
        name: 'Django',
        icon: 'django.png',
        url: 'https://www.djangoproject.com/'
      },
      {
        name: 'TensorFlow',
        icon: 'tensorflow.png',
        url: 'https://www.tensorflow.org/'
      }
    ]
  })
})
</script>
