<template>
  <v-content>
    <v-container
      class="background"
      :style="{
        'background-size': $vuetify.breakpoint.lgAndUp ? 'contain' : 'cover'
      }"
      fluid
    >
      <v-row align="center">
        <v-col
          :class="[
            'd-flex font-weight-black justify-center text-resize text-uppercase',
            $vuetify.breakpoint.mdAndUp ? 'display-3' : 'display-2',
            { 'text-center': $vuetify.breakpoint.xs }
          ]"
          cols="12"
          order-sm="2"
          sm="6"
          style="max-width: 100%; word-spacing: 100vw;"
          v-text="env.title"
        />
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
                    :active-class="$vuetify.theme.dark ? 'dark' : 'light'"
                    :aria-label="window.name"
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
          <v-window v-model="count" continuous show-arrows show-arrows-on-hover>
            <v-window-item v-for="window in windows" :key="window.icon">
              <v-container>
                <v-row justify="center">
                  <client-only>
                    <kinesis-container>
                      <kinesis-element :style="resetTransform">
                        <kinesis-element
                          :strength="2.5"
                          :style="resetTransform"
                          type="rotate"
                        >
                          <v-icon
                            color="secondary"
                            size="250"
                            @mouseenter.stop="hover = true"
                            @mouseleave.stop="hover = false"
                            v-text="window.icon"
                          />
                        </kinesis-element>
                      </kinesis-element>
                    </kinesis-container>
                  </client-only>
                </v-row>
                <v-row justify="center">
                  <v-card color="transparent" elevation="0">
                    <v-card-title
                      class="font-weight-bold justify-center pa-0"
                      style="font-size: 2.25rem;"
                      v-text="window.name"
                    />
                    <v-card-actions class="font-weight-bold justify-center">
                      <v-chip-group color="primary">
                        <v-chip
                          v-for="n in 3"
                          :key="n"
                          :to="`#Mode-${n}`"
                          class="ma-2"
                          exact
                          nuxt
                          pill
                        >
                          <v-avatar left>
                            <v-icon>mdi-record</v-icon>
                          </v-avatar>
                          Lorem
                        </v-chip>
                      </v-chip-group>
                    </v-card-actions>
                  </v-card>
                </v-row>
              </v-container>
            </v-window-item>
          </v-window>
        </v-col>
      </v-row>
    </v-container>
    <v-sheet color="accent" height="1000" style="min-height: 100%;" />
    <v-fab-transition>
      <v-btn
        aria-label="Top"
        absolute
        fab
        bottom
        right
        @click.stop="$vuetify.goTo(0)"
      >
        <v-icon>mdi-arrow-up-thick</v-icon>
      </v-btn>
    </v-fab-transition>
  </v-content>
</template>

<script lang="ts">
import Vue from 'vue'
import { mapState } from 'vuex'
export default Vue.extend({
  data: () => ({
    count: 0,
    hover: false,
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
  }),
  computed: {
    ...mapState(['env', 'hydrated']),
    resetTransform() {
      return this.hover ? '' : 'transform: none;'
    }
  }
})
</script>

<style lang="scss" scoped>
@media (max-width: 400px) {
  .text-resize {
    font-size: 2.25rem !important;
  }
}
button {
  &.light {
    color: black !important;
  }
  &.dark {
    color: white !important;
  }
}
.background {
  background: url('/images/chess-background.svg') center;
}
</style>
