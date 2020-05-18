<template>
  <v-content>
    <v-card class="ma-5">
      <v-card-title>
        Global
        <v-spacer></v-spacer>
        <v-text-field
          v-model="search"
          append-icon="mdi-magnify"
          label="Search"
          clearable
        />
      </v-card-title>
      <v-data-table
        :headers="headers"
        :items="values"
        :search="search"
        hide-default-footer
      />
      <v-pagination
        v-model="page"
        :length="pageCount"
        class="my-1"
        total-visible="10"
        circle
      />
    </v-card>
  </v-content>
</template>

<script lang="ts">
import Vue from 'vue'
export default Vue.extend({
  data: () => ({
    page: 1,
    pageCount: 50,
    search: '',
    headers: [
      { text: 'User', sortable: false, value: 'user' },
      { text: 'ELO', value: 'elo' },
      { text: 'Wins', value: 'wins' },
      { text: 'Loses', value: 'loses' },
      { text: 'Ratio', value: 'ratio' }
    ],
    values: [
      {
        user: 'JoshGA',
        elo: 118,
        wins: 21,
        loses: 16,
        ratio: 21 / 16
      },
      {
        user: 'JoshGA',
        elo: 118,
        wins: 21,
        loses: 16,
        ratio: 21 / 16
      },
      {
        user: 'JoshGA',
        elo: 118,
        wins: 21,
        loses: 16,
        ratio: 21 / 16
      },
      {
        user: 'JoshGA',
        elo: 118,
        wins: 21,
        loses: 16,
        ratio: 21 / 16
      },
      {
        user: 'JoshGA',
        elo: 118,
        wins: 21,
        loses: 16,
        ratio: 21 / 16
      },
      {
        user: 'JoshGA',
        elo: 118,
        wins: 21,
        loses: 16,
        ratio: 21 / 16
      },
      {
        user: 'JoshGA',
        elo: 118,
        wins: 21,
        loses: 16,
        ratio: 21 / 16
      },
      {
        user: 'JoshGA',
        elo: 118,
        wins: 21,
        loses: 16,
        ratio: 21 / 16
      },
      {
        user: 'JoshGA',
        elo: 118,
        wins: 21,
        loses: 16,
        ratio: 21 / 16
      },
      {
        user: 'JoshGA',
        elo: 118,
        wins: 21,
        loses: 16,
        ratio: 21 / 16
      }
    ]
  })
})
</script>
