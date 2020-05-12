<template>
  <v-content class="primary">
    <v-container class="background" fluid>
      <v-row align="center">
        <v-col
          :class="[
            'd-flex font-weight-black justify-center resizable-text text-uppercase',
            { 'text-center': $vuetify.breakpoint.xs },
            $vuetify.breakpoint.mdAndUp ? 'display-3' : 'display-2'
          ]"
          cols="12"
          order-sm="2"
          sm="6"
          style="max-width: inherit;"
        >
          <template v-for="(word, idx) in env.title.split(' ')">
            {{ word }}
            <br :key="idx" />
          </template>
        </v-col>
        <v-col>
          <v-item-group
            v-model="count"
            class="d-flex justify-space-around"
            mandatory
          >
            <v-item
              v-for="window in windows"
              #default="{ active, toggle }"
              :key="window.icon"
            >
              <v-tooltip top>
                {{ window.name }}
                <template #activator="{ on }">
                  <v-btn
                    :aria-label="window.name"
                    :input-value="active"
                    active-class="active"
                    icon
                    v-on="on"
                    @click.stop="toggle"
                  >
                    <v-icon size="25">mdi-record</v-icon>
                  </v-btn>
                </template>
              </v-tooltip>
            </v-item>
          </v-item-group>
        </v-col>
      </v-row>
      <v-row align="center">
        <v-col>
          <v-window v-model="count" continuous show-arrows show-arrows-on-hover>
            <v-window-item v-for="window in windows" :key="window.icon">
              <v-container fluid>
                <v-row justify="center">
                  <client-only>
                    <kinesis-container>
                      <kinesis-element>
                        <v-icon
                          color="secondary"
                          size="200"
                          v-text="window.icon"
                        />
                      </kinesis-element>
                    </kinesis-container>
                  </client-only>
                </v-row>
                <v-row justify="center">
                  {{ window.name }}
                </v-row>
              </v-container>
            </v-window-item>
          </v-window>
        </v-col>
      </v-row>
    </v-container>
    <v-sheet color="accent" height="1000" />
    <v-fab-transition>
      <v-btn aria-label="Top" absolute fab bottom right>
        <v-icon>mdi-arrow-up-thick</v-icon>
      </v-btn>
    </v-fab-transition>
  </v-content>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapState } from 'vuex'
export default Vue.extend({
  data() {
    return {
      count: 0,
      windows: [
        {
          icon: 'mdi-chess-king',
          name: 'Classic',
          text: 'Lorem Ipsum Dolor Sit Amet'
        },
        {
          icon: 'mdi-chess-queen',
          name: 'Blitz',
          text: 'Lorem Ipsum Dolor Sit Amet'
        },
        {
          icon: 'mdi-chess-bishop',
          name: 'Lorem',
          text: 'Lorem Ipsum Dolor Sit Amet'
        },
        {
          icon: 'mdi-chess-knight',
          name: 'Lorem',
          text: 'Lorem Ipsum Dolor Sit Amet'
        }
      ]
    }
  },
  computed: {
    ...mapState(['env', 'hydrated'])
  }
})
</script>

<style lang="scss" scoped>
@media (max-width: 400px) {
  .resizable-text {
    font-size: 2.25rem !important;
  }
}
// TODO: Fix
.active {
  color: var(--v-secondary-base) !important;
}
.background {
  background: url('/images/chess-background.svg') center;
  background-size: cover;
}
</style>
