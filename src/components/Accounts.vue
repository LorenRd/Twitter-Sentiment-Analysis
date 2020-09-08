<template>
  <v-form ref="form" @submit.prevent="getUserInfo()">
    <v-container
      class="fill-height"
      fluid
    >
    <v-row
        align="center"
        justify="center"
      >
      <h1>Account analyser</h1>
          </v-row>
      <v-row
        align="center"
        justify="center"
      >
        <v-col cols="12" sm="6" md="3">
              <v-text-field prepend-inner-icon="mdi-account" v-model="username" :rules="[rules.required]"  label="@username"
              ></v-text-field><v-btn type="submit" color="primary">Search!</v-btn>
        </v-col>
      </v-row>
      <v-row
          align="center"
          justify="center"
        >
          <TwitterCard v-for="tw in tweets" :key="tw.id" :tweetBody="tw.text" :username="twitterName" :score="tw.score" :userProfile="twitterImage" :label="tw.label"/>
      </v-row>
    </v-container>
  </v-form>
</template>

<script>
  import axios from "axios";
  import TwitterCard from './TwitterCard.vue';

  export default {
    components: {
      TwitterCard
    },
    data(){
      return {
        username: '',
        twitterName: '',
        twitterImage: '',
        tweets: [],
        rules: {
          required: value => !!value || 'Required.',
        },
      }
    },
  methods: {
      searchUsername(username){
        axios.post("http://127.0.0.1:5000/account", {"userAccount": username}, {headers: {"Access-Control-Allow-Origin": "*"}})
        .then((result) => {
          this.twitterName = result.data.profileInfo.user;
          this.twitterImage = result.data.profileInfo.profileImage;
          this.tweets = result.data.tweets;
          console.log(result.data)
        });
      },
      getUserInfo(){
        if(this.$refs.form.validate()){
          let usernameInfo = this.searchUsername(this.username);
        }
      }
    }

  }
</script>
