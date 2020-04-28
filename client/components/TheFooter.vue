<template>
  <v-footer absolute app>
    <v-container>
      <v-row align="center" justify="center">
        {{ msg }}
        <v-btn
          v-for="framework in frameworks"
          :key="framework.id"
          :href="framework.url"
          class="ml-1"
          target="_blank"
          icon
        >
          <v-avatar size="25" tile>
            <v-img
              :alt="framework.name"
              :src="require(`@/assets/icons/${framework.icon}`)"
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
      msg: 'Powered by',
      frameworks: [
        {
          id: 1,
          name: 'Nuxt.js',
          url: 'https://www.nuxtjs.org/',
          icon: 'nuxt-icon.png'
        },
        {
          id: 2,
          name: 'Django',
          url: 'https://www.djangoproject.com/',
          icon: 'django-icon.png'
        },
        {
          id: 3,
          name: 'TensorFlow',
          url: 'https://www.tensorflow.org/',
          icon: 'tensorflow-icon.png'
        }
      ]
    }
  }
})
</script>
