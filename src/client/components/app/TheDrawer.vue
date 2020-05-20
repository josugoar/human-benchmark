<template>
  <v-navigation-drawer v-model="drawer" app temporary>
    <TheSystemBar />
    <v-list nav>
      <v-container>
        <v-list-item>
          <v-list-item-avatar left>
            <v-img alt="Avatar" src="https://via.placeholder.com/150" />
          </v-list-item-avatar>
          <v-list-item-content>
            <v-list-item-title v-text="user.name" />
            <v-list-item-subtitle v-text="'GrandMaster'" />
          </v-list-item-content>
          <v-list-item-action>
            <v-btn aria-label="Settings" icon>
              <v-icon>mdi-cog</v-icon>
            </v-btn>
          </v-list-item-action>
        </v-list-item>
        <v-row justify="space-around">
          <template v-for="(card, idx) in cards">
            <v-col :key="card.title" class="d-flex justify-center pa-0">
              <v-icon v-text="card.icon" />
              <v-card color="transparent" height="50" flat>
                <v-card-title class="caption" v-text="card.subtitle" />
                <v-card-subtitle
                  class="overline"
                  v-text="card.title.toUpperCase()"
                />
              </v-card>
            </v-col>
            <v-divider v-if="idx % 2 === 0" :key="card.icon" inset vertical />
          </template>
        </v-row>
      </v-container>
      <v-divider />
      <v-subheader>Profile</v-subheader>
      <v-list-item-group>
        <v-list-item
          v-for="item in items"
          :key="item.title"
          :to="item.url"
          exact
          nuxt
        >
          <v-list-item-icon>
            <v-icon v-text="item.icon" />
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.title" />
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
    </v-list>
    <template #append>
      <v-row justify="center">
        <v-switch
          v-model="$vuetify.theme.dark"
          prepend-icon="mdi-theme-light-dark"
        />
      </v-row>
    </template>
  </v-navigation-drawer>
</template>

<script lang="ts">
import Vue from 'vue'
import { User } from 'lib'
import TheSystemBar from '@/components/app/TheSystemBar.vue'
import { EventBus } from '@/components/utils/EventBus'
export default Vue.extend({
  components: {
    TheSystemBar
  },
  data: () => ({
    drawer: false,
    cards: [
      {
        title: 'ELO',
        subtitle: 108,
        icon: 'mdi-alpha-e-box'
      },
      {
        title: 'Wins',
        subtitle: 64,
        icon: 'mdi-trophy'
      }
    ],
    items: [
      {
        title: 'Dashboard',
        icon: 'mdi-view-dashboard',
        url: '#'
      }
    ],
    user: {
      name: 'JoshGoA',
      elo: 108,
      history: {
        wins: 59,
        losses: 27
      }
    } as User
  }),
  mounted() {
    EventBus.$on('toggle', () => (this.drawer = !this.drawer))
  }
})
</script>
