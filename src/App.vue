<template>
  <v-app id="inspire">
    <v-navigation-drawer
      v-model="drawer"
      app
    >
      <v-list dense>
        <v-list-item link v-on:click="view = 'home'"> 
          <v-list-item-action>
            <v-icon>mdi-card-text</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Text Analysis</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link v-on:click="view = 'accounts'"> 
          <v-list-item-action>
            <v-icon>mdi-account</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Twitter Accounts</v-list-item-title>
          </v-list-item-content>
        </v-list-item>
        <v-list-item link v-on:click="view = 'hashtags'">
          <v-list-item-action>
            <v-icon>mdi-pound</v-icon>
          </v-list-item-action>
          <v-list-item-content>
            <v-list-item-title>Hashtags</v-list-item-title>
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
      <v-toolbar-title>👍/👎 NLP Sentiment Analysis</v-toolbar-title>
    </v-app-bar>

    <v-main>
      <SingleTweet v-if="view === 'home'"/>
      <Hashtags v-if="view === 'hashtags'"/>
      <Accounts v-if="view === 'accounts'"/>
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
  import Hashtags from './components/Hashtags.vue';
  import Accounts from './components/Accounts.vue';

  export default {
    components: {
      SingleTweet,
      Hashtags,
      Accounts
    },
    data: () => ({
      drawer: null,
      view: 'home'
    }),
  }
</script>