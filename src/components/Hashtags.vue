<template>
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
              <h3>#Topic1</h3>
              <TwitterCard />
        </v-col>
        <v-col cols="12" sm="6" md="3">
              <h3>#Topic2</h3>
              <TwitterCard />
        </v-col>
        <v-col cols="12" sm="6" md="3">
              <h3>#Topic3</h3>
              <TwitterCard />
        </v-col>
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
        text: '',
        modelLoaded: false,
        rules: {
          required: value => !!value || 'Required.',
          counter: value => value.length <= 250 || 'Max 250 characters',
        },
      }
    },
  methods: {
      stringCleaner(text){
        return text.toLowerCase().trim().replace(/@\S+|https?:\S+|http?:\S|[^A-Za-z0-9]+/g, " ").split(" ");
      },
      predict(stringCleaned){
        axios.post("https://nlp-sentiment-analysis-backend.herokuapp.com/predict", {"stringCleaned": stringCleaned}, {headers: {"Access-Control-Allow-Origin": "*"}})
        .then((result) => 
        console.log(result.data));
      },
      getTweetText(){
        if(this.$refs.form.validate()){
          let stringCleaned = this.stringCleaner(this.text);
          this.predict(stringCleaned);
        }
      }
    }

  }
</script>
