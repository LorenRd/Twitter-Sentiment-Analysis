<template>
  <div>
  <v-progress-linear v-show="hashtagsLoading" indeterminate color="cyan" />
  <v-form ref="form" @submit.prevent="getUserInfo()">
    <v-container
      class="fill-height"
      fluid
    >
    <v-row
        align="center"
        justify="center"
      >
      <h1>Hashtag analyser</h1>
          </v-row>
      <v-row
        align="center"
        justify="center"
      >
        <v-col cols="12" sm="6" md="3">
              <v-text-field prepend-inner-icon="mdi-pound" v-model="hashtag" :rules="[rules.required]"  label="Hashtag"
              ></v-text-field><v-btn :disabled="hashtagsLoading" type="submit" color="primary">Search!</v-btn>
        </v-col>
      </v-row>
      <v-row
          align="center"
          justify="center"
        >
          <TwitterCard v-for="tw in tweets" :key="tw.id" :tweetBody="tw.text" :username="tw.user" :score="tw.score" :userProfile="tw.profileImage" :label="tw.label"/>
      </v-row>
    </v-container>
  </v-form>
  </div>
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
        hashtag: '',
        hashtagsLoading: false,
        tweets: [],
        rules: {
          required: value => !!value || 'Required.',
        },
      }
    },
  methods: {
      searchUsername(hashtag){
        this.hashtagsLoading = true;
        axios.post("http://127.0.0.1:5000/hashtag", {"hashtag": hashtag}, {headers: {"Access-Control-Allow-Origin": "*"}})
        .then((result) => {
          this.tweets = result.data;
          this.hashtagsLoading = false;
          console.log(this.tweets)
        });
      },
      getUserInfo(){
        if(this.$refs.form.validate()){
          let hashtagInfo = this.searchUsername(this.hashtag);
        }
      }
    }

  }
</script>
