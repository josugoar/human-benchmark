<template>
  <v-content>
    <v-card style="min-height: 100vh">
      <v-container style="min-height: 100vh" fill-height>
        <v-col>
          <v-card>
            <v-card-title>
              Lorem
            </v-card-title>
            <v-card-text>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia
              minus natus totam dolore, atque sapiente? Fugit, libero
              praesentium officia culpa, illo laboriosam dolorem ipsam repellat,
              magni provident necessitatibus accusantium. Ipsa!
            </v-card-text>
            <v-card-actions>
              <v-row justify="center">
                <v-btn>
                  Lorem Ipsum
                </v-btn>
              </v-row>
            </v-card-actions>
          </v-card>
        </v-col>
        <v-col>
          <v-img aspect-ratio="1" src="images/bust-1.png" contain />
        </v-col>
      </v-container>
    </v-card>
    <v-container>
      <v-row v-for="i in 2" :key="i">
        <v-col v-for="j in 2" :key="j">
          <v-card>
            <v-img src="https://via.placeholder.com/150" />
            <v-card-title>
              Lorem
            </v-card-title>
            <v-card-text>
              Lorem ipsum dolor sit amet consectetur adipisicing elit. Quia
              minus natus totam dolore, atque sapiente? Fugit, libero
              praesentium officia culpa, illo laboriosam dolorem ipsam repellat,
              magni provident necessitatibus accusantium. Ipsa!
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-content>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  name: 'Home'
})
</script>

<style lang="scss" scoped></style>
