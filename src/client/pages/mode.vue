<template>
  <v-content>
    <v-container
      :style="{
        background: 'url(images/chess-background.svg) center',
        'background-size': $vuetify.breakpoint.lgAndUp ? 'contain' : 'cover'
      }"
      fluid
    >
      <v-row align="center">
        <v-col
          :class="[
            'd-flex font-weight-black justify-center text-uppercase',
            $vuetify.breakpoint.mdAndUp ? 'display-3' : 'display-2',
            { 'text-center': $vuetify.breakpoint.xs }
          ]"
          cols="12"
          order-sm="2"
          sm="6"
          style="max-width: 100%; word-spacing: 100vw;"
        >
          Human Benchmark
        </v-col>
        <v-col>
          <v-item-group
            v-model="window"
            class="d-flex justify-space-around"
            mandatory
          >
            <v-item
              v-for="window in windows"
              #default="{ active, toggle }"
              :key="window.title"
            >
              <v-tooltip top>
                {{ window.title }}
                <template #activator="{ on }">
                  <v-btn
                    :active-class="$vuetify.theme.dark ? 'dark' : 'light'"
                    :aria-label="window.title"
                    :input-value="active"
                    color="accent"
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
      <v-row>
        <v-col>
          <v-window
            v-model="window"
            continuous
            show-arrows
            show-arrows-on-hover
          >
            <v-window-item v-for="window in windows" :key="window.title">
              <v-row justify="center">
                <v-card
                  class="ma-1 mb-4 text-center"
                  color="transparent"
                  to="#"
                  width="300"
                  hover
                  @mouseenter.stop="isHovering = true"
                  @mouseleave.stop="isHovering = false"
                >
                  <kinesis-container>
                    <kinesis-element
                      :style="!isHovering ? 'transform: none;' : ''"
                      type="depth"
                    >
                      <v-icon color="primary" size="250" v-text="window.icon" />
                    </kinesis-element>
                    <v-card-title
                      class="display-1 font-weight-black justify-center pa-0"
                      v-text="window.title"
                    />
                    <v-card-subtitle class="my-1" v-text="window.subtitle" />
                  </kinesis-container>
                </v-card>
              </v-row>
            </v-window-item>
          </v-window>
        </v-col>
      </v-row>
    </v-container>
    <v-sheet color="accent" height="1000" style="min-height: 100%;" />
  </v-content>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapState } from 'vuex'
export default Vue.extend({
  data: () => ({
    isHovering: false,
    window: 0,
    windows: [
      {
        title: 'Classic',
        subtitle: 'Good old fashioned chess',
        icon: 'mdi-chess-king'
      },
      {
        title: 'Blitz',
        subtitle: 'Hectic fast paced encounters',
        icon: 'mdi-chess-queen'
      },
      {
        title: 'Custom',
        subtitle: 'Fully personalizable matches',
        icon: 'mdi-chess-bishop'
      },
      {
        title: 'Puzzle',
        subtitle: 'Engaging bite sized challenges',
        icon: 'mdi-chess-knight'
      }
    ]
  }),
  computed: {
    ...mapState(['hydrated'])
  }
})
</script>

<style lang="scss" scoped>
button {
  &.light {
    color: black !important;
  }
  &.dark {
    color: white !important;
  }
}
</style>
