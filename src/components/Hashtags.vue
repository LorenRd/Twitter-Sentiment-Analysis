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
      <h2>Hashtags</h2>
      </v-row>
      <v-row
        align="center"
        justify="center"
      >
        <v-col cols="12" sm="6" md="3">
              <h3>#{{Object.keys(trends)[0]}}</h3>
              <TwitterCard v-for="tw in Object.values(Object.keys(trends)[0])" :key="tw.id" :tweetBody="tw.text" :username="twitterName" :score="tw.score" :userProfile="twitterImage" :label="tw.label"/>
        </v-col>
        <v-col cols="12" sm="6" md="3">
              <h3>#{{Object.keys(trends)[1]}}</h3>
              <TwitterCard />
        </v-col>
        <v-col cols="12" sm="6" md="3">
              <h3>#{{Object.keys(trends)[2]}}</h3>
              <TwitterCard />
        </v-col>
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
        this.hashtagsLoading = false;
        this.trends = result.data;
        console.log(this.trends)
      });
    },
  methods: {
    }

    }
</script>
