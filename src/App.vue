<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-home</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Home</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link>
          <v-list-item-action>
            <v-icon>mdi-email</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Contact</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      color="indigo"
      dark
    >
      <v-app-bar-nav-icon @click.stop="drawer = !drawer"></v-app-bar-nav-icon>
      <v-toolbar-title>👍/👎 Twitter Sentiment Analysis</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <SingleTweet/>
    </v-main>
    <v-footer
      color="indigo"
      app
    >
      <span class="white--text">&copy; NLP Twitter sentiment analysis by <a href="https://github.com/LorenRd">LorenRD</a></span>
    </v-footer>
  </v-app>
</template>

<script>
  import SingleTweet from './components/SingleTweet.vue';
  export default {
    components: {
      SingleTweet
    },
    data: () => ({
      drawer: null,
    }),
  }
</script>