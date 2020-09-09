<template>
  <div>
  <v-progress-linear v-show="hashtagsLoading" indeterminate color="cyan" />
  <v-form ref="form">
    <v-container
      class="fill-height"
      fluid
    >
    <v-row
        align="center"
        justify="center"
      >
      <h2>Trending topics</h2>
      </v-row>
      <v-row
        align="center"
        justify="center"
       v-if="!hashtagsLoading">
        <v-col cols="12" sm="6" md="3">
              <h3>#{{Object.keys(trends)[1]}}</h3>
              <TwitterCard v-for="tw in Object.entries(trends)[0][1]" :key="tw.id" :tweetBody="tw.text" :username="tw.user" :score="tw.score" :userProfile="tw.profileImage" :label="tw.label"/>
        </v-col>
        <v-col cols="12" sm="6" md="3">
              <h3>#{{Object.keys(trends)[1]}}</h3>
              <TwitterCard v-for="tw in Object.entries(trends)[1][1]" :key="tw.id" :tweetBody="tw.text" :username="tw.user" :score="tw.score" :userProfile="tw.profileImage" :label="tw.label"/>
        </v-col>
        <v-col cols="12" sm="6" md="3">
              <h3>#{{Object.keys(trends)[2]}}</h3>
              <TwitterCard v-for="tw in Object.entries(trends)[2][1]" :key="tw.id" :tweetBody="tw.text" :username="tw.user" :score="tw.score" :userProfile="tw.profileImage" :label="tw.label"/>
        </v-col>
      </v-row>
      <v-row
        align="center"
        justify="center"
       v-else>
           <v-progress-circular
              :size="70"
              :width="7"
              color="primary"
              indeterminate
            ></v-progress-circular>
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
        hashtagsLoading: true,
        trends: {}
      }
    },
    mounted(){

      axios.get("http://127.0.0.1:5000/hashtags", {headers: {"Access-Control-Allow-Origin": "*"}})
      .then((result) => {
        let hashtags = {};
        Object.keys(result.data).forEach(key => {
          hashtags[key] = result.data[key]
        })
        this.trends = hashtags;
        this.hashtagsLoading = false;
      });
    },
  methods: {
    }

    }
</script>
