<template>
  <v-content class="primary">
    <v-container style="height: 100vh;" fluid>
      <v-row align="center">
        <v-col
          :class="[
            $vuetify.breakpoint.xs ? 'text-center' : '',
            $vuetify.breakpoint.mdAndUp ? 'display-3' : 'display-2'
          ]"
          class="d-flex font-weight-black justify-center text-uppercase"
          cols="12"
          order-sm="2"
          sm="6"
          style="color: var(--v-secondary-base); margin: 12px;"
        >
          Human
          <br />
          Benchmark
        </v-col>
        <v-col>
          <v-item-group
            v-model="window"
            class="d-flex justify-space-around"
            mandatory
          >
            <v-item v-for="n in length" #default="{ active, toggle }" :key="n">
              <v-tooltip top>
                <template v-slot:activator="{ on }">
                  <v-btn
                    :input-value="active"
                    active-class="active"
                    icon
                    v-on="on"
                    @click.stop="toggle"
                  >
                    <v-icon>
                      mdi-record
                    </v-icon>
                  </v-btn>
                </template>
                Lorem ipsum
              </v-tooltip>
            </v-item>
          </v-item-group>
        </v-col>
      </v-row>
      <v-row align="center">
        <v-col>
          <v-window
            v-model="window"
            continuous
            show-arrows
            show-arrows-on-hover
          >
            <v-window-item v-for="n in length" :key="n">
              <v-container>
                <v-row justify="center">
                  <client-only>
                    <kinesis-container>
                      <kinesis-element>
                        <v-icon color="secondary" size="200">
                          mdi-chess-king
                        </v-icon>
                      </kinesis-element>
                    </kinesis-container>
                  </client-only>
                </v-row>
                <v-row justify="center" style="color: var(--v-secondary-base);">
                  Lorem Ipsum Dolor Sit Amet
                </v-row>
              </v-container>
            </v-window-item>
          </v-window>
        </v-col>
      </v-row>
    </v-container>
    <!-- <v-fab-transition>
      <v-btn absolute fab bottom right>
        <v-icon>
          mdi-arrow-down-thick
        </v-icon>
      </v-btn>
    </v-fab-transition> -->
  </v-content>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'Home',
  data() {
    return {
      length: 5,
      window: 0
    }
  }
})
</script>

<style lang="scss" scoped>
.active {
  color: var(--v-secondary-base) !important;
}
</style>
